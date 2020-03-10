from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil
# Create your views here.
def index(requst):
   # products = Product.objects.all()
    #(products)

    allprods=[]
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))

        allprods.append([prod, range(1 ,nSlides),nSlides])

   # params ={'no_of_slides':nSlides, 'range': range(1,nSlides), 'product': products}
    #allprods = [[products, range(1, nSlides), nSlides],
     #           [products, range(1, nSlides), nSlides]]
    params ={'allprods':allprods}
    return render(requst,'shop/index.html',params)

def about(requst):
    return render(requst,'shop/about.html')

def contact(requst):
    if requst.method=="POST":
        name = requst.POST.get('name','')
        email = requst.POST.get('email','')
        phone = requst.POST.get('phone','')
        desc = requst.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    return render(requst,'shop/contact.html')

def tracker(requst):
    return render(requst, 'shop/tracker.html')

def search(requst):
    return render(requst, 'shop/search.html')

def productView(requst,myid):
    #fetch the product using id.
    product = Product.objects.filter(id=myid)
    return render(requst,'shop/prodView.html',{'product':product[0]})

def checkout(requst):
    return render(requst,'shop/checkout.html')