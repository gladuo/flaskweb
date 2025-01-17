# coding=utf-8
# Created by Meteorix at 2019/4/10
from flaskweb.app import create_app, gevent_run, db, api, admin, ModelView
from flaskweb.config import DebugConfig
import models
import views
import os

basedir = os.path.dirname(os.path.abspath(__file__))


class MyConfig(DebugConfig):
    # override default Configs
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    LOGGING_FILE = os.path.join(basedir, "logs", "app.log")
    UPLOAD_DIR = os.path.join(basedir, "uploads")


app = create_app(MyConfig)
app.register_blueprint(views.bp)
# api
api.add_namespace(views.api)
# admin
admin.add_view(ModelView(models.Todo, db.session))
admin.add_view(ModelView(models.TodoItem, db.session))


if __name__ == "__main__":
    # for debug only
    gevent_run(app, "0.0.0.0", 5000)
