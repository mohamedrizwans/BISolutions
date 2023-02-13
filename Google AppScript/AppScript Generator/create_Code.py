import pandas as pd

df = pd.read_excel(r'TableDesign.xlsx', sheet_name="Sheet1")

var_spreadsheetId = '1uKQl-a0Hk-zJA_Z4hb8lWW08dD4XLyB17cuInm7oieA'
var_sheetName = 'Sheet1'
var_dataRage = var_sheetName + '!A2:BG'
var_idRange = var_sheetName + '!A2:A'
var_lastCol = 'BG'
var_insertRange = var_sheetName + '!A1:BG1'
var_sheetID = '0'


# df = df.reset_index()  # make sure indexes pair with number of rows
# print(df["sno"].count())


def Create():
    Content = '''
      function doGet(request) {
     const userEmail = Session.getActiveUser().getEmail();
     const isValidUser = validate(userEmail, globalVariables().spreadsheetId);
     let htmlFile = (isValidUser)? 'index' : 'noaccess';

     var htmlOutput = HtmlService.createTemplateFromFile(htmlFile);
     htmlOutput.email = userEmail;

  //return HtmlService.createTemplateFromFile('index').evaluate()
  return htmlOutput.evaluate()
      .addMetaTag('viewport','width=device-width , initial-scale=1')
      .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
}


function validate(email, fileID){
  var file;
  try{
   file = DriveApp.getFileById(fileID);
   return true;
  }catch(e){
    return false; // If user has no access.
  }
}

function globalVariables(){ 
  var varArray = {
    spreadsheetId   : "''' + var_spreadsheetId + '''",
    dataRage        : "''' + var_dataRage + '''",
    idRange         : "''' + var_idRange + '''",  
    lastCol         : "''' + var_lastCol + '''",
    insertRange     : "''' + var_insertRange + '''",
    sheetID         : "''' + var_sheetID + '''"
  };
  return varArray;
}

function processForm(formObject){  
  if(formObject.RecId && checkID(formObject.RecId)){
    updateData(getFormValues(formObject),globalVariables().spreadsheetId,getRangeByID(formObject.RecId));
  }else{ 
    appendData(getFormValues(formObject),globalVariables().spreadsheetId,globalVariables().insertRange); 
  }
  return getLastTenRows();
}

function getFormValues(formObject){
  if(formObject.RecId && checkID(formObject.RecId)){
    var values = [[
    '''

    for index, row in df.iterrows():
        if index > 0:
            Content += ','
        Content += 'formObject.' + row["internalcolumn"]

    Content += '''
            ]];
        }else{
            var values = [[new Date().getTime().toString(),
        '''

    for index, row in df.iterrows():
        if index == 0:
            continue
        if index > 1:
            Content += ','
        Content += 'formObject.' + row["internalcolumn"]

    Content += '''
            ]];
        }
        return values;
        }

        function appendData(values, spreadsheetId,range){
        var valueRange = Sheets.newRowData();
        valueRange.values = values;
        var appendRequest = Sheets.newAppendCellsRequest();
        appendRequest.sheetID = spreadsheetId;
        appendRequest.rows = valueRange;
        var results = Sheets.Spreadsheets.Values.append(valueRange, spreadsheetId, range,{valueInputOption: "RAW"});
        }

        function readData(spreadsheetId,range){
        var result = Sheets.Spreadsheets.Values.get(spreadsheetId, range);
        return result.values;
        }

        function updateData(values,spreadsheetId,range){
        var valueRange = Sheets.newValueRange();
        valueRange.values = values;
        var result = Sheets.Spreadsheets.Values.update(valueRange, spreadsheetId, range, {
        valueInputOption: "RAW"});
        }

        function deleteData(ID){ 
        var startIndex = getRowIndexByID(ID);
        
        var deleteRange = {
                            "sheetId"     : globalVariables().sheetID,
                            "dimension"   : "ROWS",
                            "startIndex"  : startIndex,
                            "endIndex"    : startIndex+1
                            }
        
        var deleteRequest= [{"deleteDimension":{"range":deleteRange}}];
        Sheets.Spreadsheets.batchUpdate({"requests": deleteRequest}, globalVariables().spreadsheetId);
        
        return getLastTenRows();
        }

        function checkID(ID){
        var idList = readData(globalVariables()
        .spreadsheetId,globalVariables().idRange,)
        .reduce(function(a,b){
            return a.concat(b);
            });
        return idList.includes(ID);
        }

        function getRangeByID(id){
        if(id){
            var idList = readData(globalVariables().spreadsheetId,globalVariables().idRange);
            for(var i=0;i<idList.length;i++){
            if(id==idList[i][0]){
                return "''' + var_sheetName + '''!A"+(i+2)+':'+globalVariables().lastCol+(i+2);
            }
            }
        }
        }

        function getRecordById(id){
        if(id && checkID(id)){
            var result = readData(globalVariables().spreadsheetId,getRangeByID(id));
            return result;
        }
        }

        function getRowIndexByID(id){
        if(id){
            var idList = readData(globalVariables().spreadsheetId,globalVariables().idRange);
            for(var i=0;i<idList.length;i++){
            if(id==idList[i][0]){
                var rowIndex = parseInt(i+1);
                return rowIndex;
            }
            }
        }
        }

        function getLastTenRows(){
        var lastRow = readData(globalVariables().spreadsheetId,globalVariables().dataRage).length+1;
        if(lastRow<=11){
            var range = globalVariables().dataRage;
        }else{
            var range = "''' + var_sheetName + '''!A"+(lastRow-9)+':'+globalVariables().lastCol;
        }
        var lastTenRows = readData(globalVariables().spreadsheetId,range);
        return lastTenRows;
        }

        function getAllData(){
        var data = readData(globalVariables().spreadsheetId,globalVariables().dataRage);
        return data;
        }

        function processFormSearch(formObject){  
        var result = "";
        if(formObject.searchtext){ 
            result = search(formObject.searchtext);
        }
        return result;
        }
        
        function search(searchtext){
        var spreadsheetId   = globalVariables().spreadsheetId;
        var dataRage        = globalVariables().dataRage;
        var data = Sheets.Spreadsheets.Values.get(spreadsheetId, dataRage).values;
        var ar = [];
        
        data.forEach(function(f) {
            if (~f.indexOf(searchtext)) {
            ar.push(f);
            }
        });
        return ar;
        }
    '''
    with open('output/Code.gs', 'w') as f:
        f.write(Content)


Create()
