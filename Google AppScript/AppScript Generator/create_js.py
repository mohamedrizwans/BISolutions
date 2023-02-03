import pandas as pd

df = pd.read_excel(r'TableDesign.xlsx', sheet_name="Sheet1")
# df = df.reset_index()  # make sure indexes pair with number of rows
# print(df["sno"].count())


def Create():

    Content = '''
        <script>
        window.addEventListener("load", functionInit, true);
        function functionInit(){
            preventFormSubmit();
            getLastTenRows();
        };

        function preventFormSubmit() {
            var forms = document.querySelectorAll('form');
            for (var i = 0; i < forms.length; i++) {
            forms[i].addEventListener('submit', function(event) {
            event.preventDefault();
            });
            }
        }

            function handleFormSubmit(formObject) {
            google.script.run.withSuccessHandler(createTable).processForm(formObject);
            setTimeout(function() {$('#myModal').modal('hide');}, 3000);
            document.getElementById("message").innerHTML = "<div class='alert alert-warning' role='alert'>SAVED!.</div>";
            document.getElementById("myForm").reset();
        }

        function clearForm() {
            document.getElementById("message").innerHTML = "";
            document.getElementById("myForm").reset();
        }

        function getLastTenRows (){
        google.script.run.withSuccessHandler(createTable).getLastTenRows();
        }

        function getAllData(){
            google.script.run.withSuccessHandler(createTable).getAllData();
        }

        function createTable(dataArray) {
            if(dataArray){
            var result = "<div>"+
                        "<table class='table table-sm' style='font-size:1em'>"+
                        "<thead style='white-space: nowrap'>"+
                            "<tr>"+
                            "<th scope='col'>Delete</th>" +
                            "<th scope='col'>Edit</th>" +
    '''

    for index, row in df.iterrows():
        Content += '''
            "<th scope='col'>''' + row["screencolumn"] + '''</th>"+
            '''
    Content += '''
        "</tr>"+
                    "</thead>";
        for(var i=0; i<dataArray.length; i++) {
            result += "<tr>";

            result += "<td><button type='button' class='btn btn-outline-danger btn-xs deleteBtn' onclick='deleteData(this);'><i class='fa fa-trash''></i></button></td>";

            result += "<td><button type='button' class='btn btn-outline-primary btn-xs editBtn' data-toggle='modal' data-target='#myModal' onclick='editData(this);'><i class='fa fa-edit'></i></button></td>";

        for(var j=0; j<dataArray[i].length; j++){
                result += "<td>"+dataArray[i][j]+"</td>";
            }
            result += "</tr>";
        }
        result += "</table></div>";
        var div = document.getElementById('dataTable');
        div.innerHTML = result;
        $(document).ready(function() {
        $('#dataTable').DataTable({
            destroy:true,
            responsive: true,
            ordering: false,
            searching:false,
            pageLength: 5,
            lengthMenu: [
            [5, 10, 25, 50, 100, -1 ],
            ['5', '10', '25', '50','100', 'All' ]
        ],
                columnDefs: [
                {
                // targets: "_all",
                },
                ],
                
        language: {
        sProcessing: "Processing...",
        sLengthMenu: "_MENU_ ",
        sZeroRecords: "No Data",
        sInfo: 'Showing _START_ to _END_ of _TOTAL_ entries',
       
        sInfoPostFix: "",
        sSearch: '<i class="fas fa-search" fa-2x></i> :',
        sUrl: "",
        oPaginate: {
            sFirst: "First Page",
            sPrevious: 'Previous',
            sNext: 'Next',
            sLast: "Last Page"
        },
        },

            });
            });

        document.getElementById("message").innerHTML = "";
        }else{
        var div = document.getElementById('dataTable');
        div.innerHTML = "False!";
        }
        }

        function deleteData(el) {
            Swal.fire({
        title: 'Do You Want Delete This Data?',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            cancelButtonText: 'Cancel',
            confirmButtonText: 'Confirm'
            }).then((result) => {
            if (result.isConfirmed) {

                Swal.fire(
            'Deleted!',
                )

                var recordId = el.parentNode.parentNode.cells[2].innerHTML;
                google.script.run.withSuccessHandler(createTable).deleteData(recordId);
            }
            });
        }

        function editData(el){
            var recordId = el.parentNode.parentNode.cells[2].innerHTML;
            google.script.run.withSuccessHandler(populateForm).getRecordById(recordId);
        }

        function populateForm(records){
            
    '''

    for index, row in df.iterrows():
        Content += '''
           document.getElementById("''' + row["internalcolumn"] + '''").value = records[0][''' + str(index) + '''];
            '''

    Content += '''
        document.getElementById("message").innerHTML = "<div class='alert alert-warning' role='alert'>Update Record [ID: "+records[0][0]+"]</div>";
                }

        function loading(){
        window.addEventListener("load", functionInit, false);
        window.addEventListener("load", preventFormSubmitSearch, true);
            }

        function loading(){
        window.addEventListener("load", functionInit, false);
        window.addEventListener("load", preventFormSubmitSearch, true);
        }
            function preventFormSubmitSearch() {
                var forms = document.querySelectorAll('form');
                for (var i = 0; i < forms.length; i++) {
                forms[i].addEventListener('submit', function(event) {
                event.preventDefault();
                });
                }
            }

            function handleFormSubmitSearch(formObject) {
                google.script.run.withSuccessHandler(createTableSearch).processFormSearch(formObject);
                document.getElementById("search-form").reset();
            }

            function createTableSearch(dataArray) {
                if(dataArray && dataArray !== undefined && dataArray.length != 0){
                var result = "<div>"+
                    "<table class='table table-sm' style='font-size:1em'>"+
                    "<thead style='white-space: nowrap'>"+
                        "<tr>"+
                        //Change table headings to match witht he Google Sheet
    '''

    for index, row in df.iterrows():
        Content += '''
           "<th scope='col'>''' + row["screencolumn"] + '''</th>"+
            '''
    Content += '''
        "</tr>"+
                    "</thead>";
        for(var i=0; i<dataArray.length; i++) {
            result += "<tr>";

            result += "<td><button type='button' class='btn btn-outline-danger btn-xs deleteBtn' onclick='deleteData(this);'><i class='fa fa-trash''></i></button></td>";
            result += "<td><button type='button' class='btn btn-outline-primary btn-xs editBtn' data-toggle='modal' data-target='#myModal' onclick='editData(this);'><i class='fa fa-edit'></i></button></td>";

            for(var j=0; j<dataArray[i].length; j++){
                result += "<td>"+dataArray[i][j]+"</td>";
            }
            result += "</tr>";
        }
        result += "</table></div>";
                //var div = document.getElementById('search-results');
                var div = document.getElementById('dataTable');
                div.innerHTML = result;
                }else{
                //var div = document.getElementById('search-results');
                var div = document.getElementById('dataTable');
                Swal.fire({
                title: 'No Data!',
                showCancelButton: false,
                });
                }
            }

        </script>
    '''

    with open('output/js.html', 'w') as f:
        f.write(Content)


Create()
