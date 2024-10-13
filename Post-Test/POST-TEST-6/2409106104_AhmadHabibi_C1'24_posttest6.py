pengguna = {}

barang = {
    1: {'nama': 'Beras', 'stok': 100, 'harga': 50000},
    2: {'nama': 'Minyak Goreng', 'stok': 50, 'harga': 30000},
    3: {'nama': 'Gula', 'stok': 75, 'harga': 15000}
}

while True:
    print("||==============================================================||")
    print("                 Selamat Datang di Toko Piala                    ")
    print("||==============================================================||")
    print("                          1. Register")
    print("                          2. Login")
    print("                          3. Keluar")
    print("||==============================================================||")
    pilihan = input("Pilih Menu: ").strip()

    if pilihan == '1':
        username_baru = input("Masukkan username baru: ").strip()

        if username_baru in pengguna:
            print("Username sudah terdaftar, silakan login atau gunakan username lain!\n")
        else:
            password_baru = input("Masukkan password baru: ").strip()
            pilihan_akun = input("Pilih akun\n1. Untuk akun pengguna\n2. Untuk admin: ").strip()

            if pilihan_akun == '1':
                pengguna[username_baru] = {'password': password_baru, 'role': 'pengguna'}
                print("Registrasi pengguna berhasil!\n")
            elif pilihan_akun == '2':
                pengguna[username_baru] = {'password': password_baru, 'role': 'admin'}
                print("Registrasi admin berhasil!\n")
            else:
                print("Pilihan tidak valid!\n")

    elif pilihan == '2':
        print("ANDA MEMILIH FITUR LOGIN \nSILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA ")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()

        if username in pengguna and pengguna[username]['password'] == password:
            print(f"\nLogin berhasil sebagai {username} ({pengguna[username]['role']})\n")
            
            if pengguna[username]['role'] == 'admin':
                while True:
                    print("Menu Admin: \n1. Tambah Barang \n2. Lihat Barang \n3. Edit Barang \n4. Hapus Barang \n5. Logout")
                    pilihan_admin = input("Pilih Menu: ").strip()

                    if pilihan_admin == '1':
                        id_baru = len(barang) + 1
                        nama_baru = input("Masukkan nama barang: ").strip()
                        stok_baru = input("Masukkan stok barang: ").strip()
                        harga_baru = input("Masukkan harga barang: ").strip()

                        if stok_baru.isdigit() and harga_baru.isdigit():
                            barang[id_baru] = {'nama': nama_baru, 'stok': int(stok_baru), 'harga': int(harga_baru)}
                            print("Barang berhasil ditambahkan!\n")
                        else:
                            print("Stok dan harga harus berupa angka!\n")

                    elif pilihan_admin == '2':
                        print("\nDaftar Barang:")
                        for p_id, p in barang.items():
                            print(f"ID: {p_id}, Nama: {p['nama']}, Stok: {p['stok']}, Harga: {p['harga']}")
                        print()

                    elif pilihan_admin == '3':
                        id_edit = input("Masukkan ID barang yang akan diedit: ").strip()

                        if id_edit.isdigit():
                            id_edit = int(id_edit)
                            if id_edit in barang:
                                nama_edit = input("Masukkan nama baru: ").strip()
                                stok_edit = input("Masukkan stok baru: ").strip()
                                harga_edit = input("Masukkan harga baru: ").strip()

                                if stok_edit.isdigit() and harga_edit.isdigit():
                                    barang[id_edit] = {'nama': nama_edit, 'stok': int(stok_edit), 'harga': int(harga_edit)}
                                    print("Barang berhasil diupdate!\n")
                                else:
                                    print("Stok dan harga harus berupa angka!\n")
                            else:
                                print("Barang tidak ditemukan!\n")
                        else:
                            print("ID barang harus berupa angka!\n")

                    elif pilihan_admin == '4':
                        id_hapus = input("Masukkan ID barang yang akan dihapus: ").strip()

                        if id_hapus.isdigit():
                            id_hapus = int(id_hapus)
                            if id_hapus in barang:
                                del barang[id_hapus]
                                print("Barang berhasil dihapus!\n")
                            else:
                                print("Barang tidak ditemukan!\n")
                        else:
                            print("ID barang harus berupa angka!\n") 

                    elif pilihan_admin == '5':
                        print("Logout berhasil!\n")
                        break

                    else:
                        print("Pilihan tidak valid!\n")

            elif pengguna[username]['role'] == 'pengguna':
                while True:
                    print("Menu Pengguna: \n1. Lihat Barang \n2. Beli Barang \n3. Logout")
                    pilihan_pengguna = input("Pilih Menu: ").strip()

                    if pilihan_pengguna == '1':
                        print("\nDaftar Barang:")
                        for p_id, p in barang.items():
                            print(f"ID: {p_id}, Nama: {p['nama']}, Stok: {p['stok']}, Harga: {p['harga']}")
                        print()

                    elif pilihan_pengguna == '2':
                        id_beli = input("Masukkan ID barang yang ingin dibeli: ").strip()

                        if id_beli.isdigit():
                            id_beli = int(id_beli)
                            if id_beli in barang and barang[id_beli]['stok'] > 0:
                                print(f"Anda telah membeli {barang[id_beli]['nama']} seharga {barang[id_beli]['harga']}\n")
                                barang[id_beli]['stok'] -= 1
                            else:
                                print("Barang tidak tersedia atau stok habis!\n")
                        else:
                            print("ID barang harus berupa angka!\n")

                    elif pilihan_pengguna == '3':
                        print("Logout berhasil!\n")
                        break

                    else:
                        print("Pilihan tidak valid!\n")
        else:
            print("Login gagal! Username atau password salah.\n")

    elif pilihan == '3':
        print("Anda memilih untuk keluar, sampai jumpa lagi :)")
        break

    else:
        print("Pilihan tidak valid!\n")