from flask import Blueprint

from libs.redprint import RedPrint

api = RedPrint('book')


@api.route('/get')
def get_book():
    return 'i am book'
