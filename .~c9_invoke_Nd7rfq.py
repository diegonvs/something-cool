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

def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting)
import web
if __name__ == '__main__':
    app.run(debug=True)
    
import web

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()