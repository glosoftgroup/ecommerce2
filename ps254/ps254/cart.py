# rom django.shortcuts import render, render_to_response
# from django.core import serializers
# from django.template import Context, Template, RequestContext
# from django.http import HttpResponse, JsonResponse
# import json
# import random
# from django.views.generic import TemplateView

# #get the shopping cart
# def shopping_cart(request, template_name='orders/shopping_cart.html'):    
# '''    
# This view allows a customer to see what products are currently in their shopping cart.    
# '''    
# 	cart = get_shopping_cart(request)    
# 	ctx = {'cart': cart}    
# 	return render_to_response(template_name, ctx, context_instance=RequestContext(request))

# #add to cart function
# def add_to_cart(request, queryset, object_id=None, slug=None,slug_field='slug', template_name='orders/add_to_cart.html'):    
# '''    This view allows a customer to add a product to their shopping cart. A single GET parameter can be included to specify the quantity of the product to add.''' 

# 	obj = lookup_object(queryset, object_id)    
# 	quantity = request.GET.get('quantity', 1)    
# 	cart = get_shopping_cart(request)    
# 	cart.add_item(obj, quantity)    
# 	update_shopping_cart(request, cart)    
# 	ctx = {'object': obj, 'cart': cart}    
# 	return render_to_response(template_name, ctx, context_instance=RequestContext(request))

# #remove from cart
# def remove_from_cart(request, cart_item_id, template_name='orders/remove_from_cart.html'):    
# '''    This view allows a customer to remove a product from their shopping cart. It simply removes the entire product from the cart, without regard to quantities.    '''    
# 	cart = get_shopping_cart(request)    
# 	cart.remove_item(cart_item_id)    
# 	update_shopping_cart(request, cart)    
# 	ctx = {'cart': cart}    
# 	return render_to_response(template_name, ctx, context_instance=RequestContext(request)

# #helper function for retreiving the product
# def lookup_object(queryset, object_id=None):    
# 	if object_id is not None:        
# 		obj = queryset.get(pk=object_id)    
# 	else:         
# 		raise Http404     
# 	return ob

# #Cart class and Item class (inside cart class)
# class Cart(object):    
# 	class Item(object):        
# 		def __init__(self, itemid, product, quantity=1):            
# 			self.itemid = itemid            
# 			self.product = product            
# 			self.quantity = quantity
# 	    def __init__(self):         
# 		    self.items = list()         
# 		    self.unique_item_id = 0
# 		    def _get_next_item_id(self):        
# 		    self.unique_item_id += 1        
# 		    return self.unique_item_id    
# 		next_item_id = property(_get_next_item_id)
# 	    def add_item(self, product, quantity=1):        
# 		    item = Item(self.next_item_id, product, quantity)         
# 		    self.items.append(item)
# 	    def remove_item(self, itemid):        
# 	    	self.items = filter(lambda x: x.itemid != itemid, self.items)


# class CheckoutView(object):    
# 	template = 'payments/checkout.html'    
# 	extra_context = {}    
# 	cart = None    
# 	cart_class = Cart    
# 	request = None    
# 	form = None    
# 	form_class = None

#     def __init__(self, template=None, form_class=CheckoutForm,context_class=RequestContext):        
# 	    self.context_class = context_class        
# 	    self.form_class = form_class        
# 	    if template is not None:
# 	    	self.template = template

#     def __unicode__(self):        
#     	return self.__class__.__name__

#     def get_shopping_cart(self, request):        
#     	self.cart = request.session.get('cart', None) or self.cart_ class()

#     def __call__(self, request):        
#     	self.request = request        
#     	return self.return_response()

#     def return_response(self):        
#     	self.form = self.form_class()        
#     	context = {'cart': self.cart, 'form': self.form}        
#     	context.update(self.get_extra_context())        
#     	return render_to_response(self.template, context,context_instance=self.context_class(self.request))
    	
#     def get_extra_context(self):         
#     	return self.extra_context 