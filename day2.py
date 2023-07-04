from flask import  Flask, render_template, request

app = Flask( __name__ )

@app.route('/')
def root():
    return 'hello flask'

@app.route('/case')
def if_test():
    return render_template("case.html",num=123)

@app.route('/for')
def for_test():
    return render_template("for.html",my_list=['사과','딸기','포도','수박'])

@app.route('/table')
def table_test():
    d=[{"name":"문필욱","age":30},{"name":"최규호","age":38},{"name":"김지훈","age":28}]
    return render_template("table.html",data=d)

@app.route('/grid')
def grid_test():
    return render_template("grid.html")

@app.route('/filter')
def filter_test():
    return render_template("filter.html", n=-10, pi=3.141592, s="abc", s1="      abc        ",s2="absedadsf")

@app.template_filter('customfilter')
def customfilter1(s):
    return s[::2]

@app.route('/block')
def block_test():
    return render_template("block.html")

@app.route('/phil')
def phil_test():
    return render_template("phil.html")
@app.route('/manila')
def manila_test():
    return render_template("manila.html")
@app.route('/indonesia')
def indonesia_test():
    return render_template("indonesia.html")

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=3500, debug=True)