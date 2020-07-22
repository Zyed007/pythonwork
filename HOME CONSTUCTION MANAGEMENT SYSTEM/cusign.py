from flask import Flask, redirect, url_for, request 
app = Flask(__name__)  
@app.route('/success/<id>') 
def success(name,id,fname,psw,pno): 
    f=open('customer.txt','w')
    f.write(name+'||'+id+'||'+fname+'||'+psw+'||'+pno)
	return 'sucessfull registered %s' % name 
    f.close()
@app.route('/cusignup',methods = ['POST', 'GET']) 
def login(): 
	if request.method == 'POST': 
		id = request.form['id'] 
		user = request.form['uname']
        fname = request.form['fname']
		psw = request.form['psw']
		pno = request.form['cno'] 
		return redirect(url_for('success',id=id,name=user,fname=fname,psw=psw,pno=cno)) 
	else: 
		return redirect(url_for('error'))  
if __name__ == '__main__': 
	app.run(debug = True) 
