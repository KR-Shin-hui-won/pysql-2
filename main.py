from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

user = 'default'
db = pymysql.connect(host='database-2.cq6pri6dgw7y.ap-northeast-1.rds.amazonaws.com', port=3306, user='admin', password='password', db='AWS_MYSQL', charset='utf8')
curs = db.cursor()

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.j2')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.j2')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        sql = f'select * from sqli_2 where id="{username}" and passwd="{password}";'
        curs.execute(sql)
        res = curs.fetchone()
        if res:
            user = res[0]
            if user == 'admin':
                return f'<script>alert("you are win! flag is sqli(He11o W0r1d)");history.go(-1);</script>'
            else:
                return f'<script>alert("hello {username}");history.go(-1);</script>'
        else:
            return '<script>alert("wrong!");history.go(-1);</script>'

@app.errorhandler(404)
def page404(error):
    return render_template('page404.j2')

if __name__ == '__main__':
    app.run(port=3410)

