import numpy as np

a = np.ndarray(shape=(1, 3, 2, 4), dtype=float, order='F')

#OutputFile = open('%s.txt' %("ndarray"), 'wb')
#np.savetxt(OutputFile, a, fmt='%.5f')

print(a[(0, 2, 1, 3)])
print(a)
c = 233
d = str(c)
OutputFile = open(d + '.txt', 'w')

List = []
print(a.shape[0])
print(a.shape[1])
print(a.shape[2])
print(a.shape[3])

for y in range(0, a.shape[1]):
    print('y=');
    print(y)
    for z in range(0, a.shape[2]):
        print('z=');
        print(z)
        for w in range(0, a.shape[3]):
            print('w=');
            print(w)
            b = a[(0, y, z, w)]
            List.append(b)


OutputFile.write(str(List))
OutputFile.close()
print(len(List))
print(a)

