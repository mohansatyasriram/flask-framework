from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to flask sriram "
@app.route('/detail/<name>') #by default it was string
def detail(name):
    return "your name "+ name

@app.route('/success/<int:score>') 
def success(score):
    return "your pass mark was "+ str(score)

@app.route('/fail/<int:score>') 
def fail(score):
    return "your fail mark was "+ str(score)

@app.route('/result/<int:score>') 
def result(score):
    if score <50:
        result ='fail'
    else:
        result='success'
    return result   
#for the resultpage to import redirect,url_for     
@app.route('/resultpage/<int:marks>') 
def resultpage(marks):
    if marks <50:
        result ='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))
  

if __name__=='__main__':
    app.run(debug=True)