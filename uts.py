saldo = 100000
pin = 260102

def informasi_saldo():
    print('Saldo Anda Rp. {}'.format(saldo))

def ambil_saldo(jumlah_ambil_saldo):
    global saldo

    print('Saldo Anda Rp. {}'.format(saldo))
    saldo = saldo - jumlah_ambil_saldo
    print('Saldo Anda Sekarang Rp. {}'.format(saldo))

def tambah_saldo(jumlah_tambah_saldo):
    global saldo

    print('Saldo Anda Rp. {}'.format(saldo))
    saldo = saldo + jumlah_tambah_saldo
    print('Saldo Anda Sekarang Rp. {}'.format(saldo))

def transfer(jumlah_transfer):
    global saldo

    print('Saldo Anda Rp. {}'.format(saldo))
    saldo = saldo - jumlah_transfer
    print('Transfer Telah Berhasil Dilakukan, Saldo Anda Sekarang Rp. {}'.format(saldo))

def ganti_pin(pin_lama, pin_baru):
    global pin

    if not pin_lama == pin:
        print('pin lama salah, silahkan periksa kembali pin anda')
    else:
        pin == pin_baru
        print('pin uang digital berhasil diperbaharui')

pilihan = None
jumlah = None
pin_lama = None
pin_baru = None
while True:
    print("""
    Selamat Datang di Aplikasi Uang Digital
    1. Informasi Saldo
    2. Ambil Saldo
    3. Tambah Saldo
    4. Transfer 
    5. Ganti pin
    """)
    pilihan = int(input("Silahkan Input Pilihan: "))
    if pilihan == 1:
        informasi_saldo()
    elif pilihan == 2:
        jumlah = int(input("Masukan jumlah saldo yang akan diambil: "))
        ambil_saldo(jumlah)
    elif pilihan == 3:
        jumlah = int(input("Masukan jumlah saldo yang akan ditambahkan: "))
        tambah_saldo(jumlah)
    elif pilihan == 4:
        kode_bank = str(input("Masukan kode bank: "))
        no_rek = str(input("Masukan no rekening: "))
        jumlah = int(input("Masukan jumlah uang yang akan ditransfer: "))
        transfer(jumlah)
    elif pilihan == 5:
        pin_lama = int(input("Masukan pin lama anda: "))
        pin_baru = int(input("Masukan pin baru anda: "))
        ganti_pin(pin_lama, pin_baru)
    else:
        print("Pilihan Salah")

    
