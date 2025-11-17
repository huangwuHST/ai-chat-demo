from flask import Flask, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 从models包导入统一的数据库实例和模型
from src.models import db, User

def create_app(config_name=None):
    """创建Flask应用实例"""
    app = Flask(__name__)
    
    # 简化CORS配置，让前端代理处理跨域问题
    CORS(app, origins=['http://localhost:3000'], supports_credentials=True)
    
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///ai_qa_system.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False  # 可以设置为True来调试SQL
    
    # 初始化数据库
    db.init_app(app)
    
    # 延迟导入以避免循环导入
    with app.app_context():
        # 导入模型以确保它们被注册
        from src.models.conversation import Conversation
        from src.models.message import Message
        
        # 注册蓝图
        from src.api.auth import auth_bp
        from src.api.conversation import conversation_bp
        from src.api.message import message_bp
        from src.api.chat import chat_bp  # 导入新的聊天蓝图
        app.register_blueprint(auth_bp, url_prefix='/api/auth')
        app.register_blueprint(conversation_bp, url_prefix='/api/conversations')
        app.register_blueprint(message_bp, url_prefix='/api/messages')
        app.register_blueprint(chat_bp, url_prefix='/api/chat')  # 注册聊天蓝图
    
    @app.route('/')
    def home():
        return {'message': 'AI问数对话系统后端服务'}
    
    @app.route('/health')
    def health_check():
        return {'status': 'healthy'}
    
    # 全局错误处理
    @app.errorhandler(Exception)
    def handle_exception(e):
        import traceback
        error_info = {
            'error': str(e),
            'type': e.__class__.__name__,
            'traceback': traceback.format_exc()
        }
        print(f"全局错误捕获: {error_info}")
        return jsonify(error_info), 500

    return app

def create_default_admin_user(app):
    """创建默认管理员用户"""
    with app.app_context():
        try:
            # 检查是否已存在admin用户
            admin_user = User.query.filter_by(username='admin').first()
            
            if not admin_user:
                # 创建bcrypt实例
                bcrypt = Bcrypt(app)
                
                # 创建默认admin用户，密码为admin123
                hashed_password = bcrypt.generate_password_hash('admin123').decode('utf-8')
                admin_user = User(
                    username='admin',
                    email='admin@example.com',
                    password=hashed_password,
                    is_active=True
                )
                db.session.add(admin_user)
                db.session.commit()
                print("默认管理员用户已创建: admin/admin123")
            else:
                print("管理员用户已存在")
        except Exception as e:
            print(f"创建默认管理员用户时出错: {e}")
            db.session.rollback()

if __name__ == '__main__':
    app = create_app()
    # 创建数据库表
    with app.app_context():
        db.create_all()
    
    # 创建默认管理员用户
    create_default_admin_user(app)
    
    app.run(host='localhost', port=5000, debug=True)