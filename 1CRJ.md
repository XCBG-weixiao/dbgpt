# 基于DBGPT 二次开发

## 后端

uv sync --all-packages \
--extra "base" \
--extra "proxy_openai" \
--extra "rag" \
--extra "storage_chromadb" \
--extra "dbgpts"

然后在 `configs/dbgpt-proxy-openai.toml` 中修改配置即可

`uv run dbgpt start webserver --config configs/dbgpt-proxy-openai.toml`

或

`uv run python packages/dbgpt-app/src/dbgpt_app/dbgpt_server.py --config configs/dbgpt-proxy-openai.toml`

## 前端

```bash
cd web
```

修改 `next.config.js`，其他的不用动，下载之前把 package-lock.json 和 node_modules 删掉

然后
```bash
npm install

npm run dev
```

## 介绍前端

参考 https://copilot.tencent.com/work/ ，写一个介绍该产品的前端页面，


## Todo

- 中断
- 需要根据对话内容决定是否可视化/报告
- skills 可视化中文编码出错












