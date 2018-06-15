import time
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success/<name>,<comment>')
def success(name, comment):
	with open("log.txt", "a") as logfile:
		logfile.write(str(time.time())+", "+name+", "+comment+"\r\n")
	return "<p>Hello, "+name+", you are visitor: "+str(time.time())+" Your comments have been logged.</p>"

@app.route('/sign', methods=['POST'])
def sign():
	if request.method == 'POST':
		input_n = request.form['n']
		input_c = request.form['c']
		return redirect(url_for('.success',name=input_n,comment=input_c))
	else:
		input = request.args.get('n')
		return redirect(url_for('.success',name=input))

if __name__ == '__main__':
	app.run(debug=True)
