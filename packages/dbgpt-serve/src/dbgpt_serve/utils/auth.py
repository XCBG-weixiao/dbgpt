import logging
from typing import Optional

from fastapi import Header, HTTPException, status

from .user_auth import UserRequest, get_user_auth_store

logger = logging.getLogger(__name__)

HEADER_USER_ID_KEY = "user-id"
HEADER_AUTH_TOKEN_KEY = "x-auth-token"


def get_user_from_headers(
    user_id: Optional[str] = Header(None, alias=HEADER_USER_ID_KEY),
    auth_token: Optional[str] = Header(None, alias=HEADER_AUTH_TOKEN_KEY),
):
    try:
        user = get_user_auth_store().validate_session(user_id, auth_token)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required.",
            )
        return user
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Authentication failed!")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication failed. {str(e)}",
        ) from e
