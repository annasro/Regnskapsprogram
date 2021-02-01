import cgi
form = cgi.FieldStorage()
product = form.getvalue("name")
print(product)
