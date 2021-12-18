from django.shortcuts import render

# render main page just bunch of item for list
def list(request):
    return render(request, 'frontapp/list.html')