from django.shortcuts import render
from .models import Products,GalleryImage
# Create your views here.


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def Product(request):
    products = Products.objects.all()
    return render(request, 'product.html', {'products': products})

def gallery(request):
    featured_images = GalleryImage.objects.filter(featured=True).order_by('-created_at')[:3]
    all_images = GalleryImage.objects.all().order_by('-created_at')
    context={
        'featured_images':featured_images,
        'all_images':all_images
        
    }
    return render(request, 'gallery.html',context)