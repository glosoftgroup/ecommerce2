import xmlrpclib
# common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
#for odoo web api testing purposes
# url = 'https://demo.odoo.com/start'
url = 'http://192.168.0.18:8069'
db = 'mydb16'
username = 'pkinuthia10@gmail.com'
password = 'password'

# info = xmlrpclib.ServerProxy(url).start()
# url, db, username, password = \
# 	info['host'], info['database'], info['user'], info['password']

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = common.authenticate(db, username, password, {})
# print common.version()

#get all the products
def get_products():
	product = models.execute_kw(db, uid, password,
		'product.template', 'search_read',
		[[['active', '=', True], ['sale_ok', '=', True]]],
		{'fields': ['name', 'list_price', 'image', 'description'], 'limit': 6})
	return product
#get all the categories
def get_categories():
	category = models.execute_kw(db, uid, password,
		'product.category','search_read',
		[[]],{'fields':['name','id'], 'limit':12})
	return category
#get details of a queried product
def get_product_details(product_id):
	detail = models.execute_kw(db, uid, password,
		'product.template','search_read',[[['id','=',product_id]]],
		{'fields':['name','list_price','image', 'description']})
	return detail
#get details as products in the specified category
def get_category_details(category_id):
	categ_id = int(category_id)
	category = models.execute_kw(db, uid, password,
		'product.template','search_read',[[['categ_id','=',categ_id]]],
		{'fields':['name','list_price','image', 'description']})
	return category

#(Root Categories) get categories according to family tree 
def get_root_categories():
	root_category = models.execute_kw(db, uid, password,
		'product.category','search_read',[[['parent_id','=',[0]]]],
		{'fields':['name','id']})
	return root_category

#( Parent Categories)
def get_parent_categoriesBy(root_id):
	rt_id = int(root_id)
	parent_category = models.execute_kw(db, uid, password,
		'product.category','search_read',[[['parent_id','=',rt_id]]],
		{'fields':['name','id']})
	return parent_category

#( Child Categories)
def get_child_categoriesBy(parent_id):
	pr_id = int(parent_id)
	child_category = models.execute_kw(db, uid, password,
		'product.category','search_read',[[['parent_id','=',pr_id]]],
		{'fields':['name','id']})
	return child_category