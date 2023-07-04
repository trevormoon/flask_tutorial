from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
## Response
def root():
    return "Welcome to Page type hw1"

@app.route("/hw2")
## Response
def order():
    return render_template("hw2.html")


if __name__=="__main__":
    app.run(hot="0.0.0.0",port=5000,debug=True)