import json
import logging
import os
import secrets
from datetime import datetime, timezone
from hashlib import sha256
from threading import RLock
from typing import Any, Dict, Optional, Tuple

from dbgpt._private.pydantic import BaseModel
from dbgpt.configs.model_config import DATA_DIR

logger = logging.getLogger(__name__)

_AUTH_DIR = os.path.join(DATA_DIR, "auth")
_AUTH_FILE = os.path.join(_AUTH_DIR, "users.json")
_LOCK = RLock()

_DEFAULT_ADMIN_USERNAME = "admin"
_DEFAULT_ADMIN_PASSWORD = "crj"


class UserRequest(BaseModel):
    user_id: Optional[str] = None
    user_no: Optional[str] = None
    real_name: Optional[str] = None
    user_name: Optional[str] = None
    user_channel: Optional[str] = None
    role: Optional[str] = "normal"
    nick_name: Optional[str] = None
    email: Optional[str] = None
    avatar_url: Optional[str] = None
    nick_name_like: Optional[str] = None


def _utcnow_str() -> str:
    return datetime.now(timezone.utc).isoformat()


def _hash_password(password: str, salt: str) -> str:
    return sha256(f"{salt}:{password}".encode("utf-8")).hexdigest()


def _default_storage() -> Dict[str, Any]:
    now = _utcnow_str()
    salt = secrets.token_hex(16)
    return {
        "users": {
            _DEFAULT_ADMIN_USERNAME: {
                "salt": salt,
                "password_hash": _hash_password(_DEFAULT_ADMIN_PASSWORD, salt),
                "role": "admin",
                "created_at": now,
            }
        },
        "sessions": {},
    }


def _ensure_storage_file() -> None:
    os.makedirs(_AUTH_DIR, exist_ok=True)
    if not os.path.exists(_AUTH_FILE):
        with open(_AUTH_FILE, "w", encoding="utf-8") as f:
            json.dump(_default_storage(), f, ensure_ascii=False, indent=2)


def _load_storage() -> Dict[str, Any]:
    _ensure_storage_file()
    with open(_AUTH_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "users" not in data or not isinstance(data["users"], dict):
        data["users"] = {}
    if "sessions" not in data or not isinstance(data["sessions"], dict):
        data["sessions"] = {}
    if _DEFAULT_ADMIN_USERNAME not in data["users"]:
        now = _utcnow_str()
        salt = secrets.token_hex(16)
        data["users"][_DEFAULT_ADMIN_USERNAME] = {
            "salt": salt,
            "password_hash": _hash_password(_DEFAULT_ADMIN_PASSWORD, salt),
            "role": "admin",
            "created_at": now,
        }
        _save_storage(data)
    return data


def _save_storage(data: Dict[str, Any]) -> None:
    os.makedirs(_AUTH_DIR, exist_ok=True)
    with open(_AUTH_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _build_user_request(username: str, user_data: Dict[str, Any]) -> UserRequest:
    role = user_data.get("role") or "normal"
    return UserRequest(
        user_id=username,
        user_name=username,
        user_no=username,
        real_name=username,
        nick_name=username,
        role=role,
    )


class UserAuthStore:
    def register_user(self, username: str, password: str) -> UserRequest:
        with _LOCK:
            data = _load_storage()
            if username in data["users"]:
                raise ValueError("Username already exists.")

            salt = secrets.token_hex(16)
            data["users"][username] = {
                "salt": salt,
                "password_hash": _hash_password(password, salt),
                "role": "normal",
                "created_at": _utcnow_str(),
            }
            _save_storage(data)
            return _build_user_request(username, data["users"][username])

    def login(self, username: str, password: str) -> Tuple[UserRequest, str]:
        with _LOCK:
            data = _load_storage()
            user_data = data["users"].get(username)
            if not user_data:
                raise ValueError("Invalid username or password.")

            expected_hash = user_data.get("password_hash")
            salt = user_data.get("salt")
            if not expected_hash or not salt:
                raise ValueError("Invalid username or password.")
            if _hash_password(password, salt) != expected_hash:
                raise ValueError("Invalid username or password.")

            token = secrets.token_urlsafe(32)
            data["sessions"][token] = {
                "username": username,
                "created_at": _utcnow_str(),
            }
            _save_storage(data)
            return _build_user_request(username, user_data), token

    def logout(self, username: str, token: str) -> None:
        with _LOCK:
            data = _load_storage()
            session = data["sessions"].get(token)
            if session and session.get("username") == username:
                data["sessions"].pop(token, None)
                _save_storage(data)

    def validate_session(
        self, username: Optional[str], token: Optional[str]
    ) -> Optional[UserRequest]:
        if not username or not token:
            return None
        with _LOCK:
            data = _load_storage()
            session = data["sessions"].get(token)
            if not session:
                return None
            session_user = session.get("username")
            if session_user != username:
                return None
            user_data = data["users"].get(session_user)
            if not user_data:
                return None
            return _build_user_request(session_user, user_data)


_AUTH_STORE: Optional[UserAuthStore] = None


def get_user_auth_store() -> UserAuthStore:
    global _AUTH_STORE
    if _AUTH_STORE is None:
        _AUTH_STORE = UserAuthStore()
    return _AUTH_STORE
