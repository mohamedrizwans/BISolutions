
def Create():
    with open('CSS.html', 'w') as f:
        f.write('''
        <style>
        .btn-group-xs>.btn,
        .btn-xs {
            padding: .25rem .4rem;
            font-size: .875rem;
            line-height: .5;
            border-radius: .2rem;
        }
    </style>'''
                )


Create()
