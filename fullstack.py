# Integrate html with flask
# http verb post and get
from flask import Flask,redirect,url_for,render_template,request
 
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('fullstack.html')




@app.route('/page/<float:score>')
def page(score):
    grade=''
    if(score>50):
        grade='passs'
        return render_template('show_integratehtml.html',result=score,status=grade)
    else:
        grade='fail'
        return render_template('show_integratehtml.html',result=score,status=grade)




#result checker by submit html file
@app.route('/submit',methods=['POST','GET'])
def submit():
   total_score=0
   if request.method=='POST':
      science=float(request.form['science'])
      math=float(request.form['maths'])
      stat=float(request.form['stat'])
      logic=float(request.form['logic'])
      total_score=(science+math+stat+logic)/4
   return redirect(url_for('page',score=total_score))

    

if __name__ =='__main__':
    app.run(debug=True)