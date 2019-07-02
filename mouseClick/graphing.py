from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(16)
# money = [1.5e5, 2.5e6, 5.5e6, 2.0e7,12.5,12.8,1.5e5, 2.5e6, 5.5e6, 2.0e7,12.5,12.8,1.5e5, 2.5e6, 5.5e6, 2.0e7]


# def millions(x, pos):
#     'The two args are the value and tick position'
#     return '$%1.1fM' % (x * 1e-6)


# formatter = FuncFormatter(millions)

# fig, ax = plt.subplots()
# ax.yaxis.set_major_formatter(formatter)
# plt.bar(x, money)
# plt.xticks(x, ('q', 'w', 'e', 'r','t', 'y', 'u', 'i','o', 'p', 'a', 's','d', 'f', 'g', 'h'))
# plt.show()

fh = open('key_log6.txt')
# list =[]
line = fh.readlines()
q = line[0].split("=",1)[1]
w = line[1].split("=",1)[1]
e = line[2].split("=",1)[1]
r = line[3].split("=",1)[1]
t = line[4].split("=",1)[1]
y = line[5].split("=",1)[1]
u = line[6].split("=",1)[1]
i = line[7].split("=",1)[1]
o = line[8].split("=",1)[1]
p = line[9].split("=",1)[1]
a = line[10].split("=",1)[1]
s = line[11].split("=",1)[1]
d = line[12].split("=",1)[1]
f = line[13].split("=",1)[1]
g = line[14].split("=",1)[1]
h = line[15].split("=",1)[1]
j = line[16].split("=",1)[1]
k = line[17].split("=",1)[1]
l = line[18].split("=",1)[1]
z = line[19].split("=",1)[1]
x = line[20].split("=",1)[1]
c = line[21].split("=",1)[1]
v = line[22].split("=",1)[1]
b = line[23].split("=",1)[1]
n = line[24].split("=",1)[1]
m = line[25].split("=",1)[1]


# print(q)
# print(w)
# print(e)
# print(r)
# print(t)
# print(y)
# print(u)
# print(i)
# print(o)
# print(p)
# print(a)
# print(s)
# print(d)
# print(f)
# print(g)
# print(h)
# print(j)
# print(k)
# print(l)
# print(z)
# print(x)
# print(c)
# print(v)
# print(b)
# print(n)
# print(m)



# print(line[0])
# for line in fh:
#     # in python 2
#     # print line
#     # in python 3
#     # print(line)
#     num = line.split("=",1)[1]
#     q = num[0]
#     print(q)
#     # print (line.split("=",1)[1])
#     # print(line[3])
#     # list.append(line)
#     # print(list)
# fh.close()
