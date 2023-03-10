# Import Packages
import gspread
import mysql.connector
# import schedule
import time
import mysqlcred as mc
import json
# from gsmysql import Runner

# Execute This File Only


def main(paramhost, paramdatabase, paramuser, parampassword, sheetkey, sheettabname, sqlobj):
    # Runner()
    conn = mysql.connector.connect(
        user=paramuser,
        password=parampassword,
        host=paramhost,
        database=paramdatabase)

    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM {sqlobj}""")
    result = cur.fetchall()
    conn.commit()
    conn.close()

    sa = gspread.service_account(filename="service_account.json")
    sh = sa.open_by_key(sheetkey)
    wks = sh.worksheet(sheettabname)
    wks.batch_clear(["A2:ZZ"])

    wks.update('A2', result)


def Runner(paramhost, paramdatabase, paramuser, parampassword, sheetkey, sheettabname, sqlobj):
    main(paramhost, paramdatabase, paramuser,
         parampassword, sheetkey, sheettabname, sqlobj)

# schedule.every(2).seconds.do(main)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
