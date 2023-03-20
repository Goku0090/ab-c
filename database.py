import mysql.connector,os

mydb=mysql.connector.connect(user='yt1faamh8wtp1mtq76ab', password='pscale_pw_B5VntAeZFkPKSfVsJvj7oFoZMWlnDBkPLR29mtnMgZQ',
                              host='us-east.connect.psdb.cloud',
                              database='gautamnair')
def get_info():
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT * FROM  jobs")
  result = mycursor.fetchall()
    
    # Convert the result to a list of dictionaries
  data = []
  for row in result:
        data.append(dict(row))
    
    # Use the data in your website as needed
  return data
def load_job_from_db(id):
  mycursor = mydb.cursor(dictionary=True)
  mycursor.execute("SELECT * FROM  jobs where id={};".format(id))
  result = mycursor.fetchall()
  if len(result)==0:
    return None
  else:
    return dict(result[0])