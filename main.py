from flask import Flask
from flask.templating import render_template


app=Flask(__name__) 

tasklist=[["Walk Dog",True],["Wash Dishes",False],["Take Out Trash",True]]
@app.route('/')
def home():
     return render_template("tasklist.html",TaskList=tasklist)
     
if __name__=='__main__':
   app.run(debug=True,port=2000)

