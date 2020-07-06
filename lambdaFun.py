# Lambda is a one liner function
# def plus(a, b):
#     return a+b
#
# print(plus(1,5))

# plus = lambda a, b: a + b     This is Lambda function
# print(plus(10,7))

# def a_first(a):
#     return a[1]

# a_first = lambda a: a[1]

a = [[1,4], [5,6], [7,3], [8, 10]]
a.sort(key = lambda x: x[1])
print(a)