def tentukan_akhiran_ordinal(angka):
    """
    Fungsi ini menentukan akhiran ordinal yang benar (st, nd, rd, th)
    untuk sebuah bilangan bulat, tetapi mengembalikan hanya akhiran (suffix).

    Parameter:
    angka (int): Bilangan bulat yang akan diberikan akhiran.

    Mengembalikan:
    str: Akhiran ordinal yang benar ('st', 'nd', 'rd', atau 'th').
    """
    # Ubah angka menjadi string
    angka_str = str(angka)

    # Logika untuk angka belasan (11, 12, 13, dst.) yang selalu berakhiran 'th'
    # Pengecekan dilakukan pada 1 atau 2 digit terakhir.
    if len(angka_str) >= 2 and angka_str[-2:] in ('11', '12', '13'):
        return 'th'

    # Logika untuk angka-angka lain berdasarkan digit terakhir
    digit_terakhir = angka_str[-1]

    if digit_terakhir == '1':
        return 'st'
    elif digit_terakhir == '2':
        return 'nd'
    elif digit_terakhir == '3':
        return 'rd'
    else:
        # Semua kasus lainnya (termasuk 4, 5, 6, 7, 8, 9, 0) menggunakan 'th'
        return 'th'

def main():
    """
    Fungsi utama untuk menjalankan program interaktif,
    meminta input berulang, dan menampilkan output seperti yang diminta.
    """
    print("Ordinal Number")
    print("ketik 0 untuk menghentikan program")
    
    # Loop tak terbatas
    while True:
        try:
            # Meminta input dari pengguna
            input_str = input("masukkan angka: ")
            
            # Konversi ke integer
            angka = int(input_str)

            # Logika untuk menghentikan program
            if angka == 0:
                # Meskipun output di gambar menampilkan (0, 'th'),
                # kita harus menampilkan itu sebelum menghentikan program
                akhiran = tentukan_akhiran_ordinal(angka)
                print(f"({angka}, '{akhiran}')")
                print("terima kasih telah menggunakan program saya")
                break
            
            # Memanggil fungsi untuk mendapatkan akhiran
            akhiran = tentukan_akhiran_ordinal(angka)

            # Menampilkan output sesuai format (angka, 'suffix')
            print(f"({angka}, '{akhiran}')")

        except ValueError:
            print("Input tidak valid. Harap masukkan bilangan bulat.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            break

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()