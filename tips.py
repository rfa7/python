# Tips for playing with python
a = 1
b = 2

# swap values

a,b = b,a


# print
needle  = 'd'
haystack = ['a','b','c','d']
print(['Not found','Found'][needle in haystack])
# or
print('Found' if needle in haystack else 'Not found')
