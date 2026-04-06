import { ChatContext, ChatContextProvider } from '@/app/chat-context';
import SideBar from '@/components/layout/side-bar';
import AuthControl from '@/new-components/layout/AuthControl';
import FloatHelper from '@/new-components/layout/FloatHelper';
import { STORAGE_LANG_KEY } from '@/utils/constants/index';
import { App, ConfigProvider, MappingAlgorithm, theme } from 'antd';
import enUS from 'antd/locale/en_US';
import zhCN from 'antd/locale/zh_CN';
import classNames from 'classnames';
import type { AppProps } from 'next/app';
import Head from 'next/head';
import { useRouter } from 'next/router';
import React, { useContext, useEffect } from 'react';
import { useTranslation } from 'react-i18next';
import '../app/i18n';
import '../nprogress.css';
import '../styles/globals.css';

const antdDarkTheme: MappingAlgorithm = (seedToken, mapToken) => {
  return {
    ...theme.darkAlgorithm(seedToken, mapToken),
    colorBgBase: '#232734',
    colorBorder: '#828282',
    colorBgContainer: '#232734',
  };
};

function CssWrapper({ children }: { children: React.ReactElement }) {
  const { mode } = useContext(ChatContext);
  const { i18n } = useTranslation();

  useEffect(() => {
    if (mode) {
      document.body?.classList?.add(mode);
      if (mode === 'light') {
        document.body?.classList?.remove('dark');
      } else {
        document.body?.classList?.remove('light');
      }
    }
  }, [mode]);

  useEffect(() => {
    i18n.changeLanguage?.(window.localStorage.getItem(STORAGE_LANG_KEY) || 'zh');
  }, [i18n]);

  return <div>{children}</div>;
}

function LayoutWrapper({ children }: { children: React.ReactNode }) {
  const { isMenuExpand, mode, authReady, isAuthenticated } = useContext(ChatContext);
  const { i18n } = useTranslation();
  const router = useRouter();

  const isShareRoute = router.pathname.startsWith('/share');
  const isProtectedChatRoute =
    router.pathname === '/' || router.pathname.startsWith('/chat') || router.pathname.startsWith('/conversations');

  const renderAuthRequired = () => (
    <div className='flex h-full items-center justify-center px-6'>
      <div className='max-w-md rounded-3xl border border-white/70 bg-white/85 p-8 text-center shadow-xl backdrop-blur'>
        <div className='mb-3 text-2xl font-semibold text-[#1c2533]'>请先登录后再开始对话</div>
        <div className='mb-2 text-sm text-gray-600'>右上角可以登录或注册账号，登录后才能发起对话并查看自己的历史记录。</div>
        <div className='text-xs text-gray-500'>内置初始账户：admin / crj</div>
      </div>
    </div>
  );

  const content = isProtectedChatRoute && !isAuthenticated ? renderAuthRequired() : children;

  if (!authReady && !isShareRoute) {
    return null;
  }

  const renderContent = () => {
    if (router.pathname.includes('mobile') || isShareRoute) {
      return (
        <div className='relative h-full'>
          {!isShareRoute && (
            <div className='fixed right-4 top-4 z-50'>
              <AuthControl />
            </div>
          )}
          {content}
        </div>
      );
    }
    return (
      <div className='relative flex h-screen w-screen overflow-hidden'>
        <Head>
          <meta name='viewport' content='initial-scale=1.0, width=device-width, maximum-scale=1' />
        </Head>
        <div className='absolute right-4 top-4 z-50'>
          <AuthControl />
        </div>
        {router.pathname !== '/construct/app/extra' && (
          <div className={classNames('hidden transition-[width] md:block', isMenuExpand ? 'w-60' : 'w-20')}>
            <SideBar />
          </div>
        )}
        <div className='relative flex flex-1 flex-col overflow-hidden'>{content}</div>
        <FloatHelper />
      </div>
    );
  };

  return (
    <ConfigProvider
      locale={i18n.language === 'en' ? enUS : zhCN}
      theme={{
        token: {
          colorPrimary: '#0C75FC',
          borderRadius: 4,
        },
        algorithm: mode === 'dark' ? antdDarkTheme : undefined,
      }}
    >
      <App>{renderContent()}</App>
    </ConfigProvider>
  );
}

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ChatContextProvider>
      <CssWrapper>
        <LayoutWrapper>
          <Component {...pageProps} />
        </LayoutWrapper>
      </CssWrapper>
    </ChatContextProvider>
  );
}

export default MyApp;
