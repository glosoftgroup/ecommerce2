# cart = ['cart']
# item_id = 1
# if cart[item_id]:
# 	cart[item_id]+=1
# 	message = 'You now have '+ str(cart[item_id]) + 'items in your cart'
# else:
# 	cart[item_id]=1
# 	message = 'Successfully added '+str(cart[item_id])+' in your cart'
# print message


 # request.session['my_dict'] = {'a': 1, 'b': 2, 'c': 3}
 # current_dict=request.session['my_dict'] 
 # current_dict.pop('c') 
 # request.session.modified = True
 # request.session['my_dict']=current_dict 
import xmlrpclib

url = 'http://192.168.0.18:8069'
db = 'mydb16'
username = 'pkinuthia10@gmail.com'
password = 'password'
# import xmlrpclib
# url = 'https://demo.odoo.com/start'
# info = xmlrpclib.ServerProxy(url).start()
# url, db, username, password = \
# 	info['host'], info['database'], info['user'], info['password']

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = common.authenticate(db, username, password, {})


# product = models.execute_kw(db, uid, password,
# 	'product.template', 'search_read',
# 	[[['active', '=', True], ['sale_ok', '=', True]]],
# 	{'fields': ['name', 'list_price', 'image', 'description'], 'limit': 6})
def get_root_categories():
	root_category = models.execute_kw(db, uid, password,
		'product.category','search_read',[[['parent_id','=',[0]]]],
		{'fields':['name','id', 'child_id']})
	return root_category

#( Parent Categories)
def get_parent_categoriesBy(root_id):
	rt_id = int(root_id)
	parent_category = models.execute_kw(db, uid, password,
		'product.category','search_read',[[['parent_id','=',rt_id]]],
		{'fields':['name','id','parent_id']})
	return parent_category

#( Child Categories)
def get_child_categoriesBy(parent_id):
	pr_id = int(parent_id)
	child_category = models.execute_kw(db, uid, password,
		'product.category','search_read',[[['parent_id','=',pr_id]]],
		{'fields':['name','id','parent_id']})
	return child_category

rt =get_root_categories()
print 'Root categs --'+'*'*100
print rt
for r in get_root_categories():
	root_id = int(r['id'])
	parent_categories = get_parent_categoriesBy(root_id)
	print 'parent categs --'+'$'*100
	print parent_categories
	for p in parent_categories:
		parent_id = int(p['id'])
		child_categories = get_child_categoriesBy(parent_id)
		print 'Child Categs --'+'#'*100
		print child_categories
# print tr.root_categories
# print rt.child_id
# print child_categories