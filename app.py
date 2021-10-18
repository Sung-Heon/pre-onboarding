from flask import Flask,jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from model import models

    # 블루프린트
    from views import post_views, auth_views
    app.register_blueprint(post_views.bp)
    app.register_blueprint(auth_views.bp)

    #jwt
    jwt = JWTManager(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify(msg="없는 페이지 입니다. 아마 존재하지 않는 게시글 id로 요청을 보내셨을 가능성이 높습니다.", status_code=404)
    return app


app = create_app()

if __name__ == '__main__':
    app.run()
