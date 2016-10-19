import numpy as np
import h5py as h5
import time

def makeArray(shape):

    return np.random.rand(*shape)


def plainSave(arr, filename):
    f = open(filename, "w")

    for row in arr:
        line = " ".join([str(x) for x in row])
        line += "\n"
        f.write(line)

    f.close()

def numpySave(arr, filename):
    np.savetxt(filename, arr)

def hdf5Save(arr, filename):

    f = h5.File(filename, "w")

    dset = f.create_dataset("array", arr.shape, dtype=np.float)
    dset[...] = arr

    f.close()

def plainLoad(filename):
    f = open(filename, "r")

    arr = []
    for line in f:
        words = line.split()
        row = [float(x) for x in words]
        arr.append(row)
    f.close()

    a = np.array(arr)

    return a

def numpyLoad(filename):
    a = np.loadtxt(filename)
    return a

def hdf5Load(filename):

    f = h5.File(filename, "r")

    arr = f['array'][...]

    f.close()

    return arr

if __name__ == "__main__":

    shape = (1000,1000)
    a = makeArray(shape)

    t1 = time.time()
    numpySave(a, "numpy.txt")
    b = numpyLoad("numpy.txt")
    t2 = time.time()

    print(  np.abs(b-a).max() )

    t3 = time.time()
    plainSave(a, "plain.txt")
    c = plainLoad("plain.txt")
    t4 = time.time()

    print(  np.abs(c-a).max() )
    
    t5 = time.time()
    hdf5Save(a, "data.h5")
    d = hdf5Load("data.h5")
    t6 = time.time()

    print(  np.abs(d-a).max() )

    print("Numpy: ", t2-t1)
    print("Python: ", t4-t3)
    print("HDF5: ", t6-t5)

