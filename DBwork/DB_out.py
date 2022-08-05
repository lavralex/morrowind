from oracle_connection.connect import connection
connection1 = connection()
cursor = connection1.cursor()

rows = [ (10, "First1" ), (11, "Second2" ),
  ]

cursor.executemany("insert into mytab1(id, data) values (:1, :2)", rows)
#cursor.commit() 