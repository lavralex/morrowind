from oracle_connection.connect import connection
connection1 = connection()
cursor = connection1.cursor()

сharacters = []
cursor = connection1.cursor()
cursor.execute("""
        SELECT first_name, last_name
        FROM individual
        """,
        )
for fname, lname in cursor:
    сharacters.append(f'{fname} {lname} ')
print(сharacters)
