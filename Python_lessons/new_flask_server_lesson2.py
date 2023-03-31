from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/yolochka')
def yolochka():
    return 'Yolochka!!!!!!'

@app.route('/') #дикоратор
def first():  #свойстава дикоратора
    logging.info('User request to /')
    return 'Hello!'

# @app.route('/user_info', methods=['GET'])
# def user_info():
#
#     name = 'Alexey'
#     age = str(34)
#
#     user_list = [name, age]
#
#     resp = 'name=' + user_list[0] + ' age =' + user_list[1]
#
#
#     return jsonify(user_list)

#-------перелавать параметры
@app.route('/user_info', methods=['GET', 'POST', 'DELETE'])
def user_info():

    if request.method == 'GET':
        name = 'Alexey'
        age = str(34)

        user_name = request.args.get('name')
        user_age = request.args.get('age')

        print('user_name = ', user_age)

        user_list = [user_name, user_age]

        resp = 'name=' + user_list[0] + ' age =' + user_list[1]

        return jsonify(user_list)

    elif request.method == 'POST':

        salary = int(request.json['salary'])  #-отправить json
        name = request.json['name']
        age = request.json['age']

        annualy = str(salary * 12)

        # -вернуть json
        resp_json = {'name': name,
                     'age': age,
                     'annualy': annualy}

        return jsonify(resp_json)

        resp_str = 'Annualy salary = ' + annuary

        return resp_str

    elif request.method == 'DELETE':
        salary = int(request.form.get('salary'))

        annualy = str(salary * 24)

        resp_str = '2 years salary = ' + annuary

        return resp_str
