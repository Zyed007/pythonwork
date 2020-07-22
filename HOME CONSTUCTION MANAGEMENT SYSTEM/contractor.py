import os
from flask import Flask, redirect, url_for, request 
app = Flask(__name__) 

@app.route('/success/<name>') 
def success(name): 
	return Flask.redirect("test/pinsert.html")

@app.route('/contractor',methods = ['POST', 'GET']) 
def login(): 
	if request.method == 'POST': 
		user = request.form['uname'] 
		return redirect(url_for('success',name = user)) 
	else:  
		return redirect(url_for('error')) 
if __name__ == '__main__': 
	app.run(debug = True) 
