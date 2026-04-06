import { ChatContext } from '@/app/chat-context';
import { apiInterceptors, loginUser, logoutUser, registerUser } from '@/client/api';
import { clearAuthSession, setAuthSession } from '@/utils/auth';
import { DownOutlined, UserOutlined } from '@ant-design/icons';
import { Avatar, Button, Dropdown, Form, Input, Modal, Tabs, Typography, message } from 'antd';
import { useRouter } from 'next/router';
import { useContext, useMemo, useState } from 'react';

type AuthTab = 'login' | 'register';

function AuthControl() {
  const router = useRouter();
  const { currentUser, isAuthenticated } = useContext(ChatContext);
  const [open, setOpen] = useState(false);
  const [activeTab, setActiveTab] = useState<AuthTab>('login');
  const [submitting, setSubmitting] = useState(false);
  const [loginForm] = Form.useForm();
  const [registerForm] = Form.useForm();
  const shouldRedirectToChat =
    router.pathname === '/' || router.pathname.startsWith('/chat') || router.pathname.startsWith('/conversations');

  const menuItems = useMemo(
    () => [
      {
        key: 'logout',
        label: '\u9000\u51fa\u767b\u5f55',
      },
    ],
    [],
  );

  const handleLogin = async (values: { username: string; password: string }) => {
    setSubmitting(true);
    const [err, res] = await apiInterceptors(loginUser(values));
    setSubmitting(false);
    if (err || !res) {
      return;
    }
    setAuthSession(res);
    message.success('\u767b\u5f55\u6210\u529f');
    loginForm.resetFields();
    setOpen(false);
    if (shouldRedirectToChat) {
      router.replace('/chat');
    }
  };

  const handleRegister = async (values: { username: string; password: string; confirm_password: string }) => {
    setSubmitting(true);
    const [err, res] = await apiInterceptors(registerUser(values));
    setSubmitting(false);
    if (err || !res) {
      return;
    }
    setAuthSession(res);
    message.success('\u6ce8\u518c\u6210\u529f\uff0c\u5df2\u81ea\u52a8\u767b\u5f55');
    registerForm.resetFields();
    setOpen(false);
    if (shouldRedirectToChat) {
      router.replace('/chat');
    }
  };

  const handleLogout = async () => {
    await logoutUser().catch(() => null);
    clearAuthSession();
    message.success('\u5df2\u9000\u51fa\u767b\u5f55');
    if (shouldRedirectToChat) {
      router.replace('/chat');
      return;
    }
    router.replace(router.asPath);
  };

  return (
    <>
      {isAuthenticated ? (
        <Dropdown
          menu={{
            items: menuItems,
            onClick: ({ key }) => {
              if (key === 'logout') {
                handleLogout();
              }
            },
          }}
          trigger={['click']}
        >
          <button
            type='button'
            className='flex items-center gap-2 rounded-full border border-white/70 bg-white/85 px-3 py-2 text-sm shadow-sm backdrop-blur hover:bg-white'
          >
            <Avatar size='small' className='bg-gradient-to-tr from-[#31afff] to-[#1677ff]'>
              {currentUser?.nick_name?.slice(0, 1) || currentUser?.user_id?.slice(0, 1) || 'U'}
            </Avatar>
            <span>{currentUser?.nick_name || currentUser?.user_id}</span>
            <DownOutlined className='text-xs text-gray-500' />
          </button>
        </Dropdown>
      ) : (
        <Button type='primary' className='rounded-full' onClick={() => setOpen(true)}>
          {'\u767b\u5f55'}
        </Button>
      )}

      <Modal
        title={'\u8d26\u53f7\u767b\u5f55'}
        open={open}
        onCancel={() => setOpen(false)}
        footer={null}
        destroyOnClose
        width={420}
      >
        <Tabs
          activeKey={activeTab}
          onChange={key => setActiveTab(key as AuthTab)}
          items={[
            {
              key: 'login',
              label: '\u767b\u5f55',
              children: (
                <Form form={loginForm} layout='vertical' onFinish={handleLogin}>
                  <Form.Item
                    label={'\u7528\u6237\u540d'}
                    name='username'
                    rules={[{ required: true, message: '\u8bf7\u8f93\u5165\u7528\u6237\u540d' }]}
                  >
                    <Input prefix={<UserOutlined />} placeholder={'\u8bf7\u8f93\u5165\u7528\u6237\u540d'} />
                  </Form.Item>
                  <Form.Item
                    label={'\u5bc6\u7801'}
                    name='password'
                    rules={[{ required: true, message: '\u8bf7\u8f93\u5165\u5bc6\u7801' }]}
                  >
                    <Input.Password placeholder={'\u8bf7\u8f93\u5165\u5bc6\u7801'} />
                  </Form.Item>
                  <Typography.Paragraph type='secondary' className='mb-4 text-xs'>
                    {'\u521d\u59cb\u8d26\u53f7\uff1aadmin / crj'}
                  </Typography.Paragraph>
                  <Button type='primary' htmlType='submit' loading={submitting} block>
                    {'\u767b\u5f55'}
                  </Button>
                </Form>
              ),
            },
            {
              key: 'register',
              label: '\u6ce8\u518c',
              children: (
                <Form form={registerForm} layout='vertical' onFinish={handleRegister}>
                  <Form.Item
                    label={'\u7528\u6237\u540d'}
                    name='username'
                    rules={[{ required: true, message: '\u8bf7\u8f93\u5165\u7528\u6237\u540d' }]}
                  >
                    <Input prefix={<UserOutlined />} placeholder={'\u8bf7\u8f93\u5165\u7528\u6237\u540d'} />
                  </Form.Item>
                  <Form.Item
                    label={'\u5bc6\u7801'}
                    name='password'
                    rules={[{ required: true, message: '\u8bf7\u8f93\u5165\u5bc6\u7801' }]}
                  >
                    <Input.Password placeholder={'\u8bf7\u8f93\u5165\u5bc6\u7801'} />
                  </Form.Item>
                  <Form.Item
                    label={'\u786e\u8ba4\u5bc6\u7801'}
                    name='confirm_password'
                    dependencies={['password']}
                    rules={[
                      { required: true, message: '\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801' },
                      ({ getFieldValue }) => ({
                        validator(_, value) {
                          if (!value || getFieldValue('password') === value) {
                            return Promise.resolve();
                          }
                          return Promise.reject(new Error('\u4e24\u6b21\u8f93\u5165\u7684\u5bc6\u7801\u4e0d\u4e00\u81f4'));
                        },
                      }),
                    ]}
                  >
                    <Input.Password placeholder={'\u8bf7\u518d\u6b21\u8f93\u5165\u5bc6\u7801'} />
                  </Form.Item>
                  <Button type='primary' htmlType='submit' loading={submitting} block>
                    {'\u6ce8\u518c\u5e76\u767b\u5f55'}
                  </Button>
                </Form>
              ),
            },
          ]}
        />
      </Modal>
    </>
  );
}

export default AuthControl;
