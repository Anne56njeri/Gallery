from django.shortcuts import render
from .models import Image,Category
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
    searched_categories=Category.search(search_term)
    return render (request,'all-images/search.html',{"searched_categories":searched_categories})
