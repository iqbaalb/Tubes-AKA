import matplotlib.pyplot as plt
import time

# Iteratif
def bubble_sort_iteratif(skor):
    n = len(skor)
    for i in range(n):
        for j in range(0, n - i - 1):
            if skor[j] < skor[j + 1]:
                skor[j], skor[j + 1] = skor[j + 1], skor[j]
    return skor

# Rekursif
def merge_sort_rekursif(skor):
    if len(skor) > 1:
        tengah = len(skor) // 2
        kiri = skor[:tengah]
        kanan = skor[tengah:]

        # Pemanggilan rekursif untuk setiap setengah
        merge_sort_rekursif(kiri)
        merge_sort_rekursif(kanan)

        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] > kanan[j]:
                skor[k] = kiri[i]
                i += 1
            else:
                skor[k] = kanan[j]
                j += 1
            k += 1

        while i < len(kiri):
            skor[k] = kiri[i]
            i += 1
            k += 1

        while j < len(kanan):
            skor[k] = kanan[j]
            j += 1
            k += 1
    return skor

# Data percobaan
data_percobaan = [
    [60, 50, 40 , 30, 20, 10],
    [70, 60, 50, 40, 30, 20],
    [80, 70, 60, 50, 40, 30],
    [90, 80, 70, 60, 50, 40],
    
]

iterative_times = []
recursive_times = []

# Mengukur waktu eksekusi untuk setiap dataset
for data in data_percobaan:
    # Iteratif
    start_time = time.time()
    bubble_sort_iteratif(data.copy())
    iterative_times.append(time.time() - start_time)

    # Rekursif
    start_time = time.time()
    merge_sort_rekursif(data.copy())
    recursive_times.append(time.time() - start_time)

# Menampilkan tabel data
print(f"{' tingkat keparahan penyakit ':<40}{'Iteratif Time (s)':<25}{'Rekursif Time (s)':<25}")
for i, data in enumerate(data_percobaan):
    print(f"{str(data):<40}{iterative_times[i]:<25.10f}{recursive_times[i]:<25.10f}")

# Membuat grafik
plt.figure(figsize=(10, 5))
plt.plot(range(1, len(data_percobaan) + 1), iterative_times, marker='o', label='Iteratif')
plt.plot(range(1, len(data_percobaan) + 1), recursive_times, marker='o', label='Rekursif')
plt.title("Perbandingan Waktu Eksekusi: Iteratif vs Rekursif")
plt.xlabel("tingkat keparahan penyakit ")
plt.ylabel("Waktu Eksekusi (detik)")
plt.xticks(range(1, len(data_percobaan) + 1), [f"tingkat keparahan penyakit {i+1}" for i in range(len(data_percobaan))])
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()