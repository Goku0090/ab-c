from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'hello world'
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)# host is 0.0.0.0 for local host