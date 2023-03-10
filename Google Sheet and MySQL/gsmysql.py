# Import libraries
import gspread
import mysql.connector
import mysqlcred as mc
from oauth2client.service_account import ServiceAccountCredentials

# Don't Execute This File.
# initialize variables for gspread
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account.json', scope)
client = gspread.authorize(creds)
# connection = ''


def GetSpreadsheetData(shetKey, worksheetName):
    sheet = client.open_by_key(shetKey).worksheet(worksheetName)
    return sheet.get_all_values()[1:]


def WriteToMySQLTable(paramhost, paramdatabase, paramuser, parampassword, sql_data, tableName, column_count):

    try:
        # connection = mysql.connector.connect(
        #     user=mc.user,
        #     password=mc.password,
        #     host=mc.host,
        #     database=mc.database
        # )
        connection = mysql.connector.connect(
            user=paramuser,
            password=parampassword,
            host=paramhost,
            database=paramdatabase
        )
        sql_truncate = "TRUNCATE TABLE {} ".format(tableName)

        # sql_insert_statement = """INSERT INTO {}
        #     VALUES (
        #          %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        #         ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        #         ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        #         ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        #         ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        #         ,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        #         ,%s
        #     )""".format(tableName)
        sql_columns = ''
        for i in range(1, column_count + 1):
            if i != 1:
                sql_columns += ','
            sql_columns += '%'
            sql_columns += 's'
        sql_insert_statement = """INSERT INTO """+tableName + \
            """ VALUES (""" + sql_columns + """)""".format(tableName)

        cursor = connection.cursor()
        cursor.execute(sql_truncate)
        # print('Table {} Trucated'.format(tableName))
        for i in sql_data:
            cursor.execute(sql_insert_statement, i)
        connection.commit()
        # print("Table {} successfully updated.".format(tableName))
    except mysql.connector.Error as error:
        connection.rollback()
        print("Error: {}. Table {} not updated!".format(error, tableName))
    finally:
        cursor.execute('SELECT COUNT(*) FROM {}'.format(tableName))
        rowCount = cursor.fetchone()[0]
        print(tableName, 'row count:', rowCount)
        if connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed.")


def PreserveNULLValues(listName):
    # print('Preserving NULL values…')
    for x in range(len(listName)):
        for y in range(len(listName[x])):
            if listName[x][y] == '':
                listName[x][y] = None
    # print('NULL values preserved.')


def Runner(paramhost, paramdatabase, paramuser, parampassword, SheetKey, SheetIndex, mysqlTable, column_count):
    data = GetSpreadsheetData(SheetKey, SheetIndex)
    PreserveNULLValues(data)
    WriteToMySQLTable(paramhost, paramdatabase, paramuser,
                      parampassword, data, mysqlTable, column_count)


def connectdb(paramhost, paramdatabase, paramuser, parampassword):
    global connection
    connection = mysql.connector.connect(
        user=paramuser,
        password=parampassword,
        host=paramhost,
        database=paramdatabase
    )
