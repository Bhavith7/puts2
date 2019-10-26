from flask import Flask, request
from fractions import Fraction 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


@app.route('/add')
def addition():
    value1=request.args.get('A',default = 0, type = Fraction)
    value2=request.args.get('B',default = 0, type = Fraction)
    C=value1+value2
    result=float(C) 
    return " %s \n" %result
   


if __name__ == "__main__":
    app.run()
