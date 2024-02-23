import numpy as np

# a = np.array([1,2,3])
# print(type(a))
# print(a)
# print(a.shape)
# print(a[0], a[1], a[2])
# a[0] = 5
# print(a)

# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(type(b))
# print(b.shape)
# print(b)

a = np.zeros((3,2))
print(a)

b = np.ones((2,2))
print(b)

c = np.full((2,3), 6)
print(c)

d = np.eye(3)
print(d)

e = np.random.random((3,6))
print(e)

