from flask import Flask
##Wsgi application
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to flask sriram "
@app.route('/time')
def time():
    return "you just complete toturals in just 1 day"



if __name__=='__main__':
    app.run(debug=True)