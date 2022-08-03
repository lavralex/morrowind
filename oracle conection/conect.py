import cx_Oracle


cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\User\Desktop\instantclient_21_6")
# Connect as user "hr" with password "welcome" to the "orclpdb1" service running on this computer.
connection = cx_Oracle.connect(user="c##test", password="MyPass",
                               dsn="localhost:1521")

cursor = connection.cursor()
cursor.execute("""
        SELECT first_name, last_name
        FROM individual
        """,
        )
for fname, lname in cursor:
    print("Values:", fname, lname)
    #
    # #WHERE department_id = :did AND employee_id > :eid
    # did = 50,
    # eid = 190   localhost/orclpdb1