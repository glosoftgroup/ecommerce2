from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from services import get_products, get_categories, get_product_details, get_category_details

def home(request):
	products = get_products()
	return render(request, "index.html", {'products':products})

def about(request):
	return render(request, "about.html", {})

def contact(request):
	return render(request, "contact.html", {})

def category(request):
	return render(request, "category.html", {})

def category_byId(request):
	if request.method == 'POST':
		cat_id = request.POST['cat_id']
		category = get_category_details(cat_id)
		# return JsonResponse(category)
		return JsonResponse(dict(genres=list(category)))

def products(request):
    products = get_products()
    category = get_categories()
    return render(request,"demo.html",{'products':products, 'categories':category})

def product_detail(request, product_id):
	detail = get_product_details(product_id)
	return render(request, "d.html", {'product_detail':detail})


# class ProductsPage(TemplateView):
#     def get_records(self,request):
#         # products_list = services.get_products('2009', 'edwards')
#         records = services.get_records()
#         return render(request,'demo.html',records)