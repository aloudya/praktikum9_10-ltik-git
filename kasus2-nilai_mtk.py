import numpy as np

# urut nilai dari besar ke kecil dan 5 nilai terbesar

data = np.array([88, 92, 79, 93, 85, 91, 87, 95, 90, 89,
                32, 54, 54, 33, 90, 90, 43, 89, 90, 70,
                89, 66, 64, 90, 65, 43, 54, 43, 89, 90])

sort = np.sort(data)[::-1] # ascending
top5 = np.sort(data)[-5:][::-1]

print("Data nilai matematika siswa yang terurut:", sort)
print("5 nilai matematika siswa terbesar:", top5)