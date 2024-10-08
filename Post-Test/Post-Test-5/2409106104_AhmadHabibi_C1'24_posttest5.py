pengguna = [
    [1, 'tokopiala', 'tokopiala', 'admin'],
    [2, 'user', 'habiboy', 'pengguna']
]

barang = [
    [1, 'Beras', 100, 50000],
    [2, 'Minyak Goreng', 50, 30000],
    [3, 'Gula', 75, 15000]
]

while True:
    print("||==============================||")
    print("Selamat Datang di Manajemen Toko \n1. Login \n2. Register \n3. Keluar")
    print("||==============================||")
    pilihan = input("Pilih Menu: ").strip()

    if pilihan == '1':
        print("ANDA MEMILIH FITUR LOGIN \nSILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA ")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()

        if not username or not password:
            print("Username dan password tidak boleh kosong!\n")
            continue

        user = None
        for u in pengguna:
            if u[1] == username and u[2] == password:
                user = u
                break

        if user:
            print(f"\nLogin berhasil sebagai {user[1]} ({user[3]})\n")
            if user[3] == 'admin':
                while True:
                    print("Menu Admin:")
                    print("1. Tambah Barang")
                    print("2. Lihat Barang")
                    print("3. Edit Barang")
                    print("4. Hapus Barang")
                    print("5. Logout")
                    pilihan_admin = input("Pilih Menu: ").strip()

                    if pilihan_admin == '1':
                        nama_baru = input("Masukkan nama barang: ").strip()
                        if not nama_baru:
                            print("Nama barang tidak boleh kosong!\n")
                            continue
                        
                        stok_baru = input("Masukkan stok barang: ").strip()
                        if not stok_baru.isdigit() or int(stok_baru) <= 0:
                            print("Stok harus berupa angka positif!\n")
                            continue
                        
                        harga_baru = input("Masukkan harga barang: ").strip()
                        if not harga_baru.isdigit() or int(harga_baru) <= 0:
                            print("Harga harus berupa angka positif!\n")
                            continue
                        
                        id_baru = len(barang) + 1
                        barang.append([id_baru, nama_baru, int(stok_baru), int(harga_baru)])
                        print("Barang berhasil ditambahkan ke stok!\n")

                    elif pilihan_admin == '2':
                        if not barang:
                            print("Tidak ada barang di stok!\n")
                        else:
                            print("\nDaftar Barang:")
                            for b in barang:
                                print(f"ID: {b[0]}, Nama: {b[1]}, Stok: {b[2]}, Harga: {b[3]}")
                            print()

                    elif pilihan_admin == '3':
                        id_edit = input("Masukkan ID barang yang akan diedit: ").strip()
                        if not id_edit.isdigit():
                            print("ID harus berupa angka!\n")
                            continue

                        id_edit = int(id_edit)
                        for b in barang:
                            if b[0] == id_edit:
                                nama_edit = input("Masukkan nama baru: ").strip()
                                if not nama_edit:
                                    print("Nama barang tidak boleh kosong!\n")
                                    continue

                                stok_edit = input("Masukkan stok baru: ").strip()
                                if not stok_edit.isdigit() or int(stok_edit) <= 0:
                                    print("Stok harus berupa angka positif!\n")
                                    continue

                                harga_edit = input("Masukkan harga baru: ").strip()
                                if not harga_edit.isdigit() or int(harga_edit) <= 0:
                                    print("Harga harus berupa angka positif!\n")
                                    continue

                                b[1], b[2], b[3] = nama_edit, int(stok_edit), int(harga_edit)
                                print("Barang berhasil diupdate!\n")
                                break
                        else:
                            print("Barang tidak ditemukan!\n")

                    elif pilihan_admin == '4':
                        id_hapus = input("Masukkan ID barang yang akan dihapus: ").strip()
                        if not id_hapus.isdigit():
                            print("ID harus berupa angka!\n")
                            continue
                        
                        id_hapus = int(id_hapus)
                        for b in barang:
                            if b[0] == id_hapus:
                                barang.remove(b)
                                print("Barang berhasil dihapus dari stok!\n")
                                break
                        else:
                            print("Barang tidak ditemukan!\n")

                    elif pilihan_admin == '5':
                        print("Logout berhasil!\n")
                        break

                    else:
                        print("Pilihan tidak valid!\n")

            elif user[3] == 'pengguna':
                while True:
                    print("Menu Pengguna:")
                    print("1. Lihat Barang")
                    print("2. Beli Barang")
                    print("3. Logout")
                    pilihan_pengguna = input("Pilih Menu: ").strip()

                    if pilihan_pengguna == '1':
                        if not barang:
                            print("Tidak ada barang di stok!\n")
                        else:
                            print("\nDaftar Barang:")
                            for b in barang:
                                print(f"ID: {b[0]}, Nama: {b[1]}, Stok: {b[2]}, Harga: {b[3]}")
                            print()

                    elif pilihan_pengguna == '2':
                        if not barang:
                            print("Tidak ada barang untuk dibeli!\n")
                            continue

                        id_beli = input("Masukkan ID barang yang ingin dibeli: ").strip()
                        if not id_beli.isdigit():
                            print("ID harus berupa angka!\n")
                            continue
                        
                        id_beli = int(id_beli)
                        for b in barang:
                            if b[0] == id_beli and b[2] > 0:
                                print(f"Anda telah membeli {b[1]} seharga {b[3]}")
                                b[2] -= 1
                                break
                        else:
                            print("Barang tidak tersedia atau stok habis!\n")

                    elif pilihan_pengguna == '3':
                        print("Logout berhasil!\n")
                        break

                    else:
                        print("Pilihan tidak valid!\n")
        
        else:
            print("Login gagal! Username atau password salah.\n")

    elif pilihan == '2':
        username_baru = input("Masukkan username baru: ").strip()
        if not username_baru:
            print("Username tidak boleh kosong!\n")
            continue

        checkusername = False
        for u in pengguna:
            if u[1] == username_baru:
                checkusername = True
                break
        if checkusername:
            print("Username telah digunakan, silahkan login atau coba username lain!\n")
        else:
            password_baru = input("Masukkan password baru: ").strip()

            if not password_baru:
                print("Password tidak boleh kosong!\n")
                continue

            pilihanakun = input("Masukkan pilihan anda\n1. Untuk akun pengguna\n2. Untuk admin: ").strip()
            if pilihanakun == '1':
                pengguna.append([len(pengguna) + 1, username_baru, password_baru, 'pengguna'])
                print("Registrasi pengguna berhasil!\n")
            elif pilihanakun == '2':
                pengguna.append([len(pengguna) + 1, username_baru, password_baru, 'admin'])
                print("Registrasi admin berhasil!\n")
            else:
                print("Pilihan tidak valid! Registrasi gagal.\n")

    elif pilihan == '3':
        print("Anda memilih untuk keluar, terima kasih telah mengakses sistem manajemen toko!")
        break

    else:
        print("Pilihan tidak valid!\n")