from django.shortcuts import render
import base64
from django.views.generic import TemplateView
from services import get_records

def home(request):
	records = get_records()
	return render(request, "index.html", {'records':records})

def about(request):
	return render(request, "about.html", {})

def contact(request):
	return render(request, "contact.html", {})

def category(request):
	return render(request, "category.html", {})

def records(request):
    records = get_records()
    return render(request,"demo.html",{'records':records})

# class ProductsPage(TemplateView):
#     def get_records(self,request):
#         # products_list = services.get_products('2009', 'edwards')
#         records = services.get_records()
#         return render(request,'demo.html',records)