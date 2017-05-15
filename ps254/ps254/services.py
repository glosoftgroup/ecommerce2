import xmlrpclib
# common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
#for odoo web api testing purposes
url = 'https://demo.odoo.com/start'
# db = 'demodatadb'
# username = 'odoo'
# password = 'odoo'

info = xmlrpclib.ServerProxy(url).start()
url, db, username, password = \
	info['host'], info['database'], info['user'], info['password']

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = common.authenticate(db, username, password, {})
print common.version()

def get_products():
	product = models.execute_kw(db, uid, password,
		'product.template', 'search_read',
		[[['active', '=', True], ['sale_ok', '=', True]]],
		{'fields': ['name', 'list_price', 'image', 'description'], 'limit': 15})
	return product

def get_categories():
	category = models.execute_kw(db, uid, password,
		'product.category','search_read',
		[[]],{'fields':['name','id'], 'limit':12})
	return category

def get_product_details(product_id):
	detail = models.execute_kw(db, uid, password,
		'product.template','search_read',[[['id','=',product_id]]],
		{'fields':['name','list_price','image', 'description']})
	return detail

def get_category_details(category_id):
	categ_id = int(category_id)
	category = models.execute_kw(db, uid, password,
		'product.template','search_read',[[['categ_id','=',categ_id]]],
		{'fields':['name','list_price','image', 'description']})
	return category