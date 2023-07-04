from flask import Flask, render_template
import sys

app=Flask(__name__)


## Request
@app.route("/")
## Response
def root():
    return "hello flask"

## Request
@app.route("/aa")
## Response
def root2():
    return "hello flask2"

## Request
@app.route("/bb")
## Response
def root3():
    return render_template("test.html")

## Request
@app.route("/div")
## Response
def root4():
    return render_template("test2.html")

## Request
@app.route("/list")
## Response
def root5():
    return render_template("test3.html")

## Request
@app.route("/table")
## Response
def root6():
    return render_template("test4.html")

## Request
@app.route("/image")
## Response
def root7():
    return render_template("test5.html")


## Request
@app.route("/move")
## Response
def root8():
    return render_template("test6.html")

if __name__=="__main__":
    app.run(hot="0.0.0.0",port=5000,debug=True)