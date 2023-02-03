import pandas as pd

df = pd.read_excel(r'TableDesign.xlsx', sheet_name="Sheet1")
# df = df.reset_index()  # make sure indexes pair with number of rows
# print(df["sno"].count())


def Create():
    Content = '''
    <form id="myForm" class="p-2 border border-light rounded bg-light" onsubmit="handleFormSubmit(this)">
    <!-- Call JavaScript function "handleFormSubmit" -->
    <p class="h4 mb-4 text-center">Contact Details Form</p>
    <div id="message"></div>
    <input type="text" id="RecId" name="RecId" value="" style="display: none">
        <div class="form-group">
    '''

    for index, row in df.iterrows():
        Content += '''
            <label for="''' + row["internalcolumn"] + '''">''' + row["screencolumn"] + '''</label>
            <input type="text" class="form-control" id="''' + row["internalcolumn"] + '''" name="''' + row["internalcolumn"] + '''" placeholder="''' + row["screencolumn"] + '''" required>
            '''
    Content += '''
    </div>


    <button type="submit" class="btn btn-primary">Submit</button>
    <input class="btn btn-secondary" type="reset" value="Reset">
    </form> 
    '''

    with open('Form.html', 'w') as f:
        f.write(Content)


Create()
