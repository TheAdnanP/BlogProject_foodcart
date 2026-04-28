from .models import Product                                                                                              
from django.shortcuts import redirect, render

# Create your views here.

def add_product(request):
    return render(request,"add.html")

def add_product_post(request):
    if request.method == "POST":
        nm = request.POST.get('name')
        price = request.POST.get('price')
        des = request.POST.get('description')
        img = request.FILES.get('image')

        obj = Product(
            name=nm,
            price=price,
            description=des,
            image=img
        )
        obj.save()

        return redirect('/add_product')

    return redirect('/')