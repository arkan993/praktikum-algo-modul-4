import math

def cek_bilangan_prima(angka):
    """
    """
    # Bilangan prima harus lebih besar dari 1
    if angka <= 1:
        return False
    
    # 2 adalah bilangan prima
    if angka == 2:
        return True
    
    # Bilangan genap selain 2 bukanlah prima
    if angka % 2 == 0:
        return False
    
    # Cek pembagian dari 3 sampai akar kuadrat dari angka,
    # hanya dengan bilangan ganjil (step 2)
    # Ini meningkatkan efisiensi.
    batas_cek = int(math.sqrt(angka))
    for i in range(3, batas_cek + 1, 2):
        if angka % i == 0:
            return False
            
    # Jika tidak ada pembagi yang ditemukan, maka itu prima
    return True

def main():
    """
    Fungsi utama untuk meminta input dan menampilkan hasilnya.
    """
    # Meminta input dari pengguna
    try:
        input_angka = int(input("Masukkan sebuah bilangan bulat: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")
        return

    # Memanggil fungsi 'cek_bilangan_prima' dan menggunakan parameternya
    adalah_prima = cek_bilangan_prima(input_angka)

    # Menampilkan hasil
    print("-" * 30)
    if adalah_prima:
        print(f"Bilangan **{input_angka}** adalah **bilangan prima**.")
    else:
        print(f"Bilangan **{input_angka}** **bukan** bilangan prima.")
    print("-" * 30)

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()