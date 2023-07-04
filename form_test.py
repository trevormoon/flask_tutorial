from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
## Response
def root():
    return "Welcome to Page Type form"

@app.route("/form")
## Response
def form():
    return render_template("form.html")

@app.route("/formresult")
def form_result():
    print(request.args) #Query string data
    name=request.args['myname']
    age=request.args['myage']
    color=request.args["mycolor"]
    hobby=request.args.getlist("myhobby")
    return f"<h1>{color}님이 접속하셨습니다 취미:{ '-'.join(hobby)}</h1>"

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/quizresult")
def quiz_result():
    print(request.args) #Query string data
    n1=request.args['num1']
    n2=request.args['num2']
    n3=int(n1)+int(n2)
    return f"<h1>합 : {n3}</h1>"

@app.route("/jinja_test")
def test_jinja():
    return render_template("jinja_test.html")

@app.route("/jinja_test_result")
def test_jinja_result():
    print(request.args) #Query string data
    m_name=request.args["myname"]
    m_age=request.args["myage"]
    return render_template("jinja_test_result.html",name=m_name,age=m_age)

@app.route("/jinja_test2")
def test_jinja_result2():
    return render_template("jinja_test_result2.html",test1="123",test2="1231245")


if __name__=="__main__":
    app.run(hot="0.0.0.0",port=5000,debug=True)