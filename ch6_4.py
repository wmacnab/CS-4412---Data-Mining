# Integrating MySQL with Python using PyMySQL

# The connection/cursor model is commonly used in database programming
# A cursor keeps track of certain state information
# A cursor also contains the results of the latest query it has executed
# You can access this information by calling cur.fetchone()

import pymysql

#conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
conn = pymysql.connect(host='localhost', user='root', password='password', database='db', cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
#cur.execute('CREATE TABLE scraping (title Char(50) NULL,body Char(255) NULL,url Char(255) NULL);')
cur.execute('USE db')
cur.execute('DROP TABLE scraping')
#cur.execute('USE db')
#cur.execute('SELECT * from SCRAPING')
print(cur.fetchone())
cur.close()
conn.close()
