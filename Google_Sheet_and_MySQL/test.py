import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

json_path = './service_account.json' # Please set the file for using service account.

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
client = gspread.authorize(creds)

spreadsheetTitle = 'ZTX Data'
folderId = "1PTZZElnNqjPsFIbt8CdVDGZxRAMIhhEj" # Please set the folder ID of the folder in your Google Drive.

workbook = client.create(spreadsheetTitle, folder_id=folderId)

sa = gspread.service_account(filename="service_account.json")
sh = sa.open_by_key(workbook.id)
wks = sh.worksheet("Sheet1")
wks.batch_clear(["A2:ZZ"])

wks.update('A2', "result")