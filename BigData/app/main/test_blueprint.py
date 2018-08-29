from flask import Blueprint

test1 = Blueprint('test1', __name__)
@test1.route('/')
def index():
    return 'test1'