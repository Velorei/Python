from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/yolochka')
def yolochka():
    return 'Yolochka!!!!!!'

@app.route('/') #дикоратор
def first():  #свойстава дикоратора
    logging.info('User request to /')
    return 'Hello!'
