# <img src="./assets/LOGO_SMALL.png" alt="Logo" style="vertical-align: middle; height: 24px;" /> DB-GPT：开源 Agentic AI 数据分析智能助手

<p align="left">
  <img src="./assets/dbgpt_vision.png" width="100%" />
</p>


<div align="center">
  <p>
    <a href="https://github.com/eosphoros-ai/DB-GPT">
        <img alt="stars" src="https://img.shields.io/github/stars/eosphoros-ai/db-gpt?style=social" />
    </a>
    <a href="https://github.com/eosphoros-ai/DB-GPT">
        <img alt="forks" src="https://img.shields.io/github/forks/eosphoros-ai/db-gpt?style=social" />
    </a>
    <a href="http://dbgpt.cn/">
        <img alt="Official Website" src="https://img.shields.io/badge/Official%20website-DB--GPT-blue?style=flat&labelColor=3366CC" />
    </a>
    <a href="https://opensource.org/licenses/MIT">
      <img alt="License: MIT" src="https://img.shields.io/github/license/eosphoros-ai/db-gpt?style=flat&labelColor=009966&color=009933" />
    </a>
     <a href="https://github.com/eosphoros-ai/DB-GPT/releases">
      <img alt="Release Notes" src="https://img.shields.io/github/v/release/eosphoros-ai/db-gpt?style=flat&labelColor=FF9933&color=FF6633" />
    </a>
    <a href="https://github.com/eosphoros-ai/DB-GPT/issues">
      <img alt="Open Issues" src="https://img.shields.io/github/issues-raw/eosphoros-ai/db-gpt?style=flat&labelColor=666666&color=333333" />
    </a>
    <a href="https://x.com/DBGPT_AI">
      <img alt="X (formerly Twitter) Follow" src="https://img.shields.io/twitter/follow/DBGPT_AI" />
    </a>
    <a href="https://medium.com/@dbgpt0506">
      <img alt="Medium Follow" src="https://badgen.net/badge/Medium/DB-GPT/333333?icon=medium&labelColor=666666" />
    </a>
    <a href="https://space.bilibili.com/3537113070963392">
      <img alt="Bilibili Space" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.bilibili.com%2Fx%2Frelation%2Fstat%3Fvmid%3D3537113070963392&query=data.follower&style=flat&logo=bilibili&logoColor=white&label=Bilibili%20Fans&labelColor=F37697&color=6495ED" />
    </a>
    <a href="https://join.slack.com/t/slack-inu2564/shared_invite/zt-29rcnyw2b-N~ubOD9kFc7b7MDOAM1otA">
      <img alt="Slack" src="https://img.shields.io/badge/Slack-Join%20us-5d6b98?style=flat&logo=slack&labelColor=7d89b0" />
    </a>
    <a href="https://codespaces.new/eosphoros-ai/DB-GPT">
      <img alt="Open in GitHub Codespaces" src="https://github.com/codespaces/badge.svg" />
    </a>
  </p>

[![English](https://img.shields.io/badge/English-d9d9d9?style=flat-square)](README.md)
[![简体中文](https://img.shields.io/badge/简体中文-d9d9d9?style=flat-square)](README.zh.md)
[![日本語](https://img.shields.io/badge/日本語-d9d9d9?style=flat-square)](README.ja.md) 

[**文档**](http://docs.dbgpt.cn/docs/overview/) | [**联系团队**](https://github.com/eosphoros-ai/DB-GPT/blob/main/README.zh.md#%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC) | [**社区**](https://github.com/eosphoros-ai/community) | [**Paper**](https://arxiv.org/pdf/2312.17449.pdf)

</div>

> **一个开源的 AI 数据分析智能助手：连接你的数据，自主编写 SQL 与代码，在沙箱环境中运行 skills，把分析转化为报告、洞察与行动。**

## DB-GPT 是什么？

DB-GPT 是一个开源的 **Agentic AI 数据分析智能助手**，面向下一代 **AI + Data** 产品形态。

它可以帮助用户和团队：
- 连接 **数据库、CSV / Excel、数仓、知识库与文档**
- 使用自然语言提问，并让 AI **自主编写 SQL**
- 执行 **Python 与代码驱动的数据分析流程**
- 加载并执行可复用的 **skills**
- 自动生成 **图表、Dashboard、HTML 报告和分析总结**
- 在 **沙箱环境** 中安全执行分析任务

DB-GPT 不只是一个助手界面，它同时也是一个平台，用于构建 **AI Native 数据智能体、工作流与应用**，底层支持 agents、AWEL、RAG 与多模型能力。

## 为什么选择 DB-GPT？

### 1. Agentic 数据分析
它不只是回答问题，而是会进行任务规划、步骤拆解、工具调用和迭代式分析。
![csv-data-analysis_skill](https://github.com/user-attachments/assets/de0073f6-6b69-42f1-9fd2-5b759ca88ed8)

### 2. 自主 SQL + 自主代码执行
自动编写 SQL 和代码，用于查询数据、处理数据、计算指标并生成结果。
![agentic_write_code](https://github.com/user-attachments/assets/aeebc2b8-6c50-4ebb-96fd-07b860faa044)
![sql_query](https://github.com/user-attachments/assets/da45de20-3768-4f0d-ab20-e939ddf21361)

### 3. 多数据源分析
同时处理结构化与非结构化数据，包括数据库、表格文件、文档和知识库。
![datasource](./assets/datasources.png)

### 4. Skills 驱动的可扩展能力
将领域知识、分析方法和执行流程沉淀为 skills，实现复用与扩展。

![import_github_skill](https://github.com/user-attachments/assets/39f39c36-a014-4a2e-8e14-b3af3f1d2f1c)

### 5. 沙箱安全执行
在隔离环境中运行代码和工具，让分析过程更安全、更可控。
![sandbox](https://github.com/user-attachments/assets/bfbd78e0-15e2-42ac-876f-5b91847aadc1)

## 你可以用 DB-GPT 做什么？

- **分析 CSV / Excel 文件** 并生成可视化报告
- **连接数据库** 自动生成数据库画像与分析报告
- 用自然语言提问，让 AI **自动写 SQL**
- 进行 **财报深度分析**，生成图表、分析结论与总结
- 创建和复用 **SQL 分析技能**
- 将 **代码、SQL、检索和工具调用** 组合成完整的 agentic 分析流程
- 构建面向团队或产品的下一代 **AI + Data 智能助手**

## 产品工作流

### 数据探索
连接文件、数据库和知识库，在统一入口开始分析任务。

### 规划与执行
让 AI 进行任务推理、生成 SQL / 代码，并逐步完成分析。

### 使用 Skills
加载可复用的业务分析技能与领域工作流。

### 生成报告
自动输出图表、Dashboard、HTML 报告和决策结论。


## 快速开始

你可以通过一键安装脚本在几分钟内启动 DB-GPT（macOS / Linux）：

```bash
curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh | bash
```

也可以直接指定 profile 和 API Key：

```bash
curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh \
  | OPENAI_API_KEY=sk-xxx bash -s -- --profile openai
```

如果你想使用 Kimi 2.5（Moonshot API）：

```bash
curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh \
  | MOONSHOT_API_KEY=sk-xxx bash -s -- --profile kimi
```

如果你想使用 MiniMax（OpenAI 兼容接口）：

```bash
curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh \
  | MINIMAX_API_KEY=sk-xxx bash -s -- --profile minimax
```

如果你已经有本地 DB-GPT 仓库，也可以直接复用当前仓库，跳过 `~/.dbgpt/DB-GPT` 的重复 clone：

```bash
OPENAI_API_KEY=sk-xxx \
  bash scripts/install/install.sh --profile openai --repo-dir "$(pwd)" --yes
```

如果你想在当前仓库里直接测试 Kimi 2.5：

```bash
MOONSHOT_API_KEY=sk-xxx \
  bash scripts/install/install.sh --profile kimi --repo-dir "$(pwd)" --yes
```

如果你想在当前仓库里直接测试 MiniMax：

```bash
MINIMAX_API_KEY=sk-xxx \
  bash scripts/install/install.sh --profile minimax --repo-dir "$(pwd)" --yes
```

安装完成后，使用生成的 profile 配置启动服务：

```bash
cd ~/.dbgpt/DB-GPT && uv run dbgpt start webserver --profile <profile>
```

然后打开 [http://localhost:5670](http://localhost:5670)。

> **想先审阅安装脚本再执行？**
> ```bash
> curl -fsSL https://raw.githubusercontent.com/eosphoros-ai/DB-GPT/main/scripts/install/install.sh -o install.sh
> less install.sh
> bash install.sh --profile openai
> ```

### 通过 PyPI 安装

从 PyPI 安装 DB-GPT，一条命令即可启动，无需克隆源码仓库。

> **前置条件：** Python **3.10+**，推荐使用 [uv](https://docs.astral.sh/uv/getting-started/installation/) 包管理器，也支持 pip。

**1. 安装**

```bash
# 推荐使用 uv
uv pip install dbgpt-app

# 或使用 pip
pip install dbgpt-app
```

默认安装包含核心框架（CLI、FastAPI、Agent）、OpenAI 兼容 LLM 支持、DashScope / 通义支持、RAG 文档解析和 ChromaDB 向量存储。

**2. 启动**

```bash
dbgpt start
```

首次运行时，交互式向导会引导你选择 LLM 提供商并输入 API Key，配置完成后服务自动启动。

**3. 打开 Web 界面**

访问 [http://localhost:5670](http://localhost:5670) — 开始使用！🎉

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

[**教程**](https://www.yuque.com/eosphoros/dbgpt-docs/bex30nsv60ru0fmx)
- [**快速开始**](https://www.yuque.com/eosphoros/dbgpt-docs/ew0kf1plm0bru2ga)
  - [源码安装](https://www.yuque.com/eosphoros/dbgpt-docs/urh3fcx8tu0s9xmb)
  - [Docker安装](https://www.yuque.com/eosphoros/dbgpt-docs/glf87qg4xxcyrp89)
  - [Docker Compose安装](https://www.yuque.com/eosphoros/dbgpt-docs/wwdu11e0v5nkfzin)
- [**使用手册**](https://www.yuque.com/eosphoros/dbgpt-docs/tkspdd0tcy2vlnu4)
  - [知识库](https://www.yuque.com/eosphoros/dbgpt-docs/ycyz3d9b62fccqxh)
  - [数据对话](https://www.yuque.com/eosphoros/dbgpt-docs/gd9hbhi1dextqgbz)
  - [Excel对话](https://www.yuque.com/eosphoros/dbgpt-docs/prugoype0xd2g4bb)
  - [数据库对话](https://www.yuque.com/eosphoros/dbgpt-docs/wswpv3zcm2c9snmg)
  - [报表分析](https://www.yuque.com/eosphoros/dbgpt-docs/vsv49p33eg4p5xc1)
  - [Agents](https://www.yuque.com/eosphoros/dbgpt-docs/pom41m7oqtdd57hm)
- [**进阶教程**](https://www.yuque.com/eosphoros/dbgpt-docs/dxalqb8wsv2xkm5f)
  - [数智应用开发](https://www.yuque.com/eosphoros/dbgpt-docs/ancwnrsk9agc6e4w)
  - [智能体工作流使用](https://www.yuque.com/eosphoros/dbgpt-docs/hcomfb3yrleg7gmq)
  - [智能应用使用](https://www.yuque.com/eosphoros/dbgpt-docs/aiagvxeb86iarq6r)
  - [多模型管理](https://www.yuque.com/eosphoros/dbgpt-docs/huzgcf2abzvqy8uv)
  - [命令行使用](https://www.yuque.com/eosphoros/dbgpt-docs/gd4kgumgd004aly8)
- [**模型服务部署**](https://www.yuque.com/eosphoros/dbgpt-docs/vubxiv9cqed5mc6o)
  - [单机部署](https://www.yuque.com/eosphoros/dbgpt-docs/kwg1ed88lu5fgawb)
  - [集群部署](https://www.yuque.com/eosphoros/dbgpt-docs/gmbp9619ytyn2v1s)
  - [vLLM](https://www.yuque.com/eosphoros/dbgpt-docs/bhy9igdvanx1uluf)
- [**如何Debug**](https://www.yuque.com/eosphoros/dbgpt-docs/eyg0ocbc2ce3q95r)
- [**AWEL**](https://www.yuque.com/eosphoros/dbgpt-docs/zozbzslbfk0m0op5)
- [**FAQ**](https://www.yuque.com/eosphoros/dbgpt-docs/gomtc46qonmyt44l)

## 核心能力

### Agentic 数据分析
- 任务规划
- 分步执行
- 工具调用
- 迭代式推理

### SQL + 代码执行
- 自然语言转 SQL
- Python 数据分析与处理
- 指标计算
- 图表生成

### 多数据源访问
- 关系型数据库
- CSV / Excel
- 文档
- 知识库
- 多源混合分析

### Skills 与 Agents
- 可复用 skills
- 领域分析工作流
- agent 编排
- 可定制执行流程

### 报告与决策支持
- 数据库画像报告
- 财报分析报告
- 可视化报告与 dashboard
- 分析总结与业务洞察

### 安全执行环境
- 沙箱代码执行
- 可控工具调用
- 可复现的分析产物与 artifacts


#### DeepWiki
- [DB-GPT](https://deepwiki.com/eosphoros-ai/DB-GPT)
- [DB-GPT-HUB](https://deepwiki.com/eosphoros-ai/DB-GPT-Hub)
- [dbgpts](https://deepwiki.com/eosphoros-ai/dbgpts)

#### Text2SQL 微调模型

|     LLM     |  Supported  |
|:-----------:|:-----------:|
|    LLaMA    |      ✅     |
|   LLaMA-2   |      ✅     |
|    BLOOM    |      ✅     |
|   BLOOMZ    |      ✅     |
|   Falcon    |      ✅     |
|  Baichuan   |      ✅     |
|  Baichuan2  |      ✅     |
|  InternLM   |      ✅     |
|    Qwen     |      ✅     |
|   XVERSE    |      ✅     |
|  ChatGLM2   |      ✅     |

### 支持模型

<table>
      <thead>
        <tr>
          <th>Provider</th>
          <th>Supported</th>
          <th>Models</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td align="center" valign="middle">DeepSeek</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-R1-0528">DeepSeek-R1-0528</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-V3-0324">DeepSeek-V3-0324</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-R1">DeepSeek-R1</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-V3">DeepSeek-V3</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B">DeepSeek-R1-Distill-Llama-70B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B">DeepSeek-R1-Distill-Qwen-32B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct">DeepSeek-Coder-V2-Instruct</a><br/>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Qwen</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen3-235B-A22B">Qwen3-235B-A22B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen3-30B-A3B">Qwen3-30B-A3B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen3-32B">Qwen3-32B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/QwQ-32B">QwQ-32B</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct">Qwen2.5-Coder-32B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct">Qwen2.5-Coder-14B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen2.5-72B-Instruct">Qwen2.5-72B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/Qwen/Qwen2.5-32B-Instruct">Qwen2.5-32B-Instruct</a><br/>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">GLM</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/THUDM/GLM-Z1-32B-0414">GLM-Z1-32B-0414</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/THUDM/GLM-4-32B-0414">GLM-4-32B-0414</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/THUDM/glm-4-9b-chat">Glm-4-9b-chat</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Llama</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3.1-405B-Instruct">Meta-Llama-3.1-405B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct">Meta-Llama-3.1-70B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct">Meta-Llama-3.1-8B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3-70B-Instruct">Meta-Llama-3-70B-Instruct</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct">Meta-Llama-3-8B-Instruct</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Gemma</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/google/gemma-2-27b-it">gemma-2-27b-it</a><br>
            🔥🔥🔥  <a href="https://huggingface.co/google/gemma-2-9b-it">gemma-2-9b-it</a><br>
            🔥🔥🔥  <a href="https://huggingface.co/google/gemma-7b-it">gemma-7b-it</a><br>
            🔥🔥🔥  <a href="https://huggingface.co/google/gemma-2b-it">gemma-2b-it</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Yi</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/01-ai/Yi-1.5-34B-Chat">Yi-1.5-34B-Chat</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/01-ai/Yi-1.5-9B-Chat">Yi-1.5-9B-Chat</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/01-ai/Yi-1.5-6B-Chat">Yi-1.5-6B-Chat</a><br/>
            🔥🔥🔥  <a href="https://huggingface.co/01-ai/Yi-34B-Chat">Yi-34B-Chat</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Starling</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/Nexusflow/Starling-LM-7B-beta">Starling-LM-7B-beta</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">SOLAR</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0">SOLAR-10.7B</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Mixtral</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1">Mixtral-8x7B</a>
          </td>
        </tr>
        <tr>
          <td align="center" valign="middle">Phi</td>
          <td align="center" valign="middle">✅</td>
          <td>
            🔥🔥🔥  <a href="https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3">Phi-3</a>
          </td>
        </tr>
      </tbody>
    </table>

  - [更多开源模型](https://www.yuque.com/eosphoros/dbgpt-docs/iqaaqwriwhp6zslc#qQktR)

  - 支持在线代理模型
    - [x] [DeepSeek.deepseek-chat](https://platform.deepseek.com/api-docs/)
    - [x] [Ollama.API](https://github.com/ollama/ollama/blob/main/docs/api.md)
    - [x] [月之暗面.Moonshot](https://platform.moonshot.cn/docs/)
    - [x] [零一万物.Yi](https://platform.lingyiwanwu.com/docs)
    - [x] [OpenAI·ChatGPT](https://api.openai.com/)
    - [x] [百川·Baichuan](https://platform.baichuan-ai.com/)
    - [x] [阿里·通义](https://www.aliyun.com/product/dashscope)
    - [x] [百度·文心](https://cloud.baidu.com/product/wenxinworkshop?track=dingbutonglan)
    - [x] [智谱·ChatGLM](http://open.bigmodel.cn/)
    - [x] [讯飞·星火](https://xinghuo.xfyun.cn/)
    - [x] [Google·Bard](https://bard.google.com/)
    - [x] [Google·Gemini](https://makersuite.google.com/app/apikey)

### 隐私安全

通过私有化大模型、代理脱敏和沙箱执行等机制保障数据隐私与执行安全。

### 数据源
- [支持数据源](https://www.yuque.com/eosphoros/dbgpt-docs/rc4r27ybmdwg9472)

## 愿景

我们相信，未来的数据产品不应止于 Dashboard。

下一代 **AI + Data** 产品将是：
- **agentic**
- **多数据源**
- **skill-driven**
- **sandboxed**
- 能自主编写 **SQL 和代码**
- 能把分析转化为 **报告、结论与行动**

DB-GPT 希望帮助开发者与企业共同构建这样的未来。



## Image

🌐 [小程序云部署](https://www.yuque.com/eosphoros/dbgpt-docs/ek12ly8k661tbyn8)

## 使用说明

### 多模型使用

- [使用指南](https://www.yuque.com/eosphoros/dbgpt-docs/huzgcf2abzvqy8uv)

### 数据Agents使用

- [数据Agents](https://www.yuque.com/eosphoros/dbgpt-docs/gwz4rayfuwz78fbq)

## 贡献

更加详细的贡献指南请参考[如何贡献](https://github.com/eosphoros-ai/DB-GPT/blob/main/CONTRIBUTING.md)。

这是一个用于数据库的复杂且创新的工具, 我们的项目也在紧急的开发当中, 会陆续发布一些新的feature。如在使用当中有任何具体问题, 优先在项目下提issue, 如有需要, 请联系如下微信，我会尽力提供帮助，同时也非常欢迎大家参与到项目建设中。

### 贡献者榜单 
<a href="https://github.com/eosphoros-ai/DB-GPT/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=eosphoros-ai/DB-GPT&max=200" />
</a>


## Licence

The MIT License (MIT)

### 免责声明

- [免责声明](./DISCKAIMER.md)

## 引用
如果您发现`DB-GPT`对您的研究或开发有用，请引用以下论文，其中：

如果您想了解DB-GPT整体架构，请引用<a href="https://arxiv.org/abs/2312.17449" target="_blank">论文</a>和<a href="https://arxiv.org/abs/2404.10209" target="_blank">论文</a>

如果您想了解使用DB-GPT进行Agent开发相关的内容，请引用<a href="https://arxiv.org/abs/2412.13520" target="_blank">论文</a>

```bibtex
@article{xue2023dbgpt,
      title={DB-GPT: Empowering Database Interactions with Private Large Language Models}, 
      author={Siqiao Xue and Caigao Jiang and Wenhui Shi and Fangyin Cheng and Keting Chen and Hongjun Yang and Zhiping Zhang and Jianshan He and Hongyang Zhang and Ganglin Wei and Wang Zhao and Fan Zhou and Danrui Qi and Hong Yi and Shaodong Liu and Faqiang Chen},
      year={2023},
      journal={arXiv preprint arXiv:2312.17449},
      url={https://arxiv.org/abs/2312.17449}
}
@misc{huang2024romasrolebasedmultiagentdatabase,
      title={ROMAS: A Role-Based Multi-Agent System for Database monitoring and Planning}, 
      author={Yi Huang and Fangyin Cheng and Fan Zhou and Jiahui Li and Jian Gong and Hongjun Yang and Zhidong Fan and Caigao Jiang and Siqiao Xue and Faqiang Chen},
      year={2024},
      eprint={2412.13520},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2412.13520}, 
}
@inproceedings{xue2024demonstration,
      title={Demonstration of DB-GPT: Next Generation Data Interaction System Empowered by Large Language Models}, 
      author={Siqiao Xue and Danrui Qi and Caigao Jiang and Wenhui Shi and Fangyin Cheng and Keting Chen and Hongjun Yang and Zhiping Zhang and Jianshan He and Hongyang Zhang and Ganglin Wei and Wang Zhao and Fan Zhou and Hong Yi and Shaodong Liu and Hongjun Yang and Faqiang Chen},
      year={2024},
      booktitle = "Proceedings of the VLDB Endowment",
      url={https://arxiv.org/abs/2404.10209}
}
```

## 联系我们

  **说明: 由于微信群人数上限的限制, 我们的答疑与问题支持优先会在钉钉大群进行。**
<div style="display: flex; justify-content: space-around;">
    <figure style="display: flex; flex-direction: column;">
        <img src="./assets/ding.jpg" alt="图片2" style="width: 220px;">
        <p style="text-align: center;">
          钉钉
        </p>
    </figure>
</div>
[![Star History Chart](https://api.star-history.com/svg?repos=csunny/DB-GPT&type=Date)](https://star-history.com/#csunny/DB-GPT)

## 修改后启动指南

#### windows



在 Windows PowerShell 下，最稳妥的启动顺序我建议分成两种。

**1. 只启动 DB-GPT 后端/内置 Web 服务**
这个适合先把 Python 服务跑起来。项目要求 Python 3.11，见 [.python-version](app://-/index.html?hostId=local)，源码安装文档推荐 uv sync + uv run dbgpt start webserver，见 [docs/docs/quickstart.md](app://-/index.html?hostId=local)。

在仓库根目录 D:\pythonProjects\DB-GPT-main 执行：

```
cd D:\pythonProjects\DB-GPT-main uv python install 3.11 uv venv --python 3.11 uv sync --all-packages --extra "base" --extra "proxy_openai" --extra "rag" $env:OPENAI_API_KEY = "你的_OPENAI_API_KEY" uv run dbgpt start webserver --config configs/dbgpt-proxy-openai.toml 
```

启动后访问：

```
http://localhost:5670 
```

如果你用 DeepSeek，可以改成：

```
uv sync --all-packages --extra "base" --extra "proxy_openai" --extra "rag" --extra "hf" $env:OPENAI_API_KEY = "你的_DeepSeek_API_Key" uv run dbgpt start webserver --config configs/dbgpt-proxy-deepseek.toml 
```

可用配置文件都在 [configs](app://-/index.html?hostId=local) 目录，比如：

- [configs/dbgpt-proxy-openai.toml](app://-/index.html?hostId=local)
- [configs/dbgpt-proxy-deepseek.toml](app://-/index.html?hostId=local)
- [configs/dbgpt-local-glm.toml](app://-/index.html?hostId=local)

**2. 如果你要看到 web/ 里前端源码的改动**
你这次改的是 [web](app://-/index.html?hostId=local) 下的前端代码，所以最稳妥的是前后端分开跑。uv 只负责 Python 后端，前端仍然按 [web/README.md](app://-/index.html?hostId=local) 用 Next.js dev server 启动。

先开第一个 PowerShell 跑后端：

```
cd D:\pythonProjects\DB-GPT-main uv python install 3.11 uv venv --python 3.11 uv sync --all-packages --extra "base" --extra "proxy_openai" --extra "rag" $env:OPENAI_API_KEY = "你的_OPENAI_API_KEY" uv run dbgpt start webserver --config configs/dbgpt-proxy-openai.toml 
```

再开第二个 PowerShell 跑前端：

```
cd D:\pythonProjects\DB-GPT-main\web copy .env.template .env 
```

把 .env 里的 API_BASE_URL 改成后端地址，例如：

```
API_BASE_URL=http://127.0.0.1:5670 
```

然后执行：

```
npm install npm run dev 
```

前端开发地址通常是：

```
http://localhost:3000 
```

**3. 关于 CLI 怎么用**
如果你已经 uv sync 完成了，CLI 当然还能用。最稳的是直接：

```
uv run dbgpt start webserver --config configs/dbgpt-proxy-openai.toml 
```

如果你想激活虚拟环境再用，也可以：

```
.\.venv\Scripts\Activate.ps1 dbgpt start webserver --config configs/dbgpt-proxy-openai.toml 
```

我建议你在 Windows 下优先用 uv run ...，比手动激活环境更稳，少掉很多 PATH 和 PowerShell 执行策略问题。

如果你愿意，我可以下一步直接按你现在这个仓库状态，给你一份“OpenAI 代理模式”和“一份本地模型模式”的 Windows 启动清单。

#### linux

下面给你一份基于当前源码仓库、适用于 Linux 的启动指南。按这套做，可以跑到你本地修改后的代码，不会误用之前 pip install dbgpt 的旧版本。

**推荐方式**
优先用 uv + 当前仓库源码启动。

**一、准备环境**

安装基础依赖：

```
sudo apt update sudo apt install -y git curl build-essential pkg-config python3-dev 
```

安装 uv：

```
curl -LsSf https://astral.sh/uv/install.sh | sh source ~/.bashrc 
```

确认版本：

```
uv --version 
```

如果你要同时跑前端开发版，还需要 Node.js 18+ 和 npm：

```
node -v npm -v 
```

**二、进入项目**

```
cd /path/to/DB-GPT-main 
```

建议先确认 Python 版本，仓库里要求的是 3.11。

**三、创建虚拟环境并安装源码依赖**

如果你是 OpenAI 代理模式，先执行：

```
uv python install 3.11 uv venv --python 3.11 uv sync --all-packages --extra "base" --extra "proxy_openai" --extra "rag" 
```

如果你想用 DeepSeek，并且还要本地 embedding / HF 相关能力，可以用：

```
uv python install 3.11 uv venv --python 3.11 uv sync --all-packages --extra "base" --extra "proxy_openai" --extra "rag" --extra "hf" 
```

这一步完成后，当前仓库自己的 .venv 和本地源码会关联起来。

**四、启动后端服务**

OpenAI 代理模式：

```
export OPENAI_API_KEY="你的_API_KEY" uv run dbgpt start webserver --config configs/dbgpt-proxy-openai.toml 
```

DeepSeek 代理模式：

```
export OPENAI_API_KEY="你的_DeepSeek_API_Key" uv run dbgpt start webserver --config configs/dbgpt-proxy-deepseek.toml 
```

启动后访问：

```
http://127.0.0.1:5670 
```

**五、如果你要跑到这次修改过的前端源码**

因为你这次改了 web/ 下的前端，所以最稳妥的是前后端分开跑。

先开终端 1，启动后端：

```
cd /path/to/DB-GPT-main export OPENAI_API_KEY="你的_API_KEY" uv run dbgpt start webserver --config configs/dbgpt-proxy-openai.toml 
```

再开终端 2，启动前端：

```
cd /path/to/DB-GPT-main/web cp .env.template .env 
```

把 .env 里的 API_BASE_URL 改成：

```
API_BASE_URL=http://127.0.0.1:5670 
```

然后执行：

```
npm install npm run dev 
```

前端访问地址一般是：

```
http://127.0.0.1:3000 
```

这样你看到的就是你当前源码里的前端改动，包括登录/注册界面。

**六、还能不能用 dbgpt start**

可以，但有前提。

如果你想直接用 dbgpt start，要先进入当前仓库的虚拟环境：

```
cd /path/to/DB-GPT-main source .venv/bin/activate dbgpt start webserver --config configs/dbgpt-proxy-openai.toml 
```

更推荐的仍然是：

```
uv run dbgpt start webserver --config configs/dbgpt-proxy-openai.toml 
```

因为它不容易串到系统里以前 pip install dbgpt 的旧版本。

**七、如果你只想用 PyPI 版本，不关心本地修改**

那就不是运行当前仓库代码，而是运行发布版：

```
uv venv --python 3.11 source .venv/bin/activate uv pip install dbgpt-app dbgpt start 
```

但这不会包含你当前仓库里新改的登录功能。

**八、最常见问题**

1. dbgpt: command not found
   原因通常是你没激活 .venv，或者没用 uv run。
   优先改用：

```
uv run dbgpt start webserver --config configs/dbgpt-proxy-openai.toml 
```

1. 启动了但看不到前端改动
   说明你只跑了 Python 后端，没有跑 web/ 的前端开发服务，或者用的是旧静态资源。
2. 用了全局 pip install dbgpt 后命令冲突
   优先不要直接敲全局 dbgpt，而是始终在仓库里用：

```
uv run dbgpt ... 
```

如果你要，我可以继续给你补一份：

- “Linux 下 OpenAI 模式一键启动版”
- 或者“Linux 下前后端双进程启动版”
  我可以直接写成可复制的 shell 脚本。

## 代码解读

**整体结构**
这个 agent 框架是典型的“协议层 + 运行时 + 能力插件 + 编排层 + 服务装配层”设计。核心代码在 [packages/dbgpt-core/src/dbgpt/agent/**init**.py](app://-/index.html?hostId=local)，服务接入在 [packages/dbgpt-serve/src/dbgpt_serve/agent/agents/app_agent_manage.py#L38](app://-/index.html?hostId=local)。

**核心抽象**

- Agent 只是协议接口，定义 send/receive/generate_reply/thinking/act/verify，把“通信”“推理”“执行”“校验”拆成独立阶段，见 [agent.py#L16](app://-/index.html?hostId=local)。
- AgentContext、AgentGenerateContext、AgentMessage 是运行时数据载体，分别承载会话级配置、一次生成过程上下文、以及 agent 间传递的消息对象，见 [agent.py#L197](app://-/index.html?hostId=local) 和 [agent.py#L274](app://-/index.html?hostId=local)。
- Role 负责“人格与提示词”，ProfileConfig/Profile 负责“模板与配置”，也就是把“谁在说话”与“提示词长什么样”分开，便于动态换语言、换约束、换 prompt，见 [role.py#L34](app://-/index.html?hostId=local) 和 [base.py#L529](app://-/index.html?hostId=local)。
- ConversableAgent 是真正的运行时核心。它通过 bind() 统一注入 context/memory/resource/llm/profile/action/prompt，说明作者刻意做成了“装配式 agent”，而不是把依赖写死在构造函数里，见 [base_agent.py#L37](app://-/index.html?hostId=local) 和 [base_agent.py#L182](app://-/index.html?hostId=local)。

**执行流程**

- 主流程在 generate_reply()，它严格按 _init_reply_message -> _load_thinking_messages -> thinking -> review -> act -> verify -> write_memories 运行，本质上是一个可重试的 agent loop，见 [base_agent.py#L392](app://-/index.html?hostId=local)。
- thinking() 只负责调用 LLM，不直接执行动作，所以模型输出和执行逻辑是解耦的；模型失败时会换模型重试，见 [base_agent.py#L668](app://-/index.html?hostId=local)。
- act() 遍历 actions，让 Action 去解析 LLM 输出并真正执行，这层设计把“文本推理”转成“结构化动作”，见 [base_agent.py#L725](app://-/index.html?hostId=local) 和 [action/base.py#L90](app://-/index.html?hostId=local)。
- verify() 统一检查 review 结果、action 成功状态和内容完整性，所以失败重试不是由各个 agent 自己散落处理，而是集中在基类里，见 [base_agent.py#L777](app://-/index.html?hostId=local)。
- _load_thinking_messages() 会把 system prompt、历史记忆、依赖消息、资源提示、当前用户输入拼成最终送给 LLM 的消息列表，这是 prompt engineering 的真正入口，见 [base_agent.py#L1203](app://-/index.html?hostId=local)。

**动作、记忆、资源**

- Action 的设计重点是“定义输出 schema + 解析 LLM 文本 + 执行 run()”，因此每个 agent 的差异主要不在基类，而在绑定了什么 Action，见 [action/base.py#L40](app://-/index.html?hostId=local)。
- AgentMemory 是 agent 记忆总入口，内部再包一层底层 memory 和 GptsMemory，前者负责检索/遗忘，后者负责会话消息和计划持久化，见 [agent_memory.py#L276](app://-/index.html?hostId=local)。
- HybridMemory 明显是按“感知记忆 -> 短期记忆 -> 长期记忆”建模的，短期记忆支持增强和迁移，长期记忆走向量库，这部分是比较完整的认知架构设计，见 [hybrid.py#L31](app://-/index.html?hostId=local)。
- GptsMemory 保存计划和消息，还负责流式消息可视化输出，所以它不只是存储层，也是 agent 会话 UI 的中间层，见 [gpts_memory.py#L24](app://-/index.html?hostId=local)。
- Resource/ResourceManager 把数据库、知识库、工具、插件等都统一成资源类型，再由 build_resource() 按配置实例化，说明这个框架想把“工具调用”与“知识注入”统一成资源装配问题，见 [base.py#L89](app://-/index.html?hostId=local) 和 [manage.py#L76](app://-/index.html?hostId=local)。
- ResourcePack 是组合器，允许一个 agent 同时绑定多个资源，再统一生成 prompt 或路由执行，见 [pack.py#L21](app://-/index.html?hostId=local)。
- BaseTool/FunctionTool/@tool 这套封装说明工具本质上也是一种资源，只是多了参数 schema 和可执行函数包装，见 [tool/base.py#L64](app://-/index.html?hostId=local)。

**多 Agent 编排**

- AgentManager 用扫描注册的方式发现 expand 目录里的具体 agent，实现“框架定义协议，业务 agent 自动注册”，见 [agent_manage.py#L47](app://-/index.html?hostId=local)。
- expand 目录下的 agent 大多很薄，比如 SimpleAssistantAgent、ToolAssistantAgent 主要就是预置 profile 和 action，这说明作者希望新增 agent 的成本尽量低，见 [simple_assistant_agent.py#L16](app://-/index.html?hostId=local) 和 [tool_assistant_agent.py#L12](app://-/index.html?hostId=local)。
- PlannerAgent 专门生成计划，PlanAction 负责把计划落成结构化步骤并写入 plans_memory，见 [planner_agent.py#L14](app://-/index.html?hostId=local) 和 [plan_action.py#L38](app://-/index.html?hostId=local)。
- AutoPlanChatManager 是真正的 team manager。它读取待办 plan，选 speaker，处理依赖步骤结果，再驱动子 agent 执行，所以“计划生成”和“计划推进”被分成了两个角色，见 [team_auto_plan.py#L21](app://-/index.html?hostId=local)。
- AWEL 那条线是另一种编排模式，不靠 planner 动态调度，而是把 agent 放进 DAG 里按流程跑，适合固定流程应用，见 [team_awel_layout.py#L83](app://-/index.html?hostId=local) 和 [agent_operator.py#L137](app://-/index.html?hostId=local)。

**中间件与技能**

- MiddlewareAgent 在 ConversableAgent 外再包一层生命周期 hook，允许在 init、thinking、act、prompt 修改等阶段插入逻辑，见 [middleware/agent.py#L41](app://-/index.html?hostId=local)。
- SkillsMiddlewareV2 本质上是在生成回复前自动匹配 skill，并在 system prompt 前插入技能说明，所以它不是新执行引擎，而是 prompt augmentation 插件，见 [middleware_v2.py#L17](app://-/index.html?hostId=local)。

**服务层如何装配**

- 入口装配在 AppManager.user_chat_2_app()：先构造 AgentContext，再创建 app agent，再让 UserProxyAgent 发起对话，见 [app_agent_manage.py#L68](app://-/index.html?hostId=local)。
- create_agent_from_gpt_detail() 根据数据库里的 agent 定义，把 llm_config/resource/prompt/memory/context 绑定到具体 agent 类上，这就是业务配置转运行实例的关键桥梁，见 [app_agent_manage.py#L198](app://-/index.html?hostId=local)。
- create_agent_of_gpts_app() 根据 TeamMode 选择单 agent、自动规划 team 或 AWEL flow，所以应用层真正决定的是“编排模式”，不是底层 agent 实现，见 [app_agent_manage.py#L237](app://-/index.html?hostId=local)。
- MetaDbGptsPlansMemory 和 MetaDbGptsMessageMemory 把计划/消息持久化到数据库，说明 core 层是接口化的，serve 层再决定落地存储，见 [db_gpts_memory.py#L14](app://-/index.html?hostId=local)。