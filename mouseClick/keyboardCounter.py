from pynput.keyboard import Key, Listener, KeyCode
import logging



logging.basicConfig(filename=("key_log6.txt"), level=logging.DEBUG, format=' %(message)s')



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
spacec=[]
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
                       # logging.info('q={0}'.format(qc))
                if key.char == w:
                        wc +=1
                        total +=1
                        #logging.info('w={0}'.format(wc))
                if key.char == e:
                        ec +=1
                        total +=1
                       # logging.info('e={0}'.format(ec))
                if key.char == r:
                        rc +=1
                        total +=1
                        #logging.info('r={0}'.format(rc))
                if key.char == t:
                        tc +=1
                        total +=1
                      #  logging.info('t={0}'.format(tc))
                if key.char == y:
                        yc +=1
                        total +=1
                      #  logging.info('y={0}'.format(yc))
                if key.char == u:
                        uc +=1
                        total +=1
                        #logging.info('u={0}'.format(uc))
                if key.char == i:
                        ic +=1
                        total +=1
                        #logging.info('i={0}'.format(ic))
                if key.char == o:
                        oc +=1
                        total +=1
                       # logging.info('o={0}'.format(oc))
                if key.char == p:
                        pc +=1
                        total +=1
                       # logging.info('p={0}'.format(pc))
                if key.char == a:
                        ac +=1
                        total +=1
                        #logging.info('a={0}'.format(ac))
                if key.char == s:
                        sc +=1
                        total +=1
                       # logging.info('s={0}'.format(sc))
                if key.char == d:
                        dc +=1
                        total +=1
                       # logging.info('d={0}'.format(dc))
                if key.char == f:
                        fc +=1
                        total +=1
                       # logging.info('f={0}'.format(fc))
                if key.char == g:
                        gc +=1
                        total +=1
                       # logging.info('g={0}'.format(gc))
                if key.char == h:
                        hc +=1
                        total +=1
                       # logging.info('h={0}'.format(hc))
                if key.char == j:
                        jc +=1
                        total +=1
                       # logging.info('j={0}'.format(jc))
                if key.char == k:
                        kc +=1
                        total +=1
                       # logging.info('k={0}'.format(kc))
                if key.char == l:
                        lc +=1
                        total +=1
                       # logging.info('l={0}'.format(lc))
                if key.char == z:
                        zc +=1
                        total +=1
                       # logging.info('z={0}'.format(zc))
                if key.char == x:
                        xc +=1
                        total +=1
                       # logging.info('x={0}'.format(xc))
                if key.char == c:
                        cc +=1
                        total +=1
                        #logging.info('c={0}'.format(cc))
                if key.char == v:
                        vc +=1
                        total +=1
                        #logging.info('v={0}'.format(vc))
                if key.char == b:
                        bc += 1
                        total +=1
                       # logging.info('b={0}'.format(bc))
                if key.char == n:
                        nc +=1
                        total +=1
                        #logging.info('n={0}'.format(nc))
                if key.char == m:
                        mc +=1
                        total +=1
                        # logging.info(total)
                      #  logging.info('m={0}'.format(mc))
        except AttributeError:
                if Key.ctrl_r:
                        spacec = [qc,wc,ec,rc,tc,yc,uc,ic,oc,pc,ac,sc,dc,fc,gc,hc,jc,kc,lc,zc,xc,cc,vc,bc,nc,mc]
                        # logging.info('spacec={0}'.format(spacec[1]))
                        logging.info('q={0}'.format(spacec[0]))
                        logging.info('w={0}'.format(spacec[1]))
                        logging.info('e={0}'.format(spacec[2]))
                        logging.info('r={0}'.format(spacec[3]))
                        logging.info('t={0}'.format(spacec[4]))
                        logging.info('y={0}'.format(spacec[5]))
                        logging.info('u={0}'.format(spacec[6]))
                        logging.info('i={0}'.format(spacec[7]))
                        logging.info('o={0}'.format(spacec[8]))
                        logging.info('p={0}'.format(spacec[9]))
                        logging.info('a={0}'.format(spacec[10]))
                        logging.info('s={0}'.format(spacec[11]))
                        logging.info('d={0}'.format(spacec[12]))
                        logging.info('f={0}'.format(spacec[13]))
                        logging.info('g={0}'.format(spacec[14]))
                        logging.info('h={0}'.format(spacec[15]))
                        logging.info('j={0}'.format(spacec[16]))
                        logging.info('k={0}'.format(spacec[17]))
                        logging.info('l={0}'.format(spacec[18]))
                        logging.info('z={0}'.format(spacec[19]))
                        logging.info('x={0}'.format(spacec[20]))
                        logging.info('c={0}'.format(spacec[21]))
                        logging.info('v={0}'.format(spacec[22]))
                        logging.info('b={0}'.format(spacec[23]))
                        logging.info('n={0}'.format(spacec[24]))
                        logging.info('m={0}'.format(spacec[25]))
        
                # if Key.space:
                #         spacec +=1
                #         logging.info('space' , spacec)
                # logging.info('special key {0} pressed'.format(
                # key))


with Listener( on_press=on_press) as listener:
    listener.join() 

