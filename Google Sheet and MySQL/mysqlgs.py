# Import Packages
import gspread
import mysql.connector
# import schedule
import time
import mysqlcred as mc
import json
# from gsmysql import Runner

# Execute This File Only


def main():
    # Runner()
    conn = mysql.connector.connect(
        user=mc.user,
        password=mc.password,
        host=mc.host,
        database=mc.database)

    cur = conn.cursor()
    cur.execute("""SELECT * FROM vwJob""")
    result = cur.fetchall()
    conn.commit()
    conn.close()

    sa = gspread.service_account(filename="service_account.json")
    sh = sa.open_by_key("1QOpaJuEMCNqAdvFeol6s6SZIdURn43P4AugwQxncmtY")
    wks = sh.worksheet("processed")

    wks.update('A2', result)


main()

# schedule.every(2).seconds.do(main)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
