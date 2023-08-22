import numpy as np

# print(np.zeros((3,3), dtype="int16"))
# print(np.ones((3,3), dtype="int16"))
# print(np.full((3,3), 99))
x = np.arange(6, dtype=int)


# print(np.full_like(x, 9))
# # print(np.random.rand(2,3,4))
# print(np.identity(1))

# output = np.ones((5,5))
# print(output)

# z = np.zeros((3,3))
# z[1,1] = 9
# print(z)

# output[1:4, 1:4] = z
# print(output)


# a = np.array([1,2,3,4])

# a+= 2

# print(np.sin(a))

# a = np.full((2,3), 5)
# b = np.full((3,5), 7)

# mul = np.matmul(a,b)
# # print(np.linalg.det(mul)) 

matrix = np.array([1,2,3],
                  [3,4,7],
                  [9,0,7]
                  )

# print(np.linalg.ref(matrix))


