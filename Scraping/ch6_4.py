# Integrating MySQL with Python using PyMySQL

# The connection/cursor model is commonly used in database programming
# A cursor keeps track of certain state information
# A cursor also contains the results of the latest query it has executed
# You can access this information by calling cur.fetchone()

import pymysql

# Creating connection
conn = pymysql.connect(host='localhost', user='root', password='password', database='db', autocommit=True)#, cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

# DBMS interaction with SQL
cur.execute('USE db')

#cur.execute('DROP TABLE pages')
#cur.execute('CREATE TABLE pages (id bigint(7) NOT NULL AUTO_INCREMENT, title varchar(55) NULL,body varchar(1023) NULL,url varchar(255) NULL, PRIMARY KEY(id));')

#cur.execute('ALTER TABLE pages ADD MyColumn Char(5) NULL')
cur.execute('INSERT INTO pages (title, url, body) VALUES (\'First\', \'second\', \'third\');')
#cur.execute('DROP TABLE scraping')
#cur.execute('SELECT * from SCRAPING')
cur.execute('SELECT * FROM pages')

# Results and cleanup
print(cur.fetchone())
#conn.commit()
cur.close()
conn.close()
