import numpy as np

# konversi celcius ke farenheit dgn numpy

data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
farenheit = (data * 9/5) + 32

print(f"Suhu dalam Celcius: {data}°C")
print(f"Suhu dalam Farenheit: {farenheit}°F")

