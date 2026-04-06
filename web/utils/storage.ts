import { getStoredToken, getStoredUserInfo } from './auth';
import { STORAGE_INIT_MESSAGE_KET } from './constants/index';

export function getInitMessage() {
  const value = localStorage.getItem(STORAGE_INIT_MESSAGE_KET) ?? '';
  try {
    const initData = JSON.parse(value) as { id: string; message: string };
    return initData;
  } catch {
    return null;
  }
}

export function getUserId(): string | undefined {
  return getStoredUserInfo()?.user_id;
}

export function getAuthToken(): string | undefined {
  return getStoredToken();
}
