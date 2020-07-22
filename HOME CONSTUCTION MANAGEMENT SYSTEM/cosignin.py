from flask import Flask, redirect, url_for, request 
app = Flask(__name__)  
@app.route('/success/<id>') 
def success(name,id,psw,pno): 
    f=open('contractor.txt','w')
    f.write(name+'||'+id+'||'+psw+'||'+pno)
	return 'sucessfull registered %s' %name 
    f.close()
@app.route('/cosignup',methods = ['POST', 'GET']) 
def login(): 
	if request.method == 'POST': 
		id = request.form['id'] 
		user = request.form['uname'] 
		psw = request.form['psw']
		pno = request.form['pno']
		return redirect(url_for('success',id=id,name=user,psw=psw,pno=cno)) 
	else: 
		return redirect(url_for('error'))  
if __name__ == '__main__': 
	app.run(debug = True) 
