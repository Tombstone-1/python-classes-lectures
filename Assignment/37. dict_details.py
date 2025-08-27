book_detail = {'book_id': 10, 'book_name': 'death stranding'}

print(book_detail)
book_detail['price'] = 1000
book_detail['book_name'] = 'death stranding part 2'
book_detail.update({'author': 'hideo kojima', 'publisher': 'Sony'})
print(book_detail)

del book_detail['price']

print(book_detail)

x = input("Enter book name = ")
if x in book_detail.values():
    print(x, 'present')
else:
    print("not present")
