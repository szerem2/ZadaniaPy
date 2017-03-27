from __future__ import print_function


class Data:
    pass

my_list = []
for i in range(20):
    data = Data()
    data.n = i
    data.n_squared = i * i
    my_list.append(data)

xxx = ([x for x in my_list  if x.n > 14 and x.n <= 18])
table0 = range(0, 21)
print (table0)
table1 = [x for x in table0 if x > 13 and x <= 18]
print (table1)
print ('First: %r' % table1[0])
print (table1[:2])
print ('Last: %r' % table1[-1])
print (table1[-2:])

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
a=range(17)
print(a)
# pierwszych osiem
print(a[:8])
# od 8 dokonca
print(a[8:])
# siedem ostatnich
print(a[-7:])
# do siudmego od konca
print(a[:-7])
# co trzeci
print(a[::3])
# co czwarty od konca
print(a[::-4])
