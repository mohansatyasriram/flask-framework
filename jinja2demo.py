##jinja2 template
'''
jinja2 template engines
{% --- %} used by conditional loop statements
{{ --- }}  used by expressions to print output
{{# --- #}} used this for comments
'''
from flask import Flask,redirect,url_for,render_template,request
 
app=Flask(__name__)


@app.route('/')
def welcome():
    return render_template('integratehtml.html')


@app.route('/page/<float:score>')
def page(score):
    
  return render_template('jinja2demo.html',result=score)
  '''
  res=""
  if score>=50:
   res='pass'
  else:
   res='fail'
  exp={'score':score,'res':res}
  return render_template('jinja2demo.html',result=exp)  
  #through this we pass the statements as the form of dictnayry
  this can handle by the for html formate { % for %}
  '''


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