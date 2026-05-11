from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() :
	return "Hello EPSIC 158 ! - Modifie automatiquement par Jenkins via le webhook GitHub !"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
