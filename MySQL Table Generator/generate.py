import pandas as pd


def Create(table_design_excel, table_name):
    df = pd.read_excel(table_design_excel , sheet_name='' + table_name + '')
    SQLScript = 'CREATE TABLE ' + table_name + '('

    for index, row in df.iterrows():
        SQLScript += '''
                '''
        SQLScript += ", " if index != 0 else ""
        SQLScript += row["internalcolumn"] + ' '
        SQLScript += row["mysqldatatype"] + ' '
        SQLScript += "" if row["mysqldatatype"] != "VARCHAR" else (
            "(" + str(int(row["mysqllength"])) + ") ")
        SQLScript += "NULL" if row["nullability"] == "Yes" else "NOT NULL"
        # SQLScript += "," if df.count() == index else ""
        # print(df.count())
        # print(index)
    SQLScript += '''
    '''
    SQLScript += ');'

    with open('output/' + table_name + '.sql', 'w') as f:
        f.write(SQLScript)


# Create()
