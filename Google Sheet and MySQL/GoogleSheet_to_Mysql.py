# Import libraries
import gspread
import mysql.connector
import MySQLCredentials as mc
from oauth2client.service_account import ServiceAccountCredentials

# Don't Execute This File.
# initialize variables for gspread
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account.json', scope)
client = gspread.authorize(creds)


def GetSpreadsheetData(sheetName, worksheetIndex):
    sheet = client.open(sheetName).get_worksheet(worksheetIndex)
    return sheet.get_all_values()[1:]


def WriteToMySQLTable(sql_data, tableName):

    try:
        connection = mysql.connector.connect(
            user=mc.user,
            password=mc.password,
            host=mc.host,
            database=mc.database
        )
        sql_drop = " DROP TABLE IF EXISTS {} ".format(tableName)
        sql_create_table = """CREATE TABLE {}( 
           Rollno int,
           Name varchar(50),
           Percentage float,
           Branch varchar(10),
           PRIMARY KEY (Rollno)
            )""".format(tableName)

        sql_insert_statement = """INSERT INTO {}( 
            Rollno,
            Name,
            Percentage,
            Branch )
            VALUES ( %s,%s,%s,%s )""".format(tableName)
        cursor = connection.cursor()
        cursor.execute(sql_drop)
        print('Table {} has been dropped'.format(tableName))
        cursor.execute(sql_create_table)
        print('Table {} has been created'.format(tableName))
        for i in sql_data:
            cursor.execute(sql_insert_statement, i)
        connection.commit()
        print("Table {} successfully updated.".format(tableName))
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
            print("MySQL connection is closed.")


def PreserveNULLValues(listName):
    print('Preserving NULL values…')
    for x in range(len(listName)):
        for y in range(len(listName[x])):
            if listName[x][y] == '':
                listName[x][y] = None
    print('NULL values preserved.')


def Runner():
    data = GetSpreadsheetData('Google Sheet Pull to MySql', 0)
    PreserveNULLValues(data)
    WriteToMySQLTable(data, 'MyData')


# EXECUTER:
Runner()
