import psycopg2

conn = psycopg2.connect(database="dbtest", user="postgres",
                        password="root", host="127.0.0.1", port="5432")
print('Opened database successfully')


cur = conn.cursor()

cur.execute("SELECT a from customers")
rows = cur.fetchall()
for row in rows:
    print("ID = "), row[1]
