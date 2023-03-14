from flask import Flask,render_template,jsonify

app = Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'backend enginner',
    'location':'san franchsico,usa',
    'salary': 'rs 12,00,000'
},
     
{
    'id':2,
    'title':'forntend enginner',
    'location':'new york,usa',
    'salary': 'rs 22,00,000'},
{
    'id':3,
    'title':'data  enginner',
    'location':'new york,uk',
    'salary':'rs200000'
     },

  {
    'id':4,
    'title':'data scientist',
    'location':'new jersey,usa',
    'salary': 'rs 20,00,000'},


]
@app.route("/")
def hello_world():
    return render_template('home.html',Jobs=JOBS,company="jovan")
@app.route("/,json")
def JOBS():
    return Jobs

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)# host is 0.0.0.0 for local host