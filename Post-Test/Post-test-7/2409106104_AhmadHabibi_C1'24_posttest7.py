pengguna = {}
barang = {
    1: {'nama': 'Beras', 'stok': 100, 'harga': 50000},
    2: {'nama': 'Minyak Goreng', 'stok': 50, 'harga': 30000},
    3: {'nama': 'Gula', 'stok': 75, 'harga': 15000}
}

def register(pengguna, username_baru, password_baru, pilihan_akun):
    if username_baru in pengguna:
        print("Username sudah terdaftar, silakan login atau gunakan username lain!\n")
    else:
        if pilihan_akun == '1':
            pengguna[username_baru] = {'password': password_baru, 'role': 'pengguna'}
            print("Registrasi pengguna berhasil!\n")
        elif pilihan_akun == '2':
            pengguna[username_baru] = {'password': password_baru, 'role': 'admin'}
            print("Registrasi admin berhasil!\n")
        else:
            print("Pilihan tidak valid!\n")
    return pengguna

def login(pengguna, barang):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in pengguna and pengguna[username]['password'] == password:
        print(f"\nLogin berhasil sebagai {username} ({pengguna[username]['role']})\n")
        if pengguna[username]['role'] == 'admin':
            menu_admin(pengguna, barang)
        elif pengguna[username]['role'] == 'pengguna':
            menu_pengguna(pengguna, barang)
    else:
        print("Login gagal! Username atau password salah.\n")

def lihat_barang_rekursif(barang, index=0):
    keys = list(barang.keys())
    if index < len(keys):
        b_id = keys[index]
        b = barang[b_id]
        print(f"ID: {b_id}, Nama: {b['nama']}, Stok: {b['stok']}, Harga: {b['harga']}")
        lihat_barang_rekursif(barang, index + 1)

def lihat_barang(barang):
    print("\nDaftar Barang:")
    lihat_barang_rekursif(barang)
    print()

def tambah_barang(barang):
    id_baru = len(barang) + 1
    nama_baru = input("Masukkan nama barang: ")
    stok_baru = input("Masukkan stok barang: ")
    harga_baru = input("Masukkan harga barang: ")

    if not stok_baru.isdigit() or not harga_baru.isdigit():
        print("Error: Stok dan harga harus berupa angka!\n")
        return barang

    barang[id_baru] = {'nama': nama_baru, 'stok': int(stok_baru), 'harga': int(harga_baru)}
    print("Barang berhasil ditambahkan!\n")
    return barang

def edit_barang(barang, id_edit):
    if not id_edit.isdigit():
        print("Error: ID barang harus berupa angka!\n")
        return barang

    id_edit = int(id_edit)
    if id_edit not in barang:
        print("Error: Barang tidak ditemukan!\n")
        return barang

    nama_edit = input("Masukkan nama baru: ")
    stok_edit = input("Masukkan stok baru: ")
    harga_edit = input("Masukkan harga baru: ")

    if not stok_edit.isdigit() or not harga_edit.isdigit():
        print("Error: Stok dan harga harus berupa angka!\n")
        return barang

    barang[id_edit] = {'nama': nama_edit, 'stok': int(stok_edit), 'harga': int(harga_edit)}
    print("Barang berhasil diupdate!\n")
    return barang

def menu_admin(pengguna, barang):
    while True:
        print("Menu Admin:\n1. Tambah Barang\n2. Lihat Barang\n3. Edit Barang\n4. Hapus Barang\n5. Logout")
        pilihan_admin = input("Pilih Menu: ")

        if pilihan_admin == '1':
            barang = tambah_barang(barang) 
        elif pilihan_admin == '2':
            lihat_barang(barang)  
        elif pilihan_admin == '3':
            id_edit = input("Masukkan ID barang yang akan diedit: ")
            barang = edit_barang(barang, id_edit)  
        elif pilihan_admin == '4':
            id_hapus = input("Masukkan ID barang yang akan dihapus: ")
            barang = hapus_barang(barang, id_hapus)  
        elif pilihan_admin == '5':
            print("Logout berhasil!\n")
            break
        else:
            print("Pilihan tidak valid!\n")

def hapus_barang(barang, id_hapus):
    if not id_hapus.isdigit():
        print("Error: ID barang harus berupa angka!\n")
        return barang

    id_hapus = int(id_hapus)
    if id_hapus not in barang:
        print("Error: Barang tidak ditemukan!\n")
        return barang

    del barang[id_hapus]
    print("Barang berhasil dihapus!\n")
    return barang

def menu_pengguna(pengguna, barang):
    while True:
        print("Menu Pengguna:\n1. Lihat Barang\n2. Beli Barang\n3. Logout")
        pilihan_pengguna = input("Pilih Menu: ")

        if pilihan_pengguna == '1':
            lihat_barang(barang) 
        elif pilihan_pengguna == '2':
            barang = beli_barang(barang)
        elif pilihan_pengguna == '3':
            print("Logout berhasil!\n")
            break
        else:
            print("Pilihan tidak valid!\n")

def beli_barang(barang):
    print("\nDaftar Barang:")
    lihat_barang(barang)
    id_beli = input("Masukkan ID barang yang ingin dibeli: ")

    if not id_beli.isdigit():
        print("Error: ID barang harus berupa angka!\n")
        return barang

    id_beli = int(id_beli)
    if id_beli not in barang or barang[id_beli]['stok'] <= 0:
        print("Error: Barang tidak ditemukan atau stok habis!\n")
        return barang

    print(f"Anda telah membeli {barang[id_beli]['nama']} seharga {barang[id_beli]['harga']}\n")
    barang[id_beli]['stok'] -= 1
    return barang

while True:
    print("||==============================================================||")
    print("                 Selamat Datang di Toko Piala                    ")
    print("||==============================================================||")
    print("                          1. Register")
    print("                          2. Login")
    print("                          3. Keluar")
    print("||==============================================================||")
    pilihan = input("Pilih Menu: ")

    if pilihan == '1':
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")
        pilihan_akun = input("Pilih akun\n1. Untuk akun pengguna\n2. Untuk admin: ")
        pengguna = register(pengguna, username_baru, password_baru, pilihan_akun)
    elif pilihan == '2':
        login(pengguna, barang)
    elif pilihan == '3':
        print("Anda memilih untuk keluar. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!\n")
