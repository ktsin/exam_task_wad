from django.shortcuts import render

# Create your views here.


def layout_example(request):
    return render(request, 'layout.html')