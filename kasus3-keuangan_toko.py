import numpy as np

# rata-rata, hari dgn keuntungan tertinggi, hari dgn kerugian tertinggi

data = np.array([50000, 75000, -20000, 100000, 25000, -5000, 80000,
                3000, 15000, 7500, 90000, 43000, -12000, 65000])

avg = np.mean(data)
top = np.max(data)
bottom = np.min(data)

hari_top = np.where(data == top)[0][0]
# print(hari_top)
hari_bottom = np.where(data == bottom)[0][0]

print("Rata-rata keuntungan/kerugian toko dalam seminggu: Rp", avg)
print(f"Hari ke-{hari_top} dengan keuntungan tertinggi: Rp{top}")
print(f"Hari ke-{hari_bottom} dengan kerugian tertinggi: Rp{bottom}")