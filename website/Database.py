import sqlite3

db = sqlite3.connect('register')

rs = db.cursor()

#rs.execute('''create table register(username varchar(50), student_id varchar(10), email varchar(100), password varchar(15))''')
#db.commit()

rs.execute(''' insert into register values('Mansi', '@mail.csuchico.edu', 'mdogra1')''')
db.commit()
rs.execute('select * from register')
for i in rs:
	print(i) 