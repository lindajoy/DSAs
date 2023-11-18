# Lets understand sets.

# You can define a set with the built in method set()
sample_set = set()
#or
sample_set_2 = set([1,3,4,5,5,5,66,7]) 
# Output should be: {1,3,4,5,66,7}
sample_set_3 = set(('foo', 'bar', 'baz', 'foo', 'qux'))
# {'qux', 'foo', 'bar', 'baz'}

# Strings are also an iterable so a string can also be passed to a set() as well.
s = 'quux'
print(list(s))
#['q', 'u', 'u', 'x']
print(set(s))
# {'x', 'u', 'q'}

# Alternately a set can be defined with curly braces({})
x = {'foo', 'bar', 'baz', 'foo', 'qux'}
#{'qux', 'foo', 'bar', 'baz'}
x1 = {'q', 'u', 'u', 'x'}
#{'x', 'q', 'u'}

# Adding and removing elements from a set.
sampleSet= {1,2,3}
sampleSet.add(4)
sampleSet.add(5)
print("Sample Set After adding 4 and 5:", sampleSet)
sampleSet.remove(1)
print("Sample Set After removing 1:", sampleSet)
sampleSet.discard(2)
print("Sample set After discarding 2:", sampleSet)

# Discard and remove work similary they remove an element in the set.
# If element not found it returns a keyError.




