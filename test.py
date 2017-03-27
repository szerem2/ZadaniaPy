
# stepwise Freezing and Thawing
class FrozenUnfrozen(object):
    """
    """
    def __init__(self):
        """ Constructof for FrozenUnfrozen
        """
        self.__repr = {}                # dictionary
        self.__frozen = False
    def __getitem__(self, key):
        return self.__repr[key]
    def __setitem__(self, key, value):
        if self.__frozen:
            raise KeyError("Cannot chanage key %r" % key)
        self.__repr[key] = value
    def freeze(self):
        self.__frozen = True
    def unfreeze(self):
        self.__frozen = False

fuf = FrozenUnfrozen()
x = fuf["a"] = 100
print(x)
# fuf.freeze()
fuf["a"] = 200
fuf.unfreeze()
fuf["a"] = 300
x = fuf["a"]
print(x)




# # Freeze classes
# class Reader(object):
#     """ Opis
#         to jest opis klasy
#     """
#     def __init__(self, ):
#         """ Constructof for Reader
#         """
#         self.data = self._read()
#
#     @staticmethod
#     def _read():
#         """ Returning tuple of tuple of read data
#         """
#         data = []
#         with open("data.txt") as fobj:
#             header1 = fobj.readline ( )
#             header2 = fobj.readline ( )
#             header3 = fobj.readline ( )
#             header4 = fobj.readline ( )
#             for line in fobj:
#                 data.append(tuple(line.split()))
#             return tuple(data)
#             # return tuple( tuple(line.split()) for line in open("data.txt") )
# x = Reader()
# print(x.data)




# # avoid side effects
# class MyClass(object):
#     """Example for init only definitions"""
#     def __init__(self):
#         """Constructof for MyClass"""
#         self.attr1 = self._make_attr1()
#         self.attr2 = self._make_attr2()
#
#     @staticmethod
#     def _make_attr1():
#         """Do many things to create attr1"""
#         attr1 = []
#         # skip many lines
#         return attr1
#     @staticmethod
#     def _make_attr2():
#         pass


# #Immutable Data Type TUPLE
# my_list = range(10)
# my_tuple= tuple(my_list)
# my_set  = set(my_list)
# my_frox = frozenset(my_list)
# print (my_list)
# print (my_tuple)
# print (my_set)
# print (my_frox)
# print ("hello %s you are %s years old" % ('Franek', 1))



# # decorators
# import time
# def timeit(method):
#     def timed(*args, **kw):
#         ts = time.time()
#         result = method(*args, **kw)
#         te = time.time()
#         print '[%r] %2.2f sec' % (method.__name__, te-ts)
#         return result
#     return timed
# @timeit
# def f1():
#     time.sleep(1)
#     return
# @timeit
# def f2(a):
#     time.sleep(2)
#     return
# @timeit
# def f3(a, *args, **kw):
#     time.sleep(0.3)
#     return
# f1()
# f2(22)
# f3(33, 44, foo=3)



# # list comprehension insted of filter
# x = filter(lambda x: (x > 10), range(5,16) )
# print (x)
# x = [x for x in range(5,16) if (x > 10) ]
# print (x)


# # list comprehension insted of map
# x = map(lambda a: a * 2, range(2,6) )
# print (x)
# x = [ x*2 for x in range(2,6) ]
# print (x)


# # Lambda
# def use_callbaack(callback, arg):
#     return callback(arg)
# x = use_callbaack(lambda a: a*2, 10)
# print (x)
#
# def double(arg):
#     return arg*2
# x = use_callbaack(double, 10)
# print (x)



# # recursion
# def loop(n):
#     for x in xrange(int(n)):
#         a = 1+1
#     return a
# loop(10)
#
# def recurse(n):
#     if n <= 0:
#         return
#     a = 1 + 1
#     recurse(int(n) - 1)
# recurse(10)




# # partial function
# import functools
# def func(a,b,c):
#     return a,b,c
#
# x = func(1,2,3)
# print (x)
#
# p_func = functools.partial(func, 10)
# x = p_func(1,2)
# print (x)
#
# p_func = functools.partial(func, 10, 12)
# x = p_func(1)
# print (x)


# # Closures and curring
# def outer(outer_arg):
#     def inner(inner_arg):
#         return inner_arg + outer_arg
#     return inner
#
# func = outer(10)
# x = func(5)
# print (x)


# # functions are objects
# def func1():
#     return 1
# def func2():
#     return 2
#
# my_func = {'a':func1, 'b':func2}
# x = my_func['a']()
# print (x)
# x = my_func['b']()
# print (x)


# import sys
# print (sys.version)








# class MyClass( object ):
#     def __init__(self):
#         self.attr1 = self._make_attr1()
#         self.attr2 = self._make_attr2()
#     @staticmethod
#     def _make_attr1():
#         attr = []
#         return attr
#     @staticmethod
#     def _make_attr2():
#         attr = []
#         return attr
# x = MyClass()
# print (x._make_attr1())
#
# #decorators
#
# import functools
# def decorator(func):
#     @functools.wraps(func)
#     def new_func(*args, **kwargs):
#         print ("decorator wad here")
#         return func(*args, **kwargs)
#     return new_func
#     print ("aaaaa")
#
# @decorator
# def add(a,b):
#     return a+b
#
# x = add(1,3)
# print (x)
#
# #
# # def double(arg):
# #     return arg*2
# #
# # # list comprehension
# # x = filter(lambda a: (a > 10), range(5,16))
# # print (x)
# # x = [x                  # select
# #         for x in range(5,16)  # from
# #         if x > 10 # where
# #      ]
# # print (x)
# #
# #
# # x = map(double, range(2,6))
# # print (x)
# # x = map(lambda a: a*2, range(2,6))
# # print (x)
# # x = [x*2 for x in range(2,6)]
# # print (x)
# #
# #
# #
# #
# #
# #
# # # callback function
# # def use_callback(callback, arg):
# #     return callback(arg)
# #
# # x = use_callback(lambda a: a*2, 10)
# # print (x)
# #
# # x = use_callback(double, 10)
# # print (x)
# #
