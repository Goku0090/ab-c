from flask import Flask,render_template,jsonify
import mysql.connector
from database import mydb,get_info

app = Flask(__name__)

  
@app.route("/")
def hello_world():
    jobs=get_info()
    return render_template('home.html',Jobs=jobs,company="Gautam")
@app.route("/api/Jobs")
def li_JOBS():
  jobs=get_info()  
  return jsonify(jobs)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)# host is 0.0.0.0 for local host