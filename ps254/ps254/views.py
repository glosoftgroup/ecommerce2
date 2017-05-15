from django.shortcuts import render, render_to_response
from django.core import serializers
from django.template import Context, Template, RequestContext
from django.http import HttpResponse, JsonResponse
import json
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

# def category_byId(request):
# 	if request.method == 'POST':
# 		cat_id = request.POST['cat_id']
# 		category = get_category_details(cat_id)
# 		json_category = json.dumps(category)
# 		return HttpResponse(json_category,content_type='application/json')
def category_byId(request):
	if request.is_ajax():
		cat_id = request.GET.get('cat_id')
		category = get_category_details(cat_id)
		template = 'results.html'
		data = {'category': category}
		return render_to_response(template, data, context_instance = RequestContext(request))

def products(request):
    products = get_products()
    category = get_categories()
    return render(request,"demo.html",{'products':products, 'categories':category})

def product_detail(request, product_id):
	detail = get_product_details(product_id)
	return render(request, "detail.html", {'product_detail':detail})