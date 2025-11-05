import numpy as np

# bool -> int -> float -> string
arr = np.array([1, 2, 3, 4, 5]) # kalo di kode C ke bawah, diubah jadi objek
arr2 = np.array((6, 7, 8, 9, 10)) # tuple
print("array 1: ", arr)
print("array 1 * 2", arr * 2)
print("array 1 dtype: ", arr.dtype)

avg = np.mean(arr)
sum = np.sum(arr)
print("average array: ", avg)
print("sum array: ", sum)

print("array index:", arr[1])
print("array slicing:", arr[2:5])
print("array index sum:", arr[1] + arr[3])

arr_dt = np.array([1, 2, 3, 4, 5], dtype="U")
print(arr_dt)

# print(arr2)
# print(type(arr))
# print(type(arr2))

list = [1, 2, 3, 4, 5]
print(list)
print(type(list))

# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
d0_arr = np.array(42)
print(d0_arr)

# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
d1_arr = np.array([1, 2, 3, 4, 5]) # satu baris
print("one dimension:", d1_arr)

# An array that has 1-D arrays as its elements is called a 2-D array.
d2_arr = np.array([[1, 2, 3], [4, 5, 6]]) # baris x kolom
print("\ntwo dimension:\n", d2_arr)

# An array that has 2-D arrays (matrices) as its elements is called 3-D array.
d3_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) # lapisan x baris x kolom
print("\nthree dimension:\n", d3_arr)

print(d0_arr.ndim)
print(d1_arr.ndim)
print(d2_arr.ndim)
print(d3_arr.ndim)









