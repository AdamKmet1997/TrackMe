from pynput.keyboard import Key, Listener, KeyCode
import logging

logging.basicConfig(filename=("mouse_log9.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')



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
total = 0

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
        global total

        try:
                # print('alphanumeric key {0} pressed'.format(
                # key.char))


                if key.char == q:
                        qc +=1
                        total +=1
                        logging.info('q counter is {0}'.format(qc))
                        logging.info(total)
                if key.char == w:
                        wc +=1
                        total +=1
                        logging.info('w counter is {0}'.format(wc))
                        logging.info(total)
                if key.char == e:
                        ec +=1
                        total +=1
                        logging.info('e counter is {0}'.format(ec))
                        logging.info(total)
                if key.char == r:
                        rc +=1
                        total +=1
                        logging.info('r counter is {0}'.format(rc))
                        logging.info(total)
                if key.char == t:
                        tc +=1
                        total +=1
                        logging.info(total)
                        logging.info('t counter is {0}'.format(tc))
                if key.char == y:
                        yc +=1
                        total +=1
                        logging.info(total)
                        logging.info('y counter is {0}'.format(yc))
                if key.char == u:
                        uc +=1
                        total +=1
                        logging.info(total)
                        logging.info('u counter is {0}'.format(uc))
                if key.char == i:
                        ic +=1
                        total +=1
                        logging.info(total)
                        logging.info('i counter is {0}'.format(ic))
                if key.char == o:
                        oc +=1
                        total +=1
                        logging.info(total)
                        logging.info('o counter is {0}'.format(oc))
                if key.char == p:
                        pc +=1
                        total +=1
                        logging.info(total)
                        logging.info('p counter is {0}'.format(pc))
                if key.char == a:
                        ac +=1
                        total +=1
                        logging.info(total)
                        logging.info('a counter is {0}'.format(ac))
                if key.char == s:
                        sc +=1
                        total +=1
                        logging.info(total)
                        logging.info('s counter is {0}'.format(sc))
                if key.char == d:
                        dc +=1
                        total +=1
                        logging.info(total)
                        logging.info('d counter is {0}'.format(dc))
                if key.char == f:
                        fc +=1
                        total +=1
                        logging.info(total)
                        logging.info('f counter is {0}'.format(fc))
                if key.char == g:
                        gc +=1
                        total +=1
                        logging.info(total)
                        logging.info('g counter is {0}'.format(gc))
                if key.char == h:
                        hc +=1
                        total +=1
                        logging.info(total)
                        logging.info('h counter is {0}'.format(hc))
                if key.char == j:
                        jc +=1
                        total +=1
                        logging.info(total)
                        logging.info('j counter is {0}'.format(jc))
                if key.char == k:
                        kc +=1
                        total +=1
                        logging.info(total)
                        logging.info('k counter is {0}'.format(kc))
                if key.char == l:
                        lc +=1
                        total +=1
                        logging.info(total)
                        logging.info('l counter is {0}'.format(lc))
                if key.char == z:
                        zc +=1
                        total +=1
                        logging.info(total)
                        logging.info('z counter is{0}'.format(zc))
                if key.char == x:
                        xc +=1
                        total +=1
                        logging.info(total)
                        logging.info('x counter is {0}'.format(xc))
                if key.char == c:
                        cc +=1
                        total +=1
                        logging.info(total)
                        logging.info('c counter is {0}'.format(cc))
                if key.char == v:
                        vc +=1
                        total +=1
                        logging.info(total)
                        logging.info('v counter is {0}'.format(vc))
                if key.char == b:
                        bc += 1
                        total +=1
                        logging.info(total)
                        logging.info('b counter is{0}'.format(bc))
                if key.char == n:
                        nc +=1
                        total +=1
                        logging.info(total)
                        logging.info('n counter is{0}'.format(nc))
                if key.char == m:
                        mc +=1
                        total +=1
                        # logging.info(total)
                        logging.info('m counter is {0}'.format(mc))
        except AttributeError:
                if Key.space:
                        spacec +=1
                        logging.info('space' , spacec)
                logging.info('special key {0} pressed'.format(
                key))


with Listener( on_press=on_press) as listener:
    listener.join() 