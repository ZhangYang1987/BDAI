from datetime import datetime
# from app import app
from flask import render_template, session, redirect, url_for
from . import main

# from .forms import NameForm
from .. import db
# from ..models import User
# from . import main as main_blueprint

# app.register_blueprint(main_blueprint)



# app.register_blueprint(test1_blueprint, url_prefix='test1')

@main.route('/', methods=['GET', 'POST']) # 不同的蓝本装饰器不同
def index():
    return render_template('index.html')
    # return "hello World"
    # form = NameForm()
    # if form.validate_on_submit():
    #     return redirect(url_for('main.index')) # 每个蓝本都有一个命令空间，生成url需要加上命名空间前缀
    # return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False),
    #                        current_time=datetime.utcnow())

# @test1.route('/', methods=['GET', 'POST'])
# def index():
#     return "Hello World"