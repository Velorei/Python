from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(dbname='qa_ddl_24_140', user='user_24_140', password='123', host='159.69.151.133', port='5056')
cursor = conn.cursor()

@app.route('/yolochka')
def yolochka():
    return 'Yolochka!!!!!!'

@app.route('/db_save', methods=['GET', 'POST'])
def db_save():

    user_name = request.args.get('name')
    city = request.args.get('city')

    cursor = conn.cursor()


    if conn:
        print('CONN ======')

        base_data = (user_name, city)

        p_query = """INSERT INTO public.Person (person_name, city_id) VALUES (%s, %s)"""
        #qq = 'Insert into public.salary (person_name, city_id)) values(' + str(monthly_salary) +
        cursor.execute(p_query, base_data)

        conn.commit()

        cursor.close()

        return 'User saved'

    else:
        return  "User doesn't save"

@app.route('/users_cities')
def users_cities():

    result = {}

    cursor = conn.cursor()


    if conn:

        sl = cursor.execute("select * from public.Person;")
        sll = cursor.fetchall()

        #print(sll)

        for i in sll:
            result [str(i[0])] = {'User': i[1], "City": i[2]}

            #print(i[0], i[1])

        cursor.close()

        return jsonify(result)
    else:
        return 'Connection error'

    return jsonify(result)

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
