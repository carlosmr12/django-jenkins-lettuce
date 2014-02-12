from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html = '''
    <html>
        <head>
            <title> Titulo </title>
            <script type="text/javascript" src="http://code.jquery.com/jquery-2.1.0.min.js"></script>
        </head>
        <body><h1>Hello World</h1></body>
    </html>
    ''';

    return HttpResponse(html)
