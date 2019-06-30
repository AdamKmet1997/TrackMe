from pynput.keyboard import Key, Listener, KeyCode
# import logging

# logging.basicConfig(filename=("mouse_log8.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')



# # keyboard letters counter
qc= 0
wc= 0
ec= 0
rc= 0
tc= 0
yc= 0
uc = 0
ic= 0
oc = 0
pc = 0
ac = 0
sc = 0
dc = 0
fc= 0
gc= 0
hc= 0
jc= 0
kc= 0
lc= 0
zc= 0
xc= 0
cc= 0
vc= 0
bc= 0
nc= 0
mc= 0
spacec=0

# keyboard letter assign
q= 'q'
w= 'w'
e= 'e'
r= 'r'
t= 't'
y= 'y'
u = 'u'
i= 'i'
o = 'o'
p = 'p'
a = 'a'
s = 's'
d = 'd'
f= 'f'
g= 'g'
h= 'h'
j= 'j'
k= 'k'
l= 'l'
z= 'z'
x= 'x'
c= 'c'
v= 'v'
b= 'b'
n= 'n'
m= 'm'


class MyException(Exception): pass


def on_press(key):
        # if key.char == 'a':
        #         print('a was pressed ')
        # else:
        #         print('not a ')

        global q 
        global w
        global e
        global r
        global t
        global y
        global u
        global i
        global o
        global p
        global a
        global s
        global d
        global f
        global g
        global h
        global j
        global k
        global l
        global z
        global x
        global c
        global v
        global b
        global n
        global m

        global qc
        global wc
        global ec
        global rc
        global tc
        global yc
        global uc
        global ic
        global oc
        global pc
        global ac
        global sc
        global dc
        global fc
        global gc
        global hc
        global jc
        global kc
        global lc
        global zc
        global xc
        global cc
        global vc
        global bc
        global nc
        global mc
        global spacec

        try:
                # print('alphanumeric key {0} pressed'.format(
                # key.char))


                if key.char == q:
                        qc +=1
                        print('q counter is ', qc)
                if key.char == w:
                        wc +=1
                        print('w counter is ', wc)
                if key.char == e:
                        ec +=1
                        print('e counter is ', ec)
                if key.char == r:
                        rc +=1
                        print('r counter is ', rc)
                if key.char == t:
                        tc +=1
                        print('t counter is ', tc)
                if key.char == y:
                        yc +=1
                        print('y counter is ', yc)
                if key.char == u:
                        uc +=1
                        print('u counter is ', uc)
                if key.char == i:
                        ic +=1
                        print('i counter is ', ic)
                if key.char == o:
                        oc +=1
                        print('o counter is ', oc)
                if key.char == p:
                        pc +=1
                        print('p counter is ', pc)
                if key.char == a:
                        ac +=1
                        print('a counter is ', ac)
                if key.char == s:
                        sc +=1
                        print('s counter is ', sc)
                if key.char == d:
                        dc +=1
                        print('d counter is ', dc)
                if key.char == f:
                        fc +=1
                        print('f counter is ', fc)
                if key.char == g:
                        gc +=1
                        print('g counter is ', gc)
                if key.char == h:
                        hc +=1
                        print('h counter is ', hc)
                if key.char == j:
                        jc +=1
                        print('j counter is ', jc)
                if key.char == k:
                        kc +=1
                        print('k counter is ', kc)
                if key.char == l:
                        lc +=1
                        print('l counter is ', lc)
                if key.char == z:
                        zc +=1
                        print('z counter is ', zc)
                if key.char == x:
                        xc +=1
                        print('x counter is ', xc)
                if key.char == c:
                        cc +=1
                        print('c counter is ', cc)
                if key.char == v:
                        vc +=1
                        print('v counter is ', vc)
                if key.char == b:
                        bc += 1
                        print('b counter is ', bc)
                if key.char == n:
                        nc +=1
                        print('n counter is ', nc)
                if key.char == m:
                        mc +=1
                        print('m counter is ', mc)
        except AttributeError:
                if Key.space:
                        spacec +=1
                        print('space' , spacec)
                print('special key {0} pressed'.format(
                key))


with Listener( on_press=on_press) as listener:
    listener.join() 