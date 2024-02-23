# s = 'hello'
# print(s.capitalize())
# print(s.rjust(17))
# print(s.center(7))
# print(s.replace('l', 'ell'))


# nums = list(range(15))
# print(nums)
# print(nums[2:7])
# print(nums[4:])
# print(nums[:])
# print(nums[:12])
# nums[2:3] = [17,18]
# print(nums)


# animals = {'max', 'tillu', 'zozo'}
# for animal in animals:
#      print(animal)
# for idx, animal in enumerate(animals):
#     print("#%d: %s" % (idx+1, animal))


# nums = [0,1,2,3,4,5]
# square = []
# for numbers in nums:
#     if(numbers % 2 == 0):
#         square.append(numbers**2)
# print(square)

# square.clear()

# square = [x**2 for x in nums if x % 2 == 0]
# print(square)



        # Dictionary

# d = {'name':'Marhaba', 'roll number': 103}
# print(d)
# for x in d:
#     print(x) # name, roll number
# for x in d:
#     print(d[x]) # Marhaba, 103

# print('name' in d)
# print(d.get('name'))

# d['him'] = 'Hamdan'
# print(d)

# # del d['him']
# # print(d)

# for x in d:
#     a = d[x]
#     print("%s: %s" % (x, a))

# nums = [0,1,2,3,4,5]
# evenNumsSquare = {x:x**2 for x in nums if x % 2 == 0}
# print(evenNumsSquare)


    # Sets (Unordered (any element can be printed first))
# s = {'marhaba', 'Hamdan', 'ugh'}
# print(s)

# for x in s:
#     print(x)
# print('Hamdan' in s) # gives True
# s.add('apple')
# print(s)
# s.remove('apple')
# print(s)



    #Tuples
# t = {(x,x+1): x for x in range(5)}
# print(t)
# tuple = (1,2)
# print(type(tuple))
# print(tuple in t)
# print(t[4,5])




# def greet(name, loud = False):
#     if(loud == False):
#         print("%s %s", "Hello", name)
#     else:
#         print("%s %s", "HELLO", name.upper())

# greet('marhaba', True)


