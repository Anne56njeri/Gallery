from django.shortcuts import render

# Create your views here.
def start(request):
    title='welcome to Gallery'
    my_images=Image.objects.all()
    return render(request,'all-images/first.html',{"title":title,"my_images":my_images})
