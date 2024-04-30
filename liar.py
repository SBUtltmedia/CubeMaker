from __future__ import division
GRID_SIZE=64;
MAX_ITERATIONS=64

def liar(P):
	return 1-abs((1-P)-P)
for i in range(GRID_SIZE):
	for j in range(GRID_SIZE):
		P=i/GRID_SIZE
		Q=j/GRID_SIZE
		for k in range(MAX_ITERATIONS):
			if P>.5 and  Q>.5:
				break
			
			P=liar(P)
			Q=liar(Q)
		 	#print(P,Q)	
		print("%d %d %d" %(i,j,k))	
