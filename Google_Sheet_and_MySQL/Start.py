
# Python program to read
# json file
import gsmysql as gsm
import mysqlgs as mgs
import json
  
# Opening JSON file
f = open('Config.json')

# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Load Data from Google Sheet to Database
for i in data:        
        # gsm.connectdb(i["dbcred"]["host"],i["dbcred"]["database"],i["dbcred"]["user"],i["dbcred"]["password"])
        for j in i["gstodb"]:
                sheetid = j["sheetid"]
                for k in j["gstabs"]:
                        gstab = k["gstab"]
                        dbtab = k["dbtab"]
                        columncount = k["columncount"]
                        gsm.Runner(i["dbcred"]["host"],i["dbcred"]["database"],i["dbcred"]["user"],i["dbcred"]["password"],
                                   sheetid, gstab, dbtab, columncount)


# Load Data from Database to Google Sheet
for i2 in data:        
        # gsm.connectdb(i["dbcred"]["host"],i["dbcred"]["database"],i["dbcred"]["user"],i["dbcred"]["password"])
        for j2 in i2["dbtogs"]:
                sheetid = j2["sheetid"]
                for k2 in j2["gstabs"]:
                        gstab = k2["gstab"]
                        dbtab = k2["dbtab"]                        
                        mgs.Runner(i2["dbcred"]["host"],i2["dbcred"]["database"],i2["dbcred"]["user"],i2["dbcred"]["password"],
                                   sheetid, gstab, dbtab)
                        




# Closing file
f.close()