size = 5
boxsize = 10

for i in range(size):
    for j in range(size):
        land = (i & j) * boxsize * 2
        for l in range(0, 2):
            for m in range(0, 2):
                for n in range(0, 2):
                    ll = ((2 * l) - 1) * boxsize + i * boxsize + boxsize
                    mm = ((2 * m) - 1) * boxsize + j * boxsize + boxsize
                    landland = land * n
                    print(f"{ll}, {mm}, {landland}")
                    # Add conditions to print faces
                    if l == 0:
                        print(f"{ll - boxsize}, {mm}, {landland} {ll}, {mm}, {landland}")
                    if m == 0:
                        print(f"{ll}, {mm - boxsize}, {landland} {ll}, {mm}, {landland}")
                    if n == 0:
                        print(f"{ll}, {mm}, {landland - boxsize} s{ll}, {mm}, {landland}")
