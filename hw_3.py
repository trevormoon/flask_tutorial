from flask import  Flask, render_template, request
import mysql.connector as MY
app = Flask( __name__ )

def insertDBFormat(name,age,birth):
    try:
        conn = MY.connect(host='127.0.0.1', user='root',passwd='1234'
                   ,database='world')
        cur = conn.cursor()
        sql = "insert into student values(%s,%s,%s)"
        cur.execute(sql, (name, age, birth))
        print( '반영된갯수', cur.rowcount)
        conn.commit()
        conn.close()
        return 'insert success'
    except Exception as err:
        return err

@app.route('/')
def root():
    return 'hello flask'

@app.route('/insertForm')
def insertForm():
    return render_template('insertForm.html')

@app.route('/insert')
def insert():
    name = request.args['myname']
    age = int( request.args['myage'] )
    birth = request.args['mybirth']
    result = insertDBFormat(name,age,birth)
    return f'<h1>{result}</h1>'

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=3500, debug=True)