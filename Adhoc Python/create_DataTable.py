
def Create():
    with open('DataTable.html', 'w') as f:
        f.write('''
        <p class="h4 mb-4 text-center">Contact Details Database</p>

<div id="dataTable" class="table-responsive">
    <!-- The Data Table is inserted here by JavaScript -->
</div>
<br>
<button type="button" class="btn btn-success btn-sm" onclick="getAllData()">Get ALL Data</button>
         '''
                )


Create()
