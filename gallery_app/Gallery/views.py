from django.shortcuts import render
from .models import Image,Category,Location
from django.http import Http404

# Create your views here.
def start(request):
    title='welcome to Gallery'
    my_images=Image.objects.all()
    return render(request,'all-images/first.html',{"title":title,"my_images":my_images})
def image(request,image_id):
    try:
        images=Image.objects.get(id=image_id)
    except DoesNotExsist:
        raise Http404()
    return render(request,"all-images/image.html",{"images":images})
def search_category(request):
    search_term=request.GET.get("category")
    searched_categories=Image.search(search_term)
    return render (request,'all-images/search.html',{"searched_categories":searched_categories})
def london(request):
    location=Image.London()
    return render (request,'all-images/location.html',{"location":location})
def china(request):
    location=Image.China()
    return render (request,'all-images/location1.html',{"location":location})
def malawi(request):
    location=Image.Malawi()
    return render (request,'all-images/location2.html',{"location":location})
def europe(request):
    location=Image.Europe()
    return render (request,'all-images/location3.html',{"location":location})
