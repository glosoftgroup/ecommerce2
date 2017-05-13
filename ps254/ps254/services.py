import xmlrpclib
# common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
#for odoo web api testing purposes
url = 'https://demo.odoo.com/start'
db = 'demodatadb'
username = 'odoo'
password = 'odoo'

info = xmlrpclib.ServerProxy(url).start()
url, db, username, password = \
	info['host'], info['database'], info['user'], info['password']

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
uid = common.authenticate(db, username, password, {})
print common.version()

def get_records():
	record = models.execute_kw(db, uid, password,
		'product.product', 'search_read',
		[[['active', '=', True], ['sale_ok', '=', True], ['image', '=', True]]],
		{'fields': ['name', 'list_price', 'image'], 'limit': 15})
	return record
