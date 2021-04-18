import numpy as np

a = np.array([1,2,3,4])
a
#array([1, 2, 3, 4])
a.dtype
#dtype('int32')
a = np.array([1,2,"3",True])
a
#array(['1', '2', '3', 'True'], dtype='<U11')
a[0]
#'1'
a[1]
#'2'
a[1] = '123'
a
#array(['1', '123', '3', 'True'], dtype='<U11')
a[1] = 234
a
#array(['1', '234', '3', 'True'], dtype='<U11')
a = np.array([1,2,3,4,5,6,7,8,9])
a[2]
#3
a[[1,1,1,1,1,1,1,1,1]]
#array([2, 2, 2, 2, 2, 2, 2, 2, 2])
a[[1,1,1,1,1]]
#array([2, 2, 2, 2, 2])
a[[True,True,False,False,False,False,True,True,True]]
#array([1, 2, 7, 8, 9])
b = a.reshape(3,3)
b
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
b[1][2]
#6
b[1,2]
#6

########################################
a = np.array([1,2,3,4])
a
#array([1, 2, 3, 4])
a = np.array([1,2,3,4], 'float64')
a
#array([1., 2., 3., 4.])
np.sctypeDict
#{'?': <class 'numpy.bool_'>, 0: <class 'numpy.bool_'>, 'byte': <class 'numpy.int8'>, 'b': <class 'numpy.int8'>, 1: <class 'numpy.int8'>, 'ubyte': <class 'numpy.uint8'>, 'B': <class 'numpy.uint8'>, 2: <class 'numpy.uint8'>, 'short': <class 'numpy.int16'>, 'h': <class 'numpy.int16'>, 3: <class 'numpy.int16'>, 'ushort': <class 'numpy.uint16'>, 'H': <class 'numpy.uint16'>, 4: <class 'numpy.uint16'>, 'i': <class 'numpy.intc'>, 5: <class 'numpy.intc'>, 'uint': <class 'numpy.uint32'>, 'I': <class 'numpy.uintc'>, 6: <class 'numpy.uintc'>, 'intp': <class 'numpy.int64'>, 'p': <class 'numpy.int64'>, 9: <class 'numpy.int64'>, 'uintp': <class 'numpy.uint64'>, 'P': <class 'numpy.uint64'>, 10: <class 'numpy.uint64'>, 'long': <class 'numpy.int32'>, 'l': <class 'numpy.int32'>, 7: <class 'numpy.int32'>, 'L': <class 'numpy.uint32'>, 8: <class 'numpy.uint32'>, 'longlong': <class 'numpy.int64'>, 'q': <class 'numpy.int64'>, 'ulonglong': <class 'numpy.uint64'>, 'Q': <class 'numpy.uint64'>, 'half': <class 'numpy.float16'>, 'e': <class 'numpy.float16'>, 23: <class 'numpy.float16'>, 'f': <class 'numpy.float32'>, 11: <class 'numpy.float32'>, 'double': <class 'numpy.float64'>, 'd': <class 'numpy.float64'>, 12: <class 'numpy.float64'>, 'longdouble': <class 'numpy.longdouble'>, 'g': <class 'numpy.longdouble'>, 13: <class 'numpy.longdouble'>, 'cfloat': <class 'numpy.complex128'>, 'F': <class 'numpy.complex64'>, 14: <class 'numpy.complex64'>, 'cdouble': <class 'numpy.complex128'>, 'D': <class 'numpy.complex128'>, 15: <class 'numpy.complex128'>, 'clongdouble': <class 'numpy.clongdouble'>, 'G': <class 'numpy.clongdouble'>, 16: <class 'numpy.clongdouble'>, 'O': <class 'numpy.object_'>, 17: <class 'numpy.object_'>, 'S': <class 'numpy.bytes_'>, 18: <class 'numpy.bytes_'>, 'unicode': <class 'numpy.str_'>, 'U': <class 'numpy.str_'>, 19: <class 'numpy.str_'>, 'void': <class 'numpy.void'>, 'V': <class 'numpy.void'>, 20: <class 'numpy.void'>, 'M': <class 'numpy.datetime64'>, 21: <class 'numpy.datetime64'>, 'm': <class 'numpy.timedelta64'>, 22: <class 'numpy.timedelta64'>, 'bool8': <class 'numpy.bool_'>, 'b1': <class 'numpy.bool_'>, 'int64': <class 'numpy.int64'>, 'i8': <class 'numpy.int64'>, 'uint64': <class 'numpy.uint64'>, 'u8': <class 'numpy.uint64'>, 'float16': <class 'numpy.float16'>, 'f2': <class 'numpy.float16'>, 'float32': <class 'numpy.float32'>, 'f4': <class 'numpy.float32'>, 'float64': <class 'numpy.float64'>, 'f8': <class 'numpy.float64'>, 'complex64': <class 'numpy.complex64'>, 'c8': <class 'numpy.complex64'>, 'complex128': <class 'numpy.complex128'>, 'c16': <class 'numpy.complex128'>, 'object0': <class 'numpy.object_'>, 'bytes0': <class 'numpy.bytes_'>, 'str0': <class 'numpy.str_'>, 'void0': <class 'numpy.void'>, 'datetime64': <class 'numpy.datetime64'>, 'M8': <class 'numpy.datetime64'>, 'timedelta64': <class 'numpy.timedelta64'>, 'm8': <class 'numpy.timedelta64'>, 'Bytes0': <class 'numpy.bytes_'>, 'Datetime64': <class 'numpy.datetime64'>, 'Str0': <class 'numpy.str_'>, 'Uint64': <class 'numpy.uint64'>, 'int32': <class 'numpy.int32'>, 'i4': <class 'numpy.int32'>, 'uint32': <class 'numpy.uint32'>, 'u4': <class 'numpy.uint32'>, 'int16': <class 'numpy.int16'>, 'i2': <class 'numpy.int16'>, 'uint16': <class 'numpy.uint16'>, 'u2': <class 'numpy.uint16'>, 'int8': <class 'numpy.int8'>, 'i1': <class 'numpy.int8'>, 'uint8': <class 'numpy.uint8'>, 'u1': <class 'numpy.uint8'>, 'complex_': <class 'numpy.complex128'>, 'int0': <class 'numpy.int64'>, 'uint0': <class 'numpy.uint64'>, 'single': <class 'numpy.float32'>, 'csingle': <class 'numpy.complex64'>, 'singlecomplex': <class 'numpy.complex64'>, 'float_': <class 'numpy.float64'>, 'intc': <class 'numpy.intc'>, 'uintc': <class 'numpy.uintc'>, 'int_': <class 'numpy.int32'>, 'longfloat': <class 'numpy.longdouble'>, 'clongfloat': <class 'numpy.clongdouble'>, 'longcomplex': <class 'numpy.clongdouble'>, 'bool_': <class 'numpy.bool_'>, 'bytes_': <class 'numpy.bytes_'>, 'string_': <class 'numpy.bytes_'>, 'str_': <class 'numpy.str_'>, 'unicode_': <class 'numpy.str_'>, 'object_': <class 'numpy.object_'>, 'int': <class 'numpy.int32'>, 'float': <class 'numpy.float64'>, 'complex': <class 'numpy.complex128'>, 'bool': <class 'numpy.bool_'>, 'object': <class 'numpy.object_'>, 'str': <class 'numpy.str_'>, 'bytes': <class 'numpy.bytes_'>, 'a': <class 'numpy.bytes_'>}
a = np.array([1,2,3,4], 'uintc')
a
#array([1, 2, 3, 4], dtype=uint32)
a = np.array([1,2,3,4], 'str_')
a
#array(['1', '2', '3', '4'], dtype='<U1')
np.complex64(10)
#(10+0j)
np.int16(10.5)
#10
a = np.array([1,2,5000,1000], dtype='int8')
a
#array([   1,    2, -120,  -24], dtype=int8)
a = np.array([1,2,5000,1000])
a
#array([   1,    2, 5000, 1000])
np.complex64(a)
#array([1.e+00+0.j, 2.e+00+0.j, 5.e+03+0.j, 1.e+03+0.j], dtype=complex64)
a
#array([   1,    2, 5000, 1000])
b = np.complex64(a)
c = np.int32(b)
#<input>:1: ComplexWarning: Casting complex values to real discards the imaginary part
c
#array([   1,    2, 5000, 1000])
np.array((1,2,3))
#array([1, 2, 3])
np.array("Hello")
#array('Hello', dtype='<U5')
a = np.array([[1,2],[3,4],[5,6]])
a
#array([[1, 2],
#       [3, 4],
#       [5, 6]])
a = np.array([[1,2],[3,4],[5,6,7]])
#<input>:1: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
a = np.array([[[1,2],[3,4]],[[5,6,],[7,8]],[[9,10],[11,12]]])
a
#array([[[ 1,  2],
#        [ 3,  4]],
#       [[ 5,  6],
#        [ 7,  8]],
#       [[ 9, 10],
#        [11, 12]]])
a[0]
#array([[1, 2],
#       [3, 4]])
a[1]
#array([[5, 6],
#       [7, 8]])
a[2]
#array([[ 9, 10],
#       [11, 12]])
a[0,0]
#array([1, 2])
a[0,0,0]
#1

##########################################
import numpy as np
np.array([1,2,3])
#array([1, 2, 3])
np.array([0]*10)
#array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
np.array([1]*15)
#array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
np.array([x for x in range(10)])
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.empty(10)
#array([1.08290492e-311, 6.95216958e-310, 1.23318785e-320,             nan,
#       0.00000000e+000, 0.00000000e+000, 0.00000000e+000, 0.00000000e+000,
#       0.00000000e+000, 0.00000000e+000])
np.empty(10, dtype='int16')
#array([ 28271,  27745,   8202,   8224, -23104,  21377,    510,      0,
#            0,      0], dtype=int16)
np.empty((3,2), dtype='int16')
#array([[1, 0],
#       [2, 0],
#       [3, 0]], dtype=int16)
np.eye(4)
#array([[1., 0., 0., 0.],
#       [0., 1., 0., 0.],
#       [0., 0., 1., 0.],
#       [0., 0., 0., 1.]])
np.eye(4,2)
#array([[1., 0.],
#       [0., 1.],
#       [0., 0.],
#       [0., 0.]])
np.identity(5)
#array([[1., 0., 0., 0., 0.],
#       [0., 1., 0., 0., 0.],
#       [0., 0., 1., 0., 0.],
#       [0., 0., 0., 1., 0.],
#       [0., 0., 0., 0., 1.]])
np.zeros((2,3,4))
#array([[[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]],
#       [[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]]])
np.ones([4,3], dtype='int8')
#array([[1, 1, 1],
#       [1, 1, 1],
#       [1, 1, 1],
#       [1, 1, 1]], dtype=int8)
np.full((3,2), -1)
#array([[-1, -1],
#       [-1, -1],
#       [-1, -1]])
np.ones((4,3))
#array([[1., 1., 1.],
#       [1., 1., 1.],
#       [1., 1., 1.],
#       [1., 1., 1.]])
np.mat('1 2 3 4') #создает матрицу 1х4 из строки
#matrix([[1, 2, 3, 4]])
np.mat('1,2,3,4')
#matrix([[1, 2, 3, 4]])
np.mat('1,2;3,4')
#matrix([[1, 2],
#        [3, 4]])
np.mat([5,4,3])
#matrix([[5, 4, 3]])
np.mat([(1,2,3),(4,5,6)])
#matrix([[1, 2, 3],
#        [4, 5, 6]])
np.mat([(1,2,3),(4,5,6,7)])
#C:\Users\lenovo\PycharmProjects\Diploma\venv\lib\site-packages\numpy\matrixlib\defmatrix.py:145: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
#  arr = N.array(data, dtype=dtype, copy=copy)
#matrix([[(1, 2, 3), (4, 5, 6, 7)]], dtype=object)
np.diag([1,2,3])
#array([[1, 0, 0],
#       [0, 2, 0],
#       [0, 0, 3]])
np.diag([(1,2,3),(4,5,6),(7,8,9)])
#array([1, 5, 9])
np.diagflat([(1,2,3),(4,5,6),(7,8,9)])
#array([[1, 0, 0, 0, 0, 0, 0, 0, 0],
#       [0, 2, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 3, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 4, 0, 0, 0, 0, 0],
#       [0, 0, 0, 0, 5, 0, 0, 0, 0],
#       [0, 0, 0, 0, 0, 6, 0, 0, 0],
#       [0, 0, 0, 0, 0, 0, 7, 0, 0],
#       [0, 0, 0, 0, 0, 0, 0, 8, 0],
#       [0, 0, 0, 0, 0, 0, 0, 0, 9]])
np.tri(4)
#array([[1., 0., 0., 0.],
#       [1., 1., 0., 0.],
#       [1., 1., 1., 0.],
#       [1., 1., 1., 1.]])
np.tri(4,2)
#array([[1., 0.],
#       [1., 1.],
#       [1., 1.],
#       [1., 1.]])
np.tri(2,4)
#array([[1., 0., 0., 0.],
#       [1., 1., 0., 0.]])
a = np.array([(1,2,3),(4,5,6),(7,8,9)])
a
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
np.tril(a)
#array([[1, 0, 0],
#       [4, 5, 0],
#       [7, 8, 9]])
np.triu(a)
#array([[1, 2, 3],
#       [0, 5, 6],
#       [0, 0, 9]])
np.tril([1,2,3])
#array([[1, 0, 0],
#       [1, 2, 0],
#       [1, 2, 3]])
np.tril([[[1,2,3],[4,5,6],[7,8,9]]])
#array([[[1, 0, 0],
#        [4, 5, 0],
#        [7, 8, 9]]])
np.tril([[[1,2,3],[4,5,6],[7,8,9]],[[10,20,30],[40,50,60],[70,80,90]],[[100,200,300],[400,500,600],[700,800,900]]])
#array([[[  1,   0,   0],
#        [  4,   5,   0],
#        [  7,   8,   9]],
#       [[ 10,   0,   0],
#        [ 40,  50,   0],
#        [ 70,  80,  90]],
#       [[100,   0,   0],
#        [400, 500,   0],
#        [700, 800, 900]]])
np.vander([1,2,3])
#array([[1, 1, 1],
#       [4, 2, 1],
#       [9, 3, 1]])
np.arange(5)
#array([0, 1, 2, 3, 4])
np.arange(1,5)
#array([1, 2, 3, 4])
np.arange(1,5,0.5)
#array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])
np.arange(0,np.pi,0.1)
#array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2,
#       1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2. , 2.1, 2.2, 2.3, 2.4, 2.5,
#       2.6, 2.7, 2.8, 2.9, 3. , 3.1])
np.cos(np.arange(0,np.pi,0.1))
#array([ 1.        ,  0.99500417,  0.98006658,  0.95533649,  0.92106099,
#        0.87758256,  0.82533561,  0.76484219,  0.69670671,  0.62160997,
#        0.54030231,  0.45359612,  0.36235775,  0.26749883,  0.16996714,
#        0.0707372 , -0.02919952, -0.12884449, -0.22720209, -0.32328957,
#       -0.41614684, -0.5048461 , -0.58850112, -0.66627602, -0.73739372,
#       -0.80114362, -0.85688875, -0.90407214, -0.94222234, -0.97095817,
#       -0.9899925 , -0.99913515])
np.linspace(0, np.pi, 0)
#array([], dtype=float64)
np.linspace(0, np.pi, 1)
#array([0.])
np.linspace(0, np.pi, 2)
#array([0.        , 3.14159265])
np.linspace(0, np.pi, 3)
#array([0.        , 1.57079633, 3.14159265])
np.linspace(0, np.pi, 4)
#array([0.        , 1.04719755, 2.0943951 , 3.14159265])
np.linspace(0, np.pi, 5)
#array([0.        , 0.78539816, 1.57079633, 2.35619449, 3.14159265])
np.logspace(0,1,3)
#array([ 1.        ,  3.16227766, 10.        ])
np.logspace(0,1,4)
#array([ 1.        ,  2.15443469,  4.64158883, 10.        ])
np.geomspace(1,16,5)
#array([ 1.,  2.,  4.,  8., 16.])
a = np.array([(1,2),(3,4)])
a
#array([[1, 2],
#       [3, 4]])
b = np.copy(a)
b
#array([[1, 2],
#       [3, 4]])
b[0] = 100
b
#array([[100, 100],
#       [  3,   4]])
a
#array([[1, 2],
#       [3, 4]])
def getRange(x,y):
    return 100*x + y
a = np.fromfunction(getRange, (2,2))
a
#array([[  0.,   1.],
#       [100., 101.]])
np.fromfunction(lambda x, y: x*100+y, (2,2))
#array([[  0.,   1.],
#       [100., 101.]])
np.fromiter("hello", dtype='U1')
#array(['h', 'e', 'l', 'l', 'o'], dtype='<U1')
def getRange(N):
    for i in range(N):
        yield i


a = np.fromiter(getRange(4), dtype='int8')
a
#array([0, 1, 2, 3], dtype=int8)
np.fromstring('1 2 3', dtype='int16', sep= ' ')
#array([1, 2, 3], dtype=int16)
np.fromstring('1, 2, 3', dtype='int16', sep= ',')
#array([1, 2, 3], dtype=int16)

##########################################

a = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
a.dtype
#dtype('float64')
a.dtype = np.int8()
a
#array([-102, -103, -103, -103, -103, -103,  -71,   63, -102, -103, -103,
#       -103, -103, -103,  -55,   63,   51,   51,   51,   51,   51,   51,
#        -45,   63, -102, -103, -103, -103, -103, -103,  -39,   63,    0,
#          0,    0,    0,    0,    0,  -32,   63,   51,   51,   51,   51,
#         51,   51,  -29,   63,  102,  102,  102,  102,  102,  102,  -26,
#         63, -102, -103, -103, -103, -103, -103,  -23,   63,  -51,  -52,
#        -52,  -52,  -52,  -52,  -20,   63], dtype=int8)
a.size
#72
a.dtype = np.float64()
a
#array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
a.dtype = 'float32'
a
#array([-1.58818684e-23,  1.44999993e+00, -1.58818684e-23,  1.57499993e+00,
#        4.17232506e-08,  1.64999998e+00, -1.58818684e-23,  1.69999993e+00,
#        0.00000000e+00,  1.75000000e+00,  4.17232506e-08,  1.77499998e+00,
#        2.72008302e+23,  1.79999995e+00, -1.58818684e-23,  1.82499993e+00,
#       -1.07374184e+08,  1.84999990e+00], dtype=float32)
a.size
#18
a.itemsize
#4
a.dtype = 'float64'
a.itemsize
#8
a.size*a.itemsize
#72
b = np.ones((3,4,5))
b
#array([[[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]],
#       [[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]],
#       [[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]]])
b.ndim
#3
b.shape
#(3, 4, 5)
b.shape = 60
b
#array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
#       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
#       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
#       1., 1., 1., 1., 1., 1., 1., 1., 1.])
b.shape = 12,5
b
#array([[1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.]])
c = b.reshape(3,2,10)
c
#array([[[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]],
#       [[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]],
#       [[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]]])
b
#array([[1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.],
#       [1., 1., 1., 1., 1.]])
b[0,0] = 10
b
#array([[10.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.]])
c
#array([[[10.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]],
#       [[ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]],
#       [[ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]]])
print(id(b), id(c))
#2192252986064 2191876781520
d = b.T
d
#array([[10.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]])
b
#array([[10.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.]])
a = np.array([1,2,3,4,5,6,7,8,9])
b = a
a.shape = 3,3
b
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
a = np.array([1,2,3,4,5,6,7,8,9])
b = a.view()
b
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a.shape = 3,3
a
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
b
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a = np.array([1,2,3,4,5,6,7,8,9])
b = np.array(a)
b
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a[0] = 100
a
#array([100,   2,   3,   4,   5,   6,   7,   8,   9])
b
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])
c = a.copy()
c
#array([100,   2,   3,   4,   5,   6,   7,   8,   9])
c[0] = 1
c
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a
#array([100,   2,   3,   4,   5,   6,   7,   8,   9])

##########################################
a = np.arange(10)
a
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a.shape = 2,5
a
#array([[0, 1, 2, 3, 4],
#       [5, 6, 7, 8, 9]])
b = a.reshape(10)
b
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a
#array([[0, 1, 2, 3, 4],
#       [5, 6, 7, 8, 9]])
b[0]=-1
b
#array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9])
a
#array([[-1,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9]])
b = a.reshape(9)
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#ValueError: cannot reshape array of size 10 into shape (9,)
a.shepe = 3,3
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#AttributeError: 'numpy.ndarray' object has no attribute 'shepe'
a.shape = -1, 2
a
#array([[-1,  1],
#       [ 2,  3],
#       [ 4,  5],
#       [ 6,  7],
#       [ 8,  9]])
a.shape = -1,5
a
#array([[-1,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9]])
b.reshape(-1,1)
#array([[-1],
#       [ 1],
#       [ 2],
#       [ 3],
#       [ 4],
#       [ 5],
#       [ 6],
#       [ 7],
#       [ 8],
#       [ 9]])
b.reshape(1,-1)
#array([[-1,  1,  2,  3,  4,  5,  6,  7,  8,  9]])
b
#array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9])
a
#array([[-1,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9]])
a.ravel()
#array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9])
c = a.ravel()
c
#array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9])
a
#array([[-1,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9]])
a.shape = -1
a
#array([-1,  1,  2,  3,  4,  5,  6,  7,  8,  9])
a.resize(2,5)
a
#array([[-1,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  9]])
a.resize(3,3)
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#ValueError: cannot resize an array that references or is referenced
#by another array in this way.
#Use the np.resize function or refcheck=False
a.resize(3,3, refcheck=False)
a
#array([[-1,  1,  2],
#       [ 3,  4,  5],
#       [ 6,  7,  8]])
a.resize(4,5, refcheck=False)
a
#array([[-1,  1,  2,  3,  4],
#       [ 5,  6,  7,  8,  0],
#       [ 0,  0,  0,  0,  0],
#       [ 0,  0,  0,  0,  0]])
a = np.array([(1,2,3),(4,5,6),(7,8,9)])
a
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
b = a.T
b
#array([[1, 4, 7],
#       [2, 5, 8],
#       [3, 6, 9]])
x = np.arange(1,10)
x
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x.T
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x.shape = 1,-1
x
#array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
x.T
#array([[1],
#       [2],
#       [3],
#       [4],
#       [5],
#       [6],
#       [7],
#       [8],
#       [9]])
x_test = np.arange(32).reshape(8,2,2)
x_test
#array([[[ 0,  1],
#        [ 2,  3]],
#       [[ 4,  5],
#        [ 6,  7]],
#       [[ 8,  9],
#        [10, 11]],
#       [[12, 13],
#        [14, 15]],
#       [[16, 17],
#        [18, 19]],
#       [[20, 21],
#        [22, 23]],
#       [[24, 25],
#        [26, 27]],
#       [[28, 29],
#        [30, 31]]])
x_test.shape
#(8, 2, 2)
x_test4.shape
#(1, 8, 2, 2)
x_test4
#array([[[[ 0,  1],
#         [ 2,  3]],
#        [[ 4,  5],
#         [ 6,  7]],
#        [[ 8,  9],
#         [10, 11]],
#        [[12, 13],
#         [14, 15]],
#        [[16, 17],
#         [18, 19]],
#        [[20, 21],
#         [22, 23]],
#        [[24, 25],
#         [26, 27]],
#        [[28, 29],
#         [30, 31]]]])
x_test4[0,0,0,0] = -100
x_test4
#array([[[[-100,    1],
#         [   2,    3]],
#        [[   4,    5],
#         [   6,    7]],
#        [[   8,    9],
#         [  10,   11]],
#        [[  12,   13],
#         [  14,   15]],
#        [[  16,   17],
#         [  18,   19]],
#        [[  20,   21],
#         [  22,   23]],
#        [[  24,   25],
#         [  26,   27]],
#        [[  28,   29],
#         [  30,   31]]]])
x_test4.shape
#(1, 8, 2, 2)
a = np.append(x_test4, x_test4, axis=0)
a.shape
#(2, 8, 2, 2)
b = np.delete(a, 0, axis=0)
b.shape
#(1, 8, 2, 2)
b = np.expand_dims(x_test4,axis=-1)
b.shape
#(1, 8, 2, 2, 1)
c = np.squeeze(b)
c.shape
#(8, 2, 2)
c = np.squeeze(b, axis=0)
c.shape
#(8, 2, 2, 1)
c = np.squeeze(b, axis=1)
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#  File "<__array_function__ internals>", line 5, in squeeze
#  File "C:\Users\lenovo\PycharmProjects\Diploma\venv\lib\site-packages\numpy\core\fromnumeric.py", line 1506, in squeeze
#    return squeeze(axis=axis)
#ValueError: cannot select an axis to squeeze out which has size not equal to one
a = np.arange(1,10)
a
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a[np.newaxis, :]
b.shape
#(1, 9)
b
#array([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
b = a[:, np.newaxis]
b.shape
#(9, 1)
b
#array([[1],
#       [2],
#       [3],
#       [4],
#       [5],
#       [6],
#       [7],
#       [8],
#       [9]])
c = a[np.newaxis, :, np.newaxis]
c.shape
#(1, 9, 1)
c
#array([[[1],
#        [2],
#        [3],
#        [4],
#        [5],
#        [6],
#        [7],
#        [8],
#        [9]]])

##########################################
a = np.array([(1,2),(3,4)])
b = np.array([(5,6),(7,8)])
a
#array([[1, 2],
#       [3, 4]])
b
#array([[5, 6],
#       [7, 8]])
np.hstack([a,b])
#array([[1, 2, 5, 6],
#       [3, 4, 7, 8]])
np.vstack([a,b])
#array([[1, 2],
#       [3, 4],
#       [5, 6],
#       [7, 8]])
np.vstack([b,a])
#array([[5, 6],
#       [7, 8],
#       [1, 2],
#       [3, 4]])
np.vstack([b,a,a])
#array([[5, 6],
#       [7, 8],
#       [1, 2],
#       [3, 4],
#       [1, 2],
#       [3, 4]])
a = np.fromiter(range(18), dtype='int32')
b = np.fromiter(range(18,36), dtype='int32')
a.resize(3,3,2)
b.resize(3,3,2)
a
#array([[[ 0,  1],
#        [ 2,  3],
#        [ 4,  5]],
#       [[ 6,  7],
#        [ 8,  9],
#        [10, 11]],
#       [[12, 13],
#        [14, 15],
#        [16, 17]]])
b
#array([[[18, 19],
#        [20, 21],
#        [22, 23]],
#       [[24, 25],
#        [26, 27],
#        [28, 29]],
#       [[30, 31],
#        [32, 33],
#        [34, 35]]])
c = np.hstack([a,b])
c
#array([[[ 0,  1],
#        [ 2,  3],
#        [ 4,  5],
#        [18, 19],
#        [20, 21],
#        [22, 23]],
#       [[ 6,  7],
#        [ 8,  9],
#        [10, 11],
#        [24, 25],
#        [26, 27],
#        [28, 29]],
#       [[12, 13],
#        [14, 15],
#        [16, 17],
#        [30, 31],
#        [32, 33],
#        [34, 35]]])
c.shape
#(3, 6, 2)
d = np.vstack([a,b])
d.shape
#(6, 3, 2)
a = np.fromstring('1 2 3 4', sep = ' ')
b = np.fromstring('5 6 7 8', sep = ' ')
a
#array([1., 2., 3., 4.])
b
#array([5., 6., 7., 8.])
np.hstack([a,b])
#array([1., 2., 3., 4., 5., 6., 7., 8.])
np.vstack([a,b])
#array([[1., 2., 3., 4.],
#       [5., 6., 7., 8.]])
a
#array([1., 2., 3., 4.])
b
#array([5., 6., 7., 8.])
np.column_stack([a,b])
#array([[1., 5.],
#       [2., 6.],
#       [3., 7.],
#       [4., 8.]])
np.row_stack([a,b])
#array([[1., 2., 3., 4.],
#       [5., 6., 7., 8.]])
a = np.arange(1,13)
b = np.arange(13,26)
a.resize(3,3,2)
b.resize(3,3,2)
c0 = np.concatenate([a,b], axis=0)
c1 = np.concatenate([a,b], axis=1)
c2 = np.concatenate([a,b], axis=2)
c0.shape
#(6, 3, 2)
c1.shape
#(3, 6, 2)
c2.shape
#(3, 3, 4)
np.r_[[1,2,3],4,5]
#array([1, 2, 3, 4, 5])
np.r_[1:9,90,100]
#array([  1,   2,   3,   4,   5,   6,   7,   8,  90, 100])
np.r_[np.array([1,2,3]), np.array([4,5,6])]
#array([1, 2, 3, 4, 5, 6])
np.r_[[(1,2,3),(4,5,6)],[(7,8,9)]]
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
np.c_[1:5]
#array([[1],
#       [2],
#       [3],
#       [4]])
np.r_[1:5]
#array([1, 2, 3, 4])
np.c_[1:5]
#array([[1],
#       [2],
#       [3],
#       [4]])
np.c_[[1,2,3],[4,5,6]]
#array([[1, 4],
#       [2, 5],
#       [3, 6]])
np.c_[[(1,2,3),(4,5,6)],[[7],[8]]]
#array([[1, 2, 3, 7],
#       [4, 5, 6, 8]])
a = np.arange(10)
a
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np.hsplit(a,2)
#[array([0, 1, 2, 3, 4]), array([5, 6, 7, 8, 9])]
np.hsplit(a,3)
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#  File "<__array_function__ internals>", line 5, in hsplit
#  File "C:\Users\lenovo\PycharmProjects\Diploma\venv\lib\site-packages\numpy\lib\shape_base.py", line 942, in hsplit
#    return split(ary, indices_or_sections, 0)
#  File "<__array_function__ internals>", line 5, in split
#  File "C:\Users\lenovo\PycharmProjects\Diploma\venv\lib\site-packages\numpy\lib\shape_base.py", line 872, in split
#    raise ValueError(
#ValueError: array split does not result in an equal division
np.hsplit(a,5)
#[array([0, 1]), array([2, 3]), array([4, 5]), array([6, 7]), array([8, 9])]
np.vsplit(a,2)
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#  File "<__array_function__ internals>", line 5, in vsplit
#  File "C:\Users\lenovo\PycharmProjects\Diploma\venv\lib\site-packages\numpy\lib\shape_base.py", line 990, in vsplit
#    raise ValueError('vsplit only works on arrays of 2 or more dimensions')
#ValueError: vsplit only works on arrays of 2 or more dimensions
a.shape
(10,)
#a.shape = 10,-1
a.shape
#(10, 1)
a
#array([[0],
#       [1],
#       [2],
#       [3],
#       [4],
#       [5],
#       [6],
#       [7],
#       [8],
#       [9]])
np.vsplit(a,2)
#[array([[0],
#       [1],
#       [2],
#       [3],
#       [4]]), array([[5],
#       [6],
#       [7],
#       [8],
#       [9]])]
a = np.arange(12)
a.resize(2,6)
a
#array([[ 0,  1,  2,  3,  4,  5],
#       [ 6,  7,  8,  9, 10, 11]])
np.hsplit(a,2)
#[array([[0, 1, 2],
#       [6, 7, 8]]), array([[ 3,  4,  5],
#       [ 9, 10, 11]])]
np.vsplit(a,2)
#[array([[0, 1, 2, 3, 4, 5]]), array([[ 6,  7,  8,  9, 10, 11]])]
a = np.arange(18)
a.resize(3,3,2)
a
#array([[[ 0,  1],
#        [ 2,  3],
#        [ 4,  5]],
#       [[ 6,  7],
#        [ 8,  9],
#        [10, 11]],
#       [[12, 13],
#        [14, 15],
#        [16, 17]]])
np.array_split(a,2,axis=2)
#[array([[[ 0],
#        [ 2],
#        [ 4]],
#       [[ 6],
#        [ 8],
#        [10]],
#       [[12],
#        [14],
#        [16]]]), array([[[ 1],
#        [ 3],
#        [ 5]],
#       [[ 7],
#        [ 9],
#        [11]],
#       [[13],
#        [15],
#        [17]]])]
np.array_split(a,2,axis=0)
#[array([[[ 0,  1],
#        [ 2,  3],
#        [ 4,  5]],
#       [[ 6,  7],
#        [ 8,  9],
#        [10, 11]]]), array([[[12, 13],
#        [14, 15],
#        [16, 17]]])]
np.array_split(a,2,axis=1)
#[array([[[ 0,  1],
#        [ 2,  3]],
#       [[ 6,  7],
#        [ 8,  9]],
#       [[12, 13],
#        [14, 15]]]), array([[[ 4,  5]],
#       [[10, 11]],
#       [[16, 17]]])]

###############################

a = np.arange(12)
a
#array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
a[2]
#2
a[0]
#0
a[-1]
#11
a[-2]
#10
a[12]
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#IndexError: index 12 is out of bounds for axis 0 with size 12
a[0]=100
a
#array([100,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11])
b = a[2:4]
b
#array([2, 3])
b[0]=-100
b
#array([-100,    3])
a
#array([ 100,    1, -100,    3,    4,    5,    6,    7,    8,    9,   10,
#         11])
a[3:]
#array([ 3,  4,  5,  6,  7,  8,  9, 10, 11])
a[:5]
#array([ 100,    1, -100,    3,    4])
a[-5:-1]
#array([ 7,  8,  9, 10])
a[:]
#array([ 100,    1, -100,    3,    4,    5,    6,    7,    8,    9,   10,
#         11])
a[1:6:2]
#array([1, 3, 5])
a[::2]
#array([ 100, -100,    4,    6,    8,   10])
a[::-1]
#array([  11,   10,    9,    8,    7,    6,    5,    4,    3, -100,    1,
#        100])
a[:4] = [-1,-2,-3,-4]
a
#array([-1, -2, -3, -4,  4,  5,  6,  7,  8,  9, 10, 11])
a[4::2]=np.array([10,20,30,40])
a
#array([-1, -2, -3, -4, 10,  5, 20,  7, 30,  9, 40, 11])
for x in a:
    print(x, sep=' ', end=' ')

#-1 - 2 - 3 - 4
#10
#5
#20
#7
#30
#9
#40
#11
x = np.array([(1,2,3),(10,20,30),(100,200,300)])
x
#array([[  1,   2,   3],
#       [ 10,  20,  30],
#       [100, 200, 300]])
x[1,1]
#20
x[-1,-1]
#300
x[0]
#array([1, 2, 3])
x[1]
#array([10, 20, 30])
x[0,:]
#array([1, 2, 3])
x[:,1]
#array([  2,  20, 200])
for row in x:
    for val in row:
        print(val, end=' ')
    print()

#1
#2
#3
#10
#20
#30
#100
#200
#300
for val in x.flat:
    print(val, end=' ')

#1
#2
#3
#10
#20
#30
#100
#200
#300
a = np.arange(1,82).reshape(3,3,3,3)
a[1,2,0,1]
#47
a[:,1,:,:]
#array([[[10, 11, 12],
#        [13, 14, 15],
#        [16, 17, 18]],
#       [[37, 38, 39],
#        [40, 41, 42],
#        [43, 44, 45]],
#       [[64, 65, 66],
#        [67, 68, 69],
#        [70, 71, 72]]])
a[0,0]
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
a[0,0,:,:]
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])
a[:,:,1,1]
#array([[ 5, 14, 23],
#       [32, 41, 50],
#       [59, 68, 77]])
a[0:2,0:2,1,1]
#array([[ 5, 14],
#       [32, 41]])
a[...,1,1]
#array([[ 5, 14, 23],
#       [32, 41, 50],
#       [59, 68, 77]])
a = np.arange(1,9)
a
#array([1, 2, 3, 4, 5, 6, 7, 8])
a[0]
#1
a[[0]]
#array([1])
b = a[[0]]
b[0]=100
b
#array([100])
a
#array([1, 2, 3, 4, 5, 6, 7, 8])
a[[0,1,7,5]]
#array([1, 2, 8, 6])
a[[0,0,1,1,1,2,3,4,5,6,7]]
#array([1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8])
indx = np.array([0,0,1,1,1,2])
a[indx]
#array([1, 1, 2, 2, 2, 3])
bindx = [True,True,False,False,False,True,False,False]
#a[bindx]
#array([1, 2, 6])
i = a > 5
i
#array([False, False, False, False, False,  True,  True,  True])
a[i]
#array([6, 7, 8])
a[a > 5]
#array([6, 7, 8])
a = np.arange(1,9)
a
#array([1, 2, 3, 4, 5, 6, 7, 8])
i = np.array([[0,1],[2,3]])
i
#array([[0, 1],
#       [2, 3]])
a[i]
#array([[1, 2],
#       [3, 4]])
i = [[0,1],[2,3]]
a[i]
#<input>:1: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
a = np.arange(1,13).reshape(3,4)
a
#array([[ 1,  2,  3,  4],
#       [ 5,  6,  7,  8],
#       [ 9, 10, 11, 12]])
indx = [2,1,0]
a[indx]
#array([[ 9, 10, 11, 12],
#       [ 5,  6,  7,  8],
#       [ 1,  2,  3,  4]])
indx = np.array([[1,0],[2,1]])
indx
#array([[1, 0],
#       [2, 1]])
a[indx]
#array([[[ 5,  6,  7,  8],
#        [ 1,  2,  3,  4]],
#       [[ 9, 10, 11, 12],
#        [ 5,  6,  7,  8]]])
i0 = [0,1]
i1 = [1,2]
a[i0,i1]
#array([2, 7])
a[:,i1]
#array([[ 2,  3],
#       [ 6,  7],
#       [10, 11]])
a[i0,1]
#array([2, 6])
a = np.arange(7)
a
#array([0, 1, 2, 3, 4, 5, 6])
a[[0,4,6]]=[-1,-2,-3]
a
#array([-1,  1,  2,  3, -2,  5, -3])
a[[0,0,0,1]]=[1,2,3,100]
a
#array([  3, 100,   2,   3,  -2,   5,  -3])
a[[0,0,0]]=a[[0,0,0]] + 3
a
#array([  6, 100,   2,   3,  -2,   5,  -3])
a[[0,0,1,2]] +=1
a
#array([  7, 101,   3,   3,  -2,   5,  -3])

#############################################