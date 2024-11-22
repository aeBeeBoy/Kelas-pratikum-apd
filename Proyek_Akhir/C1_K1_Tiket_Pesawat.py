import pwinput  # Mengimpor pwinput untuk menangani input password dengan bintang

# Menyimpan akun pengguna yang mendaftar
akuns = {}

# Data akun admin yang sudah ada
akunADM = {
    "name": ["Yusuf", "Hazzel", "Habibi", "admin"],  # Daftar username admin
    "password": [93, 96, 104, 123]  # Daftar password admin
}

# Data jadwal penerbangan (tujuan, harga, jumlah tiket)
jadwal_penerbangan = {
    "1": {"tujuan": "Bali", "harga": "1000000", "jumlah": "50"},
    "2": {"tujuan": "Jakarta", "harga": "500000", "jumlah": "30"},
    "3": {"tujuan": "Surabaya", "harga": "600000", "jumlah": "40"}
}

# Data pembelian tiket yang dilakukan oleh pengguna
pembelian = {}

def registrasi():
    print("="*25)
    print("Halo Pengguna Baru. Silahkan Registrasi terlebih dahulu")
    try:
        username = str(input("Username: "))
        
        # Mengecek jika username kosong
        if not username.strip():  # Mengecek jika username kosong atau hanya spasi
            print("Username tidak boleh kosong. Silakan coba lagi.")
            print(" ")
            return  # Menghentikan proses jika username kosong
        
        # Gunakan pwinput untuk menyembunyikan password yang dimasukkan
        password = pwinput.pwinput("Password: ")
        
        # Cek apakah password bisa dikonversi ke integer
        try:
            password = int(password)  # Mengkonversi password yang dimasukkan ke tipe integer
        except ValueError:
            print("Password harus berupa angka. Silakan coba lagi.")
            print(" ")
            return  # Kembali ke awal fungsi jika terjadi ValueError

        # Cek apakah username sudah terdaftar
        if username in akuns:
            print("Nama sudah terpakai. Silahkan coba lagi.")
            print(" ")
        else:
            akuns[username] = password  # Menyimpan kata sandi pengguna
            print(f"Akun Anda berhasil terdaftar dengan ID: {username}")

        print("="*25)
    except ValueError:
        print("Nama pengguna harus berupa Hurf, pastikan Anda tidak menekan tombol Enter saja.")
        print(" ")
        
        

def tampil_jadwal():
    """Fungsi untuk menampilkan jadwal penerbangan dengan kolom rapi."""
    if jadwal_penerbangan:  # Jika jadwal penerbangan ada
        print("="*40)
        print(f"{'ID':<5} {'Tujuan':<15} {'Harga':<10} {'Jumlah':<10}") # <5, <15, <10: Menentukan lebar kolom yang akan disesuaikan untuk No, Tujuan, Harga
        print("="*40)
        
        for id, tiket in jadwal_penerbangan.items():
            # Menampilkan ID, tujuan, harga, dan jumlah tiket dengan lebar kolom yang konsisten
            print(f"{id:<5} {tiket['tujuan']:<15} {tiket['harga']:<10} {tiket['jumlah']:<10}")
        
        print("="*40)
    else:
        print("Saat ini anda belum membuat jadwal penerbangan.")
def beli_tiket(username):
    """Fungsi untuk membeli tiket penerbangan."""
    if not jadwal_penerbangan:  # Jika tidak ada tiket yang tersedia
        print("Tidak ada tiket yang tersedia untuk dibeli.")
        return
    
    tampil_jadwal()  # Menampilkan daftar jadwal penerbangan
    tiket_id = input("Masukkan ID tiket yang ingin dibeli: ")
    
    if tiket_id in jadwal_penerbangan:  # Memeriksa apakah tiket ID valid
        tiket = jadwal_penerbangan[tiket_id]
        jumlah_tiket_tersedia = int(tiket['jumlah'])  # Mengambil jumlah tiket yang tersedia
        
        jumlah = int(input("Masukkan jumlah tiket yang ingin dibeli: "))  # Input jumlah tiket yang ingin dibeli
        
        if jumlah > jumlah_tiket_tersedia:  # Jika jumlah tiket yang dibeli melebihi jumlah yang tersedia
            print("Tiket yang dibeli melebihi kapasitas. Pembelian dibatalkan.")
        else:
            total_harga = jumlah * float(tiket['harga'])  # Menghitung total harga tiket
            print(f"Total harga untuk {jumlah} tiket ke {tiket['tujuan']}: {total_harga}")
            
            konfirmasi = input("Apakah Anda yakin ingin membeli? (iya/tidak): ")  # Konfirmasi pembelian
            
            if konfirmasi.lower() == "iya":
                # Update jumlah tiket yang tersedia setelah pembelian
                tiket['jumlah'] = str(jumlah_tiket_tersedia - jumlah)
                
                if username not in pembelian:
                    pembelian[username] = []  # Menambah user baru jika belum ada
                
                # Menambahkan pembelian ke daftar pembelian pengguna
                pembelian[username].append({
                    "tujuan": tiket['tujuan'],
                    "harga": tiket['harga'],
                    "jumlah": jumlah
                })
                print("Pembelian berhasil!")
            else:
                print("Pembelian dibatalkan.")
    else:
        print("ID tiket tidak valid.")

def menu_admin(username):
    """Menu untuk admin setelah login berhasil."""
    while True:
        print("----------------------------------")
        print("[1] Tampilkan jadwal Tiket       |")
        print("[2] Tambah Tiket                 |")
        print("[3] Hapus Tiket                  |")
        print("[4] Ubah Tiket                   |")
        print("[5] Daftar Pembelian             |")
        print("[6] Log out                      |")
        print("----------------------------------")
        
        try:
            admopsi = int(input("Pilih opsi: "))
        except ValueError:
            print("Pilihan harus berupa angka. Silakan coba lagi.")
            continue
        
        if admopsi == 1:
            print("="*25)
            tampil_jadwal()  # Menampilkan jadwal tiket
        elif admopsi == 2:
            try:
                print("="*25)
                print("Silahkan tambah jadwal tiket penerbangan beserta harganya")
                tujuan = str(input("Masukkan tujuan penerbangan: "))
                
                if not tujuan.strip():  # Mengecek apakah tujuan kosong
                    raise ValueError("Tujuan tidak boleh kosong.")
                
                jumlah = int(input("Masukkan Jumlah Tiket: "))
                
                if jumlah <= 0:  # Mengecek apakah jumlah tiket lebih dari 0
                    raise ValueError("Jumlah tiket harus lebih dari 0.")
                
                harga = int(input("Masukkan harga: "))
                
                if harga <= 0:  # Mengecek apakah harga lebih dari 0
                    raise ValueError("Harga harus lebih dari 0.")
                
                # Menambahkan tiket baru ke jadwal penerbangan
                id = str(len(jadwal_penerbangan) + 1)
                jadwal_penerbangan[id] = {"tujuan": tujuan, "harga": harga, "jumlah": jumlah}
                print(f"Penerbangan ke {tujuan} dengan harga {harga} telah berhasil ditambahkan.")
                
            except ValueError as e:
                print(f"Tolong mengisi tiket dengan benar: {e}")
                
        elif admopsi == 3:
            print("="*25)
            tampil_jadwal()

            if not jadwal_penerbangan:  # Jika tidak ada tiket untuk dihapus
                print("Tidak ada tiket yang bisa dihapus.")
            else:
                hapus = input("Tiket nomor berapa yang ingin dihapus: ")
                
                if hapus in jadwal_penerbangan:  # Memeriksa apakah ID tiket valid
                    print("Apa Anda yakin ingin membatalkan penerbangan ini?")
                    print("1. Iya")
                    print("2. Tidak")
                    memastikan_hapus = input("Pilih: ")
                    
                    if memastikan_hapus == "1":
                        del jadwal_penerbangan[hapus]  # Menghapus tiket dari jadwal penerbangan
                        print("Tiket yang Anda pilih sudah dihapus!\n")
                    elif memastikan_hapus == "2":
                        print("Aksi untuk menghapus dibatalkan.")
                    else:
                        print("Mohon pilih '1' atau '2'")
                else:
                    print("ID tiket tidak ada di daftar.")  # Pesan jika ID tiket tidak valid
                
        elif admopsi == 4:
            print("="*25)
            if not jadwal_penerbangan:  # Jika tidak ada tiket untuk diubah
                print("Tidak ada tiket yang dapat diubah.")
            else:
                tampil_jadwal()  # Menampilkan tiket yang ada
                tiket_id = input("Masukkan ID tiket yang ingin diubah: ")
                if tiket_id in jadwal_penerbangan:
                    print("Masukkan detail baru untuk tiket ini:")
                    tujuan_baru = input(f"Tujuan (sekarang: {jadwal_penerbangan[tiket_id]['tujuan']}): ") 
                    jumlah_baru = input(f"Jumlah (sekarang: {jadwal_penerbangan[tiket_id]['jumlah']}): ") 
                    harga_baru = input(f"Harga (sekarang: {jadwal_penerbangan[tiket_id]['harga']}): ") 
                    # Update tiket
                    jadwal_penerbangan[tiket_id] = {
                        "tujuan": tujuan_baru,
                        "harga": harga_baru,
                        "jumlah": jumlah_baru
                    }
                    print(f"Tiket dengan ID {tiket_id} telah diperbarui.")
                else:
                    print("ID tiket tidak valid.")
        elif admopsi == 5:
            print("="*40)
            if pembelian:
                print(f"{'Username':<20} {'Tujuan':<15} {'Harga':<10} {'Jumlah':<10}")
                print("="*40)
                
                for username, daftar_beli in pembelian.items():
                    for item in daftar_beli:
                        # Menampilkan pembelian dengan kolom yang terstruktur
                        print(f"{username:<20} {item['tujuan']:<15} {item['harga']:<10} {item['jumlah']:<10}")
                        
            else:
                print("Tidak ada pembelian yang tercatat.")
            print("="*40)
        elif admopsi == 6:
            print("Admin logout.")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

def menu_pengguna(username):
    """Menu untuk pengguna biasa setelah login berhasil."""
    while True:
        print("----------------------------------")
        print("[1] Lihat Jadwal                 |")
        print("[2] Membeli Tiket                |")
        print("[3] Batal Beli                   |")
        print("[4] Lihat Transaksi              |")
        print("[5] Log out                      |")
        print("----------------------------------")
        
        try:
            useropsi = int(input("Pilih opsi: "))
        except ValueError:
            print("Pilihan harus berupa angka. Silakan coba lagi.")
            continue
        
        if useropsi == 1:
            print("="*25)
            tampil_jadwal()  # Menampilkan jadwal penerbangan
        elif useropsi == 2:
            print("="*25)
            beli_tiket(username)  # Membeli tiket
        elif useropsi == 3:
            print("="*40)
            if username in pembelian and pembelian[username]:
                # Menampilkan header kolom
                print(f"{'No':<5} {'Tujuan':<15} {'Harga':<10} {'Jumlah':<10}")
                print("="*40)

                # Menampilkan daftar pembelian pengguna
                for i, item in enumerate(pembelian[username], start=1):
                    print(f"{i:<5} {item['tujuan']:<15} {item['harga']:<10} {item['jumlah']:<10}")
                    print("="*40)
                
                # Meminta input nomor tiket yang ingin dibatalkan
                tiket_id = input("Masukkan nomor tiket yang ingin dibatalkan: ")

                if tiket_id.isdigit() and 1 <= int(tiket_id) <= len(pembelian[username]): 
                    # isdigit Memastikan bahwa input yang dimasukkan oleh pengguna (tiket_id) hanya terdiri dari angka
                    tiket_batal = pembelian[username][int(tiket_id) - 1]
                    konfirmasi_batal = input(f"Apakah Anda yakin ingin membatalkan pembelian tiket ke {tiket_batal['tujuan']}? (iya/tidak): ").lower()

                    if konfirmasi_batal == "iya":
                        del pembelian[username][int(tiket_id) - 1]
                        for id, tiket in jadwal_penerbangan.items():
                            if tiket['tujuan'] == tiket_batal['tujuan']:
                                tiket['jumlah'] = str(int(tiket['jumlah']) + tiket_batal['jumlah'])
                                break
                        print(f"Tiket pembelian ke {tiket_batal['tujuan']} telah dibatalkan.")
                    else:
                        print("Pembatalan dibatalkan.")
                else:
                    print("Nomor tiket tidak valid.")
            else:
                print("Anda belum melakukan pembelian.")
            print("="*40)
            
        elif useropsi == 4:
            print("="*25)
            if username in pembelian and pembelian[username]:
                print("Daftar Pembelian Anda:")
                for i, item in enumerate(pembelian[username], start=1):
                    print(f"{i}. Tujuan: {item['tujuan']}, Harga: {item['harga']}, Jumlah: {item['jumlah']}") 
            else:
                print("Anda belum melakukan pembelian.")
        elif useropsi == 5:
            print("Terima kasih! Sampai jumpa.")
            break
        else:
            print("Opsi tidak valid, silakan coba lagi.")

# Program utama
while True:
    print("Halo! Selamat datang di Aplikasi Penerbangan")
    print("Silakan pilih Registrasi terlebih dahulu jika belum buat akun!")
    print("-----------------------")
    print("[1] Registrasi        |")
    print("[2] Login             |")
    print("[3] Keluar            |")
    print("-----------------------")

    try:
        opsi = int(input("Pilih opsi: "))
    except ValueError:
        print("Pilihan harus berupa angka. Silakan coba lagi.")
        print("="*25)
        continue

    if opsi == 1:
        registrasi()  # Memanggil fungsi registrasi
    elif opsi == 2:
        print("="*25)
        print("Silahkan Masukan akun anda")
        print("="*40)
        
        username = str(input("Username: "))
        
        # Mengecek jika username kosong
        if not username.strip():  # Mengecek jika username kosong atau hanya spasi
            print("Username tidak boleh kosong. Silakan coba lagi.")
            print(" ")
            continue  # Kembali ke menu pilihan

        # Menggunakan pwinput untuk input password yang tersembunyi dengan bintang
        password = pwinput.pwinput("Password (harus angka): ")
        print("="*40)

        try:
            password = int(password)  # Mengkonversi password yang dimasukkan ke tipe integer
        except ValueError:
            print("Password harus berupa angka.")
            print(" ")
            continue

        # Login sebagai admin
        if username in akunADM["name"]:
            index = akunADM["name"].index(username)
            if password == akunADM["password"][index]:
                print(f"Selamat datang, {username}! Anda adalah admin.")
                menu_admin(username)
            else:
                print("Password salah.")
                print("="*25)
        
        # Login sebagai pengguna biasa
        elif username in akuns and akuns[username] == password:
            print("="*25)
            print(f"Hallo {username}, Selamat datang di Aplikasi Penerbangan kami :) ")
            menu_pengguna(username)  # Pengguna biasa login
        else:
            print("Username atau Password salah.")
    elif opsi == 3:
        print("="*25)
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Opsi tidak valid.")