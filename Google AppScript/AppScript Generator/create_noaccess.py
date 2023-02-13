
def Create():

    Content = '''
        <!DOCTYPE html>
        <html>
        <head>
            <base target="_top">
        </head>
        <body>
            <h1> You Do Not Have Access !! </h1>
        </body>
        </html>
    '''

    with open('output/noaccess.html', 'w') as f:
        f.write(Content)


Create()
