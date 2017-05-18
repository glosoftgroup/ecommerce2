from django.conf import settings
from django.core.mail import send_mail
from django.template import Context, Template, RequestContext
from django.shortcuts import render, render_to_response
from django.core.exceptions import ObjectDoesNotExist

from products.models import ProductFeatured, Product
from .forms import ContactForm, SignUpForm
from .models import SignUp
from carts.models import Cart

# Create your views here.
def home(request):
	title = 'Sign Up Now'

	featured_image = ProductFeatured.objects.filter(active=True).order_by("?").first()
	products = Product.objects.all().order_by("?")[:6]
	products2 = Product.objects.all().order_by("?")[:6]

	form = SignUpForm(request.POST or None)

	cart_id = request.session.get("cart_id")
	# request.session["cart_id"] = cart_id
	# cart = Cart.objects.get(id=cart_id)
	if cart_id == None:
		count = 0
		cart = Cart()
		cart.tax_percentage = 0.075
		cart.save()
		cart_id = cart.id
	else:
		cart = Cart.objects.get(id=cart_id)
		count = cart.items.count()
	request.session["cart_item_count"] = count
	context = {
		"title": title,
		"form": form,
		"featured_image":featured_image,
		"products":products,
		"products2":products2,
		"object": cart
	}


	if form.is_valid():
		#form.save()
		#print request.POST['email'] #not recommended
		instance = form.save(commit=False)

		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		# if not instance.full_name:
		# 	instance.full_name = "Justin"
		instance.save()
		context = {
			"title": "Thank you"
		}

	return render(request, "index2.html", context)



def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		# 	#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'youotheremail@email.com']
		contact_message = "%s: %s via %s"%( 
				form_full_name, 
				form_message, 
				form_email)
		some_html_message = """
		<h1>hello</h1>
		"""
		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				html_message=some_html_message,
				fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms.html", context)

def minicart(request):
	if request.is_ajax():
		cart_id = request.session.get("cart_id")
		request.session["cart_id"] = cart_id
		cart = Cart.objects.get(id=cart_id)
		template = 'carts/cartpopup.html'
		data = {'object': cart}
	return render_to_response(template, data, context_instance = RequestContext(request))
















