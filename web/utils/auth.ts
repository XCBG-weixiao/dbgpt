import { LoginUserResponse, UserInfoResponse } from '@/types/userinfo';
import { STORAGE_TOKEN_KET, STORAGE_USERINFO_KEY, STORAGE_USERINFO_VALID_TIME_KEY } from '@/utils/constants';

export const AUTH_CHANGE_EVENT = 'dbgpt-auth-change';

function emitAuthChange() {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new Event(AUTH_CHANGE_EVENT));
  }
}

export function getStoredUserInfo(): UserInfoResponse | undefined {
  if (typeof window === 'undefined') {
    return undefined;
  }
  try {
    const value = window.localStorage.getItem(STORAGE_USERINFO_KEY);
    return value ? (JSON.parse(value) as UserInfoResponse) : undefined;
  } catch {
    return undefined;
  }
}

export function getStoredToken(): string | undefined {
  if (typeof window === 'undefined') {
    return undefined;
  }
  return window.localStorage.getItem(STORAGE_TOKEN_KET) ?? undefined;
}

export function isAuthenticated(): boolean {
  const user = getStoredUserInfo();
  const token = getStoredToken();
  return Boolean(user?.user_id && token);
}

export function setAuthSession(payload: LoginUserResponse) {
  if (typeof window === 'undefined') {
    return;
  }
  const userInfo: UserInfoResponse = {
    user_channel: 'dbgpt',
    user_no: payload.user_id,
    nick_name: payload.nick_name,
    role: payload.role,
    user_id: payload.user_id,
  };
  window.localStorage.setItem(STORAGE_USERINFO_KEY, JSON.stringify(userInfo));
  window.localStorage.setItem(STORAGE_TOKEN_KET, payload.token);
  window.localStorage.setItem(STORAGE_USERINFO_VALID_TIME_KEY, Date.now().toString());
  emitAuthChange();
}

export function clearAuthSession() {
  if (typeof window === 'undefined') {
    return;
  }
  window.localStorage.removeItem(STORAGE_USERINFO_KEY);
  window.localStorage.removeItem(STORAGE_TOKEN_KET);
  window.localStorage.removeItem(STORAGE_USERINFO_VALID_TIME_KEY);
  emitAuthChange();
}
