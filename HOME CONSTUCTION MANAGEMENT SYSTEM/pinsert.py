from flask import Flask, redirect, url_for, request 
app = Flask(__name__)  
@app.route('/success/<name>') 
def success(name,pid,wrk): 
    f=open('pinsert.txt','w')
    f.write(name+'||'+pid+'||'+wrk+'||')
	return 'sucessfull registered %s' % name 
    f.close()
@app.route('/pinsert',methods = ['POST', 'GET']) 
def login(): 
	if request.method == 'POST': 
	    pid = request.form['pid'] 
	    pname = request.form['pname']
        wrk = request.form['wrk']
		return redirect(url_for('success' pid=pid,name=pname,wrk=wrk)) 
	else: 
		return redirect(url_for('error'))  
if __name__ == '__main__': 
	app.run(debug = True) 
