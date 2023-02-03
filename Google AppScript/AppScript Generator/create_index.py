import pandas as pd

df = pd.read_excel(r'TableDesign.xlsx', sheet_name="Sheet1")
# df = df.reset_index()  # make sure indexes pair with number of rows
# print(df["sno"].count())


def Create():
    Content = '''
        <!DOCTYPE html>
        <html>

        <head>
        <base target="_top">

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.0.1/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdn.datatables.net/1.11.5/css/dataTables.bootstrap5.min.css">
        <link rel="stylesheet" href="https://cdn.datatables.net/responsive/2.2.9/css/responsive.bootstrap5.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Niramit:wght@300&family=Prompt:wght@300&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js"></script>

        <style>
        body {
            font-family:Prompt;
            font-size: 14px;
        }

        .btn-group-xs > .btn, .btn-xs {
        padding: .25rem .4rem;
        font-size: .875rem;
        line-height: .5;
        border-radius: .2rem;
        }

        .btn-head-table {
        padding-bottom: 10px;
        }

        .editBtn:hover {
            color: white;
        }
        </style>

        </head>

        <body>
        <div class="container">

            <!-- The Modal Form -->
            <div class="modal" id="myModal">
            <div class="modal-dialog">
                <div class="modal-content">

                <!-- Modal Header -->
                <div class="modal-header">
                    <h2>Add/Edit Data</h2>
                    <button type="button" id="btn-close" class="close" data-dismiss="modal" onclick="clearForm();">&times;</button>
                </div>

                <!-- Modal body -->
                <div class="modal-body">
                    <!-- start form -->
                    <form id="myForm" class="p-2 border border-light rounded bg-light" onsubmit="handleFormSubmit(this)">
                    <!-- Call JavaScript function "handleFormSubmit" -->

                    <div id="message"></div>
                    <input type="text" id="RecId" name="RecId" value="" style="display: none">
                    <div class="form-row">
    '''

    for index, row in df.iterrows():
        Content += '''
            <div class="form-group col-md-6">
                  <label for="''' + row["internalcolumn"] + '''" >''' + row["screencolumn"] + '''</label>
                  <input type="text" class="form-control" id="''' + row["internalcolumn"] + '''" name="''' + row["internalcolumn"] + '''" placeholder="''' + row["screencolumn"] + '''">
            </div>
            '''

    Content += '''
            <button id="btnSubmit" type="submit" class="btn btn-primary" >Save</button>
                    <input class="btn btn-secondary" type="reset" value="Clear">

                    </form>

                    <!-- end datatable -->

                </div>
                </div>
            </div>
            </div>
        </div>

        <!-- DataTable  -->
        <div style="margin-left:20px;margin-top:10px; margin-right:20px">
            <div class="row">
            <div class="col-sm-9">
                <div class="btn-head-table">
                <p></p>
                </div>
            </div>
            </div>
            <div class="row">
            <div class="col-md">

                <!-- start datatable -->
                <div class="table-wrapper" style="height:50px">
                <div class="row">
                    <div class="col-xs-6" style="margin-left:5px;margin-top:10px">
                    <h4>Import/Export Main Data</h4>
                    </div>
                    <div class="col">
                    <!-- button for adding user. ------------------ -->
                    <div class='btn-head-table'>
                        <button type='button' class='btn btn-info'data-toggle='modal' data-target='#myModal'style="float:right;margin-top:-41px; margin-right:5px"> + Add Entry</button>
                    </div>
                    </div>
                </div>
                </div><br>
                <div class="col-auto" style="float:right">
                <form id="search-form" class="form-inline" onclick="loading();" onsubmit="handleFormSubmitSearch(this);">
                    <div class="form-group mb-2">
                    <label for="searchtext"><i class="fa fa-search" aria-hidden="true"></i></label>
                    </div>
                    <div class="form-group mx-sm-3 mb-2">
                    <input type="text" class="form-control" id="searchtext" name="searchtext" placeholder="Search here...">
                    </div>
                    <button type="submit" class="btn btn-primary mb-2">Search</button>
                </form>
                </div>
            </div>

            <!-- <div id="dataTable" class="table-responsive"></div> -->
            <table id="dataTable" class="table dt-responsive nowrap" style="width:100%"></table>

            <!-- <div>
                <button type="button" class="btn btn-primary" onclick="getAllData()">All Data</button>
            </div> -->
            <!-- end datatable -->

            </div>
        </div>

        <?!= HtmlService.createHtmlOutputFromFile('js').getContent() ?>
        <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>
        <script src=" https://code.jquery.com/jquery-3.5.1.js"></script>
        <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
        <script src="https://cdn.datatables.net/1.11.5/js/dataTables.bootstrap5.min.js"></script>
        <script src="https://cdn.datatables.net/responsive/2.2.9/js/dataTables.responsive.min.js"></script>
        <script src="https://cdn.datatables.net/responsive/2.2.9/js/responsive.bootstrap5.min.js"></script>
        </body>

        </html>

    '''

    with open('output/index.html', 'w') as f:
        f.write(Content)


Create()
