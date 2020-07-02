#1.Write a python program to create a tuple.
x = ()      
print(x)
tuple = (1, 2,3)
print(tuple)
#Output:-
#()
#(1, 2, 3)

#2.Write a python program to create a tuple with different data types.
tuple = ("Python", True,3.2, 35)
print(tuple)
#Output:-
#('Python', True, 3.2, 35)

#3.Write a python program to convert a tuple to a string.
t = ('p','y','t','h','o','n')
str =  ''.join(t)
print(str)
#Output:-
#python

#4.Write a python program to slice a tuple.
t = ("a", "p","p", "l", "e")
print(t[3:])                  
print(t[:-2])
print(t[2:4])
print(t[::-1])
#Output:-
#('l', 'e')
#('a', 'p', 'p')
#('p', 'l')
#('e', 'l', 'p', 'p', 'a')

#5.Write a python program to find the length of a tuple.
tuple1 = ("apple", "banana", "cherry")
print(tuple1)
print(len(tuple1))
tuple2=('p','y','t',' ','h','o','n')
print(tuple2)
print(len(tuple2))
#Output:-
#('apple', 'banana', 'cherry')
#3
#('p', 'y', 't', ' ','h', 'o', 'n')
#7

#6.Write a python program to convert a tuple to a dictionary.
tuple = ((1,"a"),  (2,"b"),(3,"c"),(4,"d"))
dct=dict((y, x) for x, y in tuple)
print(dct)
#Output:-
#{'a': 1, 'b': 2, 'c': 3, 'd': 4}

#7.Write a python program to reverse a tuple.
a = ('m','a','n','g','o')
b = reversed(a)
print(tuple(b))
x = (5,13, 24,37)
y = reversed(x)
print(tuple(y))
#Output:-
#('o', 'g', 'n', 'a', 'm')
#(37 ,24 ,13 ,5)

#8.Write a python program to convert a list of tuples into a dictionary.
l = [("a",1) , ("b",2) , ("c",3)]
d = { }
for a , b in l :
	d.setdefault(a,[ ]).append(b)
print(d)
#Output:-
#{'a': [1], 'b': [2], 'c': [3]}

#9.Write a python program to convert a list to a tuple.
list = [1,2,3,4,5]
print(list)
tuplex= tuple(list)
print(tuplex)
#Output:-
#[1, 2, 3, 4, 5]
#(1, 2, 3, 4, 5)
