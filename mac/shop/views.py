from math import ceil

from django.shortcuts import render

from .models import Product, Contact, Orders


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
    if requst.method == "POST":
        items_json = requst.POST.get('itemsJson', '')
        name = requst.POST.get('name', '')
        email = requst.POST.get('email', '')
        address = requst.POST.get('address1', '') + " " +requst.POST.get('address2', '')
        city = requst.POST.get('city', '')
        state = requst.POST.get('state', '')
        zip_code = requst.POST.get('zip_code', '')
        phone = requst.POST.get('phone', '')
        order = Orders( items_json=items_json,name=name, email=email,address=address,city=city,state=state,zip_code=zip_code, phone=phone)
        order.save()

        thank = True
        id= order.order_id
        return render(requst,'shop/checkout.html',{'thank':thank,'id':id})
    return render(requst,'shop/checkout.html')