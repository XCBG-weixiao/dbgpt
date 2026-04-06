import { apiInterceptors, getUsableModels } from '@/client/api';
import { ChatHistoryResponse, DialogueListResponse, IChatDialogueSchema } from '@/types/chat';
import { UserInfoResponse } from '@/types/userinfo';
import { AUTH_CHANGE_EVENT, getStoredToken, getStoredUserInfo } from '@/utils/auth';
import { STORAGE_THEME_KEY } from '@/utils/constants/index';
import { useRequest } from 'ahooks';
import { useSearchParams } from 'next/navigation';
import { createContext, useCallback, useEffect, useState } from 'react';

type ThemeMode = 'dark' | 'light';

interface IChatContext {
  mode: ThemeMode;
  authReady: boolean;
  isAuthenticated: boolean;
  currentUser?: UserInfoResponse;
  isContract?: boolean;
  isMenuExpand?: boolean;
  scene: IChatDialogueSchema['chat_mode'] | (string & {});
  chatId: string;
  model: string;
  modelList: string[];
  dbParam?: string;
  agent: string;
  dialogueList?: DialogueListResponse;
  setAgent?: (val: string) => void;
  setMode: (mode: ThemeMode) => void;
  setModel: (val: string) => void;
  setIsContract: (val: boolean) => void;
  setIsMenuExpand: (val: boolean) => void;
  setDbParam: (val: string) => void;
  currentDialogue?: DialogueListResponse[0];
  history: ChatHistoryResponse;
  setHistory: (val: ChatHistoryResponse) => void;
  docId?: number;
  setDocId: (docId: number) => void;
  currentDialogInfo: {
    chat_scene: string;
    app_code: string;
  };
  setCurrentDialogInfo: (val: { chat_scene: string; app_code: string }) => void;
  adminList: UserInfoResponse[];
  refreshAuth: () => void;
  refreshDialogList?: any;
}

function getDefaultTheme(): ThemeMode {
  const theme = localStorage.getItem(STORAGE_THEME_KEY) as ThemeMode;
  if (theme) return theme;
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

const ChatContext = createContext<IChatContext>({
  mode: 'light',
  authReady: false,
  isAuthenticated: false,
  currentUser: undefined,
  scene: '',
  chatId: '',
  model: '',
  modelList: [],
  dbParam: undefined,
  dialogueList: [],
  agent: '',
  setAgent: () => {},
  setModel: () => {},
  setIsContract: () => {},
  setIsMenuExpand: () => {},
  setDbParam: () => void 0,
  setMode: () => void 0,
  history: [],
  setHistory: () => {},
  docId: undefined,
  setDocId: () => {},
  currentDialogInfo: {
    chat_scene: '',
    app_code: '',
  },
  setCurrentDialogInfo: () => {},
  adminList: [],
  refreshAuth: () => {},
  refreshDialogList: () => {},
});

const ChatContextProvider = ({ children }: { children: React.ReactElement }) => {
  const searchParams = useSearchParams();
  const chatId = searchParams?.get('id') ?? '';
  const scene = searchParams?.get('scene') ?? '';
  const db_param = searchParams?.get('db_param') ?? '';
  const [isContract, setIsContract] = useState(false);
  const [model, setModel] = useState<string>('');
  const [isMenuExpand, setIsMenuExpand] = useState<boolean>(scene !== 'chat_dashboard');
  const [dbParam, setDbParam] = useState<string>(db_param);
  const [agent, setAgent] = useState<string>('');
  const [history, setHistory] = useState<ChatHistoryResponse>([]);
  const [docId, setDocId] = useState<number>();
  const [mode, setMode] = useState<ThemeMode>('light');
  const [adminList] = useState<UserInfoResponse[]>([]);
  const [authReady, setAuthReady] = useState(false);
  const [currentUser, setCurrentUser] = useState<UserInfoResponse>();
  const [authToken, setAuthToken] = useState<string>();

  const [currentDialogInfo, setCurrentDialogInfo] = useState({
    chat_scene: '',
    app_code: '',
  });

  const refreshAuth = useCallback(() => {
    setCurrentUser(getStoredUserInfo());
    setAuthToken(getStoredToken());
    setAuthReady(true);
  }, []);

  const isAuthenticated = Boolean(currentUser?.user_id && authToken);

  const { data: modelList = [], run: fetchModelList, mutate: setModelList } = useRequest(
    async () => {
      const [, res] = await apiInterceptors(getUsableModels());
      return res ?? [];
    },
    {
      manual: true,
    },
  );

  useEffect(() => {
    refreshAuth();
    const handleAuthChange = () => refreshAuth();
    window.addEventListener(AUTH_CHANGE_EVENT, handleAuthChange);
    window.addEventListener('storage', handleAuthChange);
    return () => {
      window.removeEventListener(AUTH_CHANGE_EVENT, handleAuthChange);
      window.removeEventListener('storage', handleAuthChange);
    };
  }, [refreshAuth]);

  useEffect(() => {
    setMode(getDefaultTheme());
    try {
      const dialogInfo = JSON.parse(localStorage.getItem('cur_dialog_info') || '');
      setCurrentDialogInfo(dialogInfo);
    } catch {
      setCurrentDialogInfo({
        chat_scene: '',
        app_code: '',
      });
    }
  }, []);

  useEffect(() => {
    if (authReady && isAuthenticated) {
      fetchModelList();
      return;
    }
    if (authReady) {
      setModelList([]);
      setModel('');
    }
  }, [authReady, fetchModelList, isAuthenticated, setModelList]);

  useEffect(() => {
    setModel(modelList[0] || '');
  }, [modelList]);

  const contextValue = {
    mode,
    authReady,
    isAuthenticated,
    currentUser,
    isContract,
    isMenuExpand,
    scene,
    chatId,
    model,
    modelList,
    dbParam: dbParam || db_param,
    agent,
    setAgent,
    setMode,
    setModel,
    setIsContract,
    setIsMenuExpand,
    setDbParam,
    history,
    setHistory,
    docId,
    setDocId,
    currentDialogInfo,
    setCurrentDialogInfo,
    adminList,
    refreshAuth,
  };

  return <ChatContext.Provider value={contextValue}>{children}</ChatContext.Provider>;
};

export { ChatContext, ChatContextProvider };
