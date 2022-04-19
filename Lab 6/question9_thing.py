def thing(x, y):
    z = 0
    k = 0
    for i in range(len(x)):
        if x[i] == -y[i]:
            z += x[i]
            k += 1
    print("k =", k, "z =", z)

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [1,2,3,4,5,6,7,-8,-9,10,-11,-12]
thing(x, y)