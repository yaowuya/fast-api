from flask import Blueprint

from libs.redprint import RedPrint

api = RedPrint('user')


@api.route('/get')
def get_user():
    return 'i am ruifeng'
