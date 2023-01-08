# Import Packages
import gspread
import mysql.connector
import schedule
import time
import MySQLCredentials as mc
from GoogleSheet_to_Mysql import Runner

# Execute This File Only


def main():
    Runner()
    conn = mysql.connector.connect(
        user=mc.user,
        password=mc.password,
        host=mc.host,
        database=mc.database)
    cur = conn.cursor()
    cur.execute("""SELECT * FROM mydata""")
    result = cur.fetchall()
    conn.commit()
    conn.close()

    sa = gspread.service_account(filename="service_account.json")
    sh =   .open("Google Sheet Pull to MySql")
    wks = sh.worksheet("Sheet2")

    wks.update('A2', result)


schedule.every(2).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
