# variabel yang menampung data bertipe list
ikan = ['Tuna', 'Hiu', 'Paus']
ekspor = ['Amerika', 'Asia', 'Eropa']
waktu = ['Biasa', 'Sedang', 'Cepat']

# untuk membuat server berjalan terus
while True:
    # Print Tulisan Toko ikan Internasional
    print('==== Toko Ikan International ====')

    # looping dari 0 sampai kurang dari panjang  list ikan (panjang  list ikan 3)
    # jadi variabel "i" nya nanti akan berisi perulangan mulai dari 0,1,2 karena panjang  list ikan nya cuma 3
    # lalu print ikan index ke "i" jadi output looping ini akan menjadi
    # ikan[0] (yang isi nya Tuna)
    # ikan[1] (yang isi nya Hiu)
    # ikan[2] (yang isi nya Paus)
    for i in range(0, len(ikan)):
        # "i" + 1 supaya tampilan nya mulai dari 1 karena variabel "i" awal nya dari 0
        print(f'{i+1}.{ikan[i]}')

    # membuat vriabel pilihan yang nanti nya berisi inputan user
    # untuk memilih ikan yang dipilih 1,2, atau 3 sesuai banyak nya list ikan
    # inputan di convert ke int supaya nanti bisa mengakses index dengan pilih
    pilih = int(input('Silahkan Pilih Ikan : '))
    # print tulisan ekspor
    print('==== ekspor ====')

    # looping dari 0 sampai kurang dari panjang list ekspor (panjang list ekspor 3)
    # jadi variabel "k" nya nanti akan berisi perulangan mulai dari 0,1,2 karena panjang list ekspor nya cuma 3
    # lalu print ekspor index ke "k" jadi output looping ini akan menjadi
    # ekspor[0]  (yang isi nya Amerika)
    # ekspor[1] (yang isi nya Asia)
    # ekspor[2] (yang isi nya Eropa)
    for k in range(0, len(ekspor)):
        # "k" + 1 supaya tampilan nya mulai dari 1 karena variabel "k" awal nya dari 0
        print(f'{k+1}.{ekspor[k]}')

    # membuat vriabel tujuan yang nanti nya berisi inputan user untuk memilih tujuan bedasarkan menu ekspor
    # untuk memilih ekspor yang digunakan
    tujuan = int(input('Silahkan Pilih ekspor : '))

    # print tulisan waktu
    # penjelasan kurang lebih sama dengan kedua di atas
    print('==== waktu ====')
    for l in range(0, len(waktu)):
        # "l" + 1 supaya tampilan nya mulai dari 1 karena variabel "l" awal nya dari 0
        print(f'{l+1}.{waktu[l]}')
    tipe = int(input('Silahkan Pilih waktu : '))

    # print bebas disini saya print hasil nya
    print('====================')
    # disini index nya di minus 1 karena yang ditampilkan
    # di layar saat menampilkan menu itu awal nya di plus 1 dan sekarang di kembalikan menjadi minus 1 lagi karena array / list dimulai dari 0
    print(f'Ikan : {ikan[pilih-1]}')
    print(f'ekspor : {ekspor[tujuan-1]}')
    print(f'Kecepatan Expor : {waktu[tipe-1]}')
    print('Sedang Di Proses')
    print('====================')
    # untuk inputan dari user apakah mau lanjut atau tidak
    # jika memasukan "y" maka akan continue / lanjut while lagi jika tidak maka akan break / berhenti
    lanjut = input('Apakah Mau Beli Ikan Lagi y/n ')
    if lanjut == 'y' or lanjut == 'Y':
        continue
    else:
        break
