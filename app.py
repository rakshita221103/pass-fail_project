from flask import *
import pandas as pd
from sklearn.linear_model import LinearRegression

app=Flask(__name__)
####################################
url ="https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/student-pass-fail-data.csv"
df = pd.read_csv(url)

X = df.iloc[:, :2].values
Y = df.iloc[:, 2].values

model = LinearRegression( )
model.fit(X, Y)
res = model.predict([[ 5,25]])
op= (str( round(res[0]*100 ,2)) + "%")
###################################

@app.route('/')
def hello_world():
  return render_template("index.html")
  # return 'HELLO AIML FOR PYTHON WEB DEVELOPMENT !!' + op  

@app.route('/project')
def project  ():
  return render_template("form.html") 
 
@app.route('/predict' , methods=['POST'])
def predict  ():
  dhrs=int(request.form['dhrs'])
  mhrs=int(request.form['mhrs'])
  op=str(dhrs)+str(mhrs)
  res = model.predict([[ dhrs,mhrs]])
  op="Predicted Result :"+(str( round(res[0]*100 ,2)) + "%")
  return render_template("form.html",result=op) 

@app.route('/home')
def home():
  return render_template("index.html")

if __name__=='__main__':
  app.run()    