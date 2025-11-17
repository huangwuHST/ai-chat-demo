# AI问数对话系统 (AI Question Answering Dialogue System)

本项目是一个基于人工智能的问答对话系统，允许用户通过自然语言与系统进行交互，获取相关数据和信息。

## 项目结构

```
.
├── backend                 # 后端服务
│   ├── src                 # 源代码目录
│   │   ├── api             # API接口
│   │   ├── models          # 数据模型
│   │   └── ...
│   ├── app.py              # Flask应用入口
│   └── requirements.txt    # Python依赖
├── frontend                # 前端界面
│   ├── src                 # Vue源代码
│   │   ├── pages           # 页面组件
│   │   ├── services        # API服务
│   │   └── ...
│   ├── package.json        # Node.js依赖
│   └── ...
└── 文档                    # 相关文档
```

## 技术栈

### 后端
- Python Flask
- SQLAlchemy (数据库ORM)
- SQLite (默认数据库)
- Flask-CORS (跨域支持)
- Flask-Bcrypt (密码加密)

### 前端
- Vue 3
- Vue Router
- Axios (HTTP客户端)
- Vite (构建工具)

## 快速开始

### 后端启动

1. 安装依赖：
```bash
cd backend
pip install -r requirements.txt
```

2. 运行应用：
```bash
python app.py
```

后端服务将在 `http://localhost:5000` 上运行。

### 前端启动

1. 安装依赖：
```bash
cd frontend
npm install
```

2. 运行开发服务器：
```bash
npm run dev
```

前端将在 `http://localhost:3000` 上运行。

## 默认管理员账户

- 用户名：admin
- 密码：admin123

## API 接口

主要的 API 接口包括：
- `/api/auth` - 认证相关接口
- `/api/conversations` - 对话管理接口
- `/api/messages` - 消息管理接口
- `/api/chat` - 聊天接口

## 开发文档

详细的设计和开发文档可以在项目的文档目录中找到。