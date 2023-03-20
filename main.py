from flask import Flask,render_template,jsonify
import mysql.connector
from database import mydb,get_info,load_job_from_db

app = Flask(__name__)

  
@app.route("/")
def hello_world():
    jobs=get_info()
    return render_template('home.html',Jobs=jobs,company="Gautam")
@app.route("/api/Jobs")
def li_JOBS():
  jobs=get_info()  
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job=load_job_from_db(id)
  if not job:
    return 'Not Found 404',404
  return render_template('jobpage.html',job=job)
  
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)# host is 0.0.0.0 for local host