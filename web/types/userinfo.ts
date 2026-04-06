export type Role = 'normal' | 'admin';
export type PostUserAddParams = {
  user_channel: string;
  user_no: string;
  avatar_url?: string;
  role?: Role;
  nick_name?: string;
  email?: string;
  user_id?: string;
};

// eslint-disable-next-line @typescript-eslint/no-empty-object-type
export interface UserInfoResponse extends PostUserAddParams {}

export interface LoginUserRequest {
  username: string;
  password: string;
}

export interface RegisterUserRequest extends LoginUserRequest {
  confirm_password: string;
}

export interface LoginUserResponse {
  token: string;
  user_id: string;
  user_name: string;
  nick_name: string;
  role: Role;
}
