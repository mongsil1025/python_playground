# octal (start with 0o + number)
octal = 0o177

# hexadecimal (start with 0x + number)
hexadecimal = 0x8ff

# square
square = 3 ** 4 # 81
print(square)

# multiline
print("=" * 50)
multiline = """
    Life is too short
    You need python
"""
print(multiline)
print("=" * 50)

# slicing
slicing_org = "Life is too short, You need Python"
slicing = slicing_org[0:4]
print(slicing) # life

# Tip: string is immutable, so can not access it by index

# String Function
count = "hobby".count('b')
find_index = "Python is the best choice".find('b') # return -1 if not found
index = "Life is too short".index('t') # error if not found
join = ",".join('abcd')
strip = "   aaa ".strip()

# List
list = [1,2,3]
del list[1] # [1, 3]
list.append(4)
list.sort()
list.reverse()
list.index(4)
list.insert(0,0)
list.remove(4)
list.pop()
list.count(1)
list.extend([10,11,12])

# Tuple
# can not change the value in tuple (unlike list)
tuple1 = (1,)
tuple_multi = (1, 2, 'a', 'b')

# Dictionary
# Node that key have to be UNIQUE
dict = {'name':'mongsil', 'phone':'00000000'}
dict['birth'] = '941025'
dict[(10,20)] = 'tuple_key'
print(dict.keys()) # dict_keys(['name', 'phone', 'birth', (10, 20)])
for k in dict.keys(): # use like list, but do not support List Functions like append, insert, pop, remove, sort 
    print(k)
dict.values()
dict.items()
dict.get('mbti') # return None
# dict['mbti'] # error
'mbti' in dict # false
dict.clear()

# Set
set1 = set([1,2,3])
set2 = set("Hello") # {'e', 'H', 'l' 'o'}

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
# intersect
s1 & s2
s1.intersection(s2)
# union
s1 | s2
s1.union(s2)
# minus
s1 - s2
s1.difference(s2)
#add
s1.add(100)
s1.update([100, 200, 300])