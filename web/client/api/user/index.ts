import { LoginUserRequest, LoginUserResponse, Role, UserInfoResponse } from '@/types/userinfo';
import { GET, POST } from '../index';

interface Props {
  role: Role;
}

/**
 * 查询管理员列表
 */
export const queryAdminList = (_data: Props) => {
  return Promise.resolve({
    data: {
      data: [] as UserInfoResponse[],
      err_code: null,
      err_msg: null,
      success: true,
    },
  } as any);
};

export const loginUser = (data: LoginUserRequest) => {
  return POST<LoginUserRequest, LoginUserResponse>('/api/v1/user/login', data);
};

export const registerUser = (data: LoginUserRequest & { confirm_password: string }) => {
  return POST<LoginUserRequest & { confirm_password: string }, LoginUserResponse>('/api/v1/user/register', data);
};

export const getCurrentUser = () => {
  return GET<null, UserInfoResponse>('/api/v1/user/me');
};

export const logoutUser = () => {
  return POST<null, boolean>('/api/v1/user/logout');
};
