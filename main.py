import functions_framework

@functions_framework.http
def line_webhook(request):
    return 'OK', 200
