import mysql.connector,os

mydb = os.environ['mydb']
def get_info():
 cursor = mydb.cursor(dictionary=True)
 sql = "SELECT * FROM jobs"
 cursor.execute(sql)
 rows = cursor.fetchall()
 jobs=[]
 for row in rows:
   jobs.append(dict(row))
 return jobs