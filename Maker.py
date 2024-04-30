import sys
funkey=sys.argv[1]
size = 4
halfBox=5
boxsize = halfBox*2

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


funcs={'p':b_p,'or':b_or, 'not':b_not_ex, 'and':b_and, 'if':b_if, 'iff':b_iff,'notiff':b_notiff}
func={b_or}
for i in range(size):
    for j in range(size):
        fun = funcs[funkey](i,j)*boxsize
        for z in range(0,2):
            for y in range(0,2):
                  for x in range(0,2):   
                    ll = ((2*y)-1)* halfBox+ i  * boxsize + halfBox
                    mm = ((2*x)-1) * halfBox + j * boxsize + halfBox               
                    landland = fun * z + boxsize
                    print(f"v {ll} {mm} {landland}")
for k in range(verts):
    
    print(f'''
f {k*8+1} {k*8+2} {k*8+4} {k*8+3} 
f {k*8+5} {k*8+6} {k*8+8} {k*8+7} 
f {k*8+1} {k*8+3} {k*8+7} {k*8+5} 
f {k*8+2} {k*8+4} {k*8+8} {k*8+6}  
f {k*8+1} {k*8+2} {k*8+6} {k*8+5} 
f {k*8+3} {k*8+4} {k*8+8} {k*8+7} 
''')          
        