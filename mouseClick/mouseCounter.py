from pynput.mouse import Listener
from pynput.keyboard import Key, Listener, KeyCode
import logging

logging.basicConfig(filename=("mouse_log1.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

counter = 0

# keyboard letters counter
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



# def on_click(x, y, button, pressed):
#     if pressed:
#         logging.info(' clicked at ({0}, {1}) with {2}'.format(x, y, button))

#counts the amount of clicks with left mouse  and saves the count into a file 

def on_click(x, y, button, pressed):
    global counter

    if pressed:
        counter += 1
        # print(counter)faaa
        logging.info(counter)

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

        if key.char == q:
                qc +=1
                print('q counter is ', qc)
        if key.char == w:
                wc +=1
                print('q counter is ', wc)
        if key.char == e:
                ec +=1
                print('q counter is ', ec)
        if key.char == r:
                rc +=1
                print('q counter is ', rc)
        if key.char == t:
                tc +=1
                print('q counter is ', tc)
        if key.char == y:
                yc +=1
                print('q counter is ', yc)
        if key.char == u:
                uc +=1
                print('q counter is ', uc)
        if key.char == i:
                ic +=1
                print('q counter is ', ic)
        if key.char == o:
                oc +=1
                print('q counter is ', oc)
        if key.char == p:
                pc +=1
                print('q counter is ', pc)
        if key.char == a:
                ac +=1
                print('q counter is ', ac)
        if key.char == s:
                sc +=1
                print('q counter is ', sc)
        if key.char == d:
                dc +=1
                print('q counter is ', dc)
        if key.char == f:
                fc +=1
                print('q counter is ', fc)
        if key.char == g:
                gc +=1
                print('q counter is ', gc)
        if key.char == h:
                hc +=1
                print('q counter is ', hc)
        if key.char == j:
                jc +=1
                print('q counter is ', jc)
        if key.char == k:
                kc +=1
                print('q counter is ', kc)
        if key.char == l:
                lc +=1
                print('q counter is ', lc)
        if key.char == z:
                zc +=1
                print('q counter is ', zc)
        if key.char == x:
                xc +=1
                print('q counter is ', xc)
        if key.char == c:
                cc +=1
                print('q counter is ', cc)
        if key.char == v:
                vc +=1
                print('q counter is ', vc)
        if key.char == b:
                bc +=1
                print('q counter is ', bc)
        if key.char == n:
                nc +=1
                print('q counter is ', nc)
        if key.char == m:
                mc +=1
                print('q counter is ', mc)
       

   
#     print('{0} pressed'.format(
#         key))
        
with Listener( on_click=on_click, on_press=on_press) as listener:
    listener.join()