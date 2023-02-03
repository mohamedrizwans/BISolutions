
def Create():
    with open('Index.html', 'w') as f:
        f.write('''
            <!DOCTYPE html>
            <html>

            <head>
                <base target="_top">
                <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"
                    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
                    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
                    crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js"
                    integrity="sha384-xrRywqdh3PHs8keKZN+8zzc5TX0GRTLCcmivcbNJWm2rs5C8PRhcEn3czEjhAO9o"
                    crossorigin="anonymous"></script>
                <?!= include('JavaScript'); ?> <!-- See JavaScript.html file -->
                <?!= include('CSS'); ?> <!-- See CSS.html file -->
            </head>

            <body onload="createCountryDropdown()">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-6">
                            <?!= include('Form'); ?> <!-- See Form.html file -->
                            <br><br>
                            <div id="output"></div>
                        </div>
                        <div class="col-lg-6">
                            <?!= include('DataTable'); ?> <!-- See DataTable.html File -->
                        </div>
                    </div>
                </div>
            </body>

            </html>
            '''
                )


Create()
