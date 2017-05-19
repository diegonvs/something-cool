#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    lal = ""
    arq = open("data.txt","r")
    for x in arq:
        lal += x
    arq.close()    
    return lal

if __name__ == '__main__':
    app.run(debug=True)