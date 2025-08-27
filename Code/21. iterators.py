# Python iterators
"""
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
"""

# iterator bs iterable
# list, tuple , dictionaries are all set of iterable objects.
# they are iterable containers which you can get a iterator from.
# all these objects have a iter() method which is used to get an iterator.

# EXAMPLE :
tuple1 = ("apple", "bannan", "cherry")
iterator1 = iter(tuple1)

print(next(myit))
print(next(myit))
print(next(myit))

# iterate from a string
str1 = "hospital"
iterator2 = iter(str1)

print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
print(next(iterator2))
# if written more than limit it will raise error.

# the __iter__() method acts similar, you can do operations like initializing, but must always return the iterator object itself.
# the __next__() method also allows you to do operations and must return the next item in the sequence.
# Iterators using Class
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
cls_itr1 = iter(myclass)

print(next(cls_itr1))
print(next(cls_itr1))
print(next(cls_itr1))
print(next(cls_itr1))
print(next(cls_itr1))

# to stop iteration from going forever or you want to just stop middle of work.
# use stopiteration 
# stop iteration after 20 iterations.
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

























