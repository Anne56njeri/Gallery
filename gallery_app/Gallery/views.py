from django.shortcuts import render

# Create your views here.
def start(request):
    title='welcome to Gallery'
    return render(request,'all-images/first.html',{"title":title})
