from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
## Response
def root():
    return "Welcome to Page type hw1"

@app.route("/hw1")
## Response
def obesidy():
    return render_template("hw1.html")

@app.route("/hwresult")
## Response
def obesidyresult():
    h=int(request.args["myheight"])
    w=int(request.args["myweight"])
    s_w=(h-100)*0.85
    ob=w/s_w*100
    ob_grade=str()
    loc=str()
    if ob<=90:
        ob_grade="저체중"
        loc="/static/images/weight/low.png"
    elif ob>90 and ob<=110:
        ob_grade="정상"
        loc="/static/images/weight/normal.png"
    elif ob>110 and ob<=120:
        ob_grade="과체중"
        loc="/static/images/weight/over.png"
    elif ob>120:
        ob_grade="비만"
        loc="/static/images/weight/obese.png"
    return render_template("hw1result.html",height=h,weight=w,grade=ob_grade,img_p=loc)


if __name__=="__main__":
    app.run(hot="0.0.0.0",port=5000,debug=True)