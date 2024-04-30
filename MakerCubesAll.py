import sys
funkey=sys.argv[2]
size = int(sys.argv[1])
halfBox=5
boxsize = halfBox*2
FunSet = []


verts=size*size
def b_or(p,q):
    return p|q
def b_p(p,q):
    return p
def b_not(p):
    return size-1-p
def b_not_ex(p,q):
    return b_not(p)
def b_and(p,q):
    return b_not(b_or(b_not(p),b_not(q))) 
def b_if(p,q):
    return b_or(b_not(p),q)
def b_iff(p,q):
    return b_and(b_if(p,q),b_if(q,p))
def b_notiff(p,q):
    return (b_not(b_iff(p,q)))
def tee(p,q):
    return (b_or(p,b_not(p)))
def eet(p,q):
    return b_not(b_or(p,b_not(p)))
def makeNthCube(n):
    return f'''
f {n*8+1} {n*8+5} {n*8+7} {n*8+3}
f {n*8+4} {n*8+3} {n*8+7} {n*8+8}
f {n*8+8} {n*8+7} {n*8+5} {n*8+6}
f {n*8+6} {n*8+2} {n*8+4} {n*8+8}
f {n*8+2} {n*8+1} {n*8+3} {n*8+4}
f {n*8+6} {n*8+5} {n*8+1} {n*8+2}
'''

funcs={'p':b_p,'or':b_or, 'not':b_not_ex, 'and':b_and, 'if':b_if, 'iff':b_iff,'notiff':b_notiff,'tee':tee, 'eet':eet}
func={b_or}
boxCount=0
faces=""
for i in range(size):
    for j in range(size):
       for k in range(size):
        fun = funcs[funkey](i,j)
        if k == fun:
            for l in range(k+1):
                faces+=makeNthCube(boxCount)
                boxCount+=1
                for z in range(0,2):
                    for y in range(0,2):
                        for x in range(0,2):   
                            ll = ((2*y)-1) * halfBox + i  * boxsize + halfBox
                            mm = ((2*x)-1) * halfBox + j * boxsize + halfBox               
                            landland = l * boxsize+ z * boxsize
                            FunSet.append((ll,mm,landland))
                                #print(f"v {ll} {mm} {landland}")
for Verts in list(FunSet):
    
    print(f"v {Verts[0]} {Verts[1]} {Verts[2]}")

print(faces)  
 