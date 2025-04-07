def bilangan(x):
    return list(range(x, 0, -1))  # Membuat list dari x ke 1

# Input dari user
x = int(input("Masukkan bilangan: "))

angka = bilangan(x)

# Proses perkalian
hasil = 1
for i in angka:
    hasil *= i

# Format output string
teks = ' x '.join(str(i) for i in angka)
print(f"{teks} = {hasil}")
