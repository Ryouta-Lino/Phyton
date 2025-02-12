import datetime

class Kasir:
    def __init__(self):
        # Inisialisasi daftar produk dengan harga
        self.daftar_produk = {
            'Mie Ayam Original': 10000,
            'Mie Ayam Polos': 7000,
            'Mie Ayam Bakso': 13000,
            'Mie Ayam Ceker': 13000,
            'Mie Ayam Komplit': 16000,
            'Bakso Original': 10000,
            'Es Jeruk': 5000,
            'Es Teh': 3000,
            'Es Cappucino': 5000,
            'Es Permen Karet': 5000,
            'Jeruk Hangat': 5000,
            'Teh Hangat': 3000,
        }
        # Inisialisasi pesanan
        self.pesanan = {}

    def tampilkan_produk(self):
        print("\n=== DAFTAR PRODUK ===")
        print("No  | Produk           | Harga")
        print("-" * 37)
        for idx, (produk, harga) in enumerate(self.daftar_produk.items(), 1):
            print(f"{idx:<4}| {produk:<16} | Rp {harga:,}")
        
        pilihan = input("\nIngin menambahkan produk ke pesanan? (y/n): ")
        if pilihan.lower() == 'y':
            self.tambah_ke_pesanan(tampilkan_daftar=False)

    def tambah_ke_pesanan(self, tampilkan_daftar=True):
        if tampilkan_daftar:
            self.tampilkan_produk()
        try:
            nomor_produk = int(input("\nMasukkan nomor produk: "))
            if 1 <= nomor_produk <= len(self.daftar_produk):
                produk = list(self.daftar_produk.keys())[nomor_produk-1]
                jumlah = int(input(f"Masukkan jumlah {produk} yang dibeli: "))
                if jumlah > 0:
                    if produk in self.pesanan:
                        self.pesanan[produk] += jumlah
                    else:
                        self.pesanan[produk] = jumlah
                    print(f"\n{jumlah} {produk} berhasil ditambahkan ke pesanan")
                    
                    print("\nPilih opsi:")
                    print("1. Tambah produk lain")
                    print("2. Proses pembayaran")
                    print("3. Kembali ke menu utama")
                    
                    while True:
                        pilihan = input("Masukkan pilihan (1-3): ")
                        if pilihan == "1":
                            return self.tambah_ke_pesanan()
                        elif pilihan == "2":
                            return self.proses_pembayaran()
                        elif pilihan == "3":
                            return
                        else:
                            print("\nPilihan tidak valid! Silakan pilih 1-3")
                else:
                    print("\nJumlah harus lebih dari 0!")
            else:
                print("\nNomor produk tidak valid!")
        except ValueError:
            print("\nMasukkan angka yang valid!")

    def hapus_dari_pesanan(self):
        if not self.pesanan:
            print("\nPesanan masih kosong!")
            return

        print("\n=== DAFTAR PESANAN ===")
        for idx, (produk, jumlah) in enumerate(self.pesanan.items(), 1):
            print(f"{idx}. {produk} ({jumlah})")

        try:
            nomor_produk = int(input("\nMasukkan nomor produk yang akan dihapus (0 untuk batal): "))
            if nomor_produk == 0:
                return
            if 1 <= nomor_produk <= len(self.pesanan):
                produk = list(self.pesanan.keys())[nomor_produk-1]
                del self.pesanan[produk]
                print(f"\n{produk} berhasil dihapus dari pesanan")
            else:
                print("\nNomor produk tidak valid!")
        except ValueError:
            print("\nMasukkan angka yang valid!")

    def hitung_total(self):
        total = 0
        for produk, jumlah in self.pesanan.items():
            total += self.daftar_produk[produk] * jumlah
        
        if total > 100000:
            diskon = total * 0.1  # Diskon 10%
            total = total - diskon
            return total, diskon
        return total, 0

    def proses_pembayaran(self):
        if not self.pesanan:
            print("\nPesanan masih kosong!")
            return

        total, diskon = self.hitung_total()
        print(f"\nTotal pesanan: Rp {total + diskon:,}")
        if diskon > 0:
            print(f"Diskon 10%: Rp {diskon:,}")
            print(f"Total setelah diskon: Rp {total:,}")
        
        while True:
            try:
                pembayaran_input = input("Masukkan jumlah uang: Rp ")
                pembayaran_clean = pembayaran_input.replace('.', '').replace(',', '')
                pembayaran = int(pembayaran_clean)
                
                if pembayaran >= total:
                    kembalian = pembayaran - total
                    waktu_transaksi = datetime.datetime.now()
                    self.cetak_struk(total, diskon, pembayaran, kembalian, waktu_transaksi)
                    self.pesanan.clear()
                    break
                else:
                    print("\nUang tidak mencukupi!")
            except ValueError:
                print("\nMasukkan angka yang valid!")

    def cetak_struk(self, total, diskon, pembayaran, kembalian, waktu):
        print("\n" + "="*40)
        print("           STRUK PEMBELIAN           ")
        print("="*40)
        print(f"Tanggal: {waktu.strftime('%Y-%m-%d')}")
        print(f"Waktu  : {waktu.strftime('%H:%M:%S')}")
        print("-"*40)
        print("Produk           Mie Ayam Kendil    Harga    Subtotal")
        print("-"*40)
        
        subtotal = 0
        for produk, jumlah in self.pesanan.items():
            harga = self.daftar_produk[produk]
            sub = harga * jumlah
            subtotal += sub
            print(f"{produk:<16}{jumlah:<8}Rp {harga:,} Rp {sub:,}")
        
        print("-"*40)
        print(f"Subtotal         : Rp {subtotal:,}")
        if diskon > 0:
            print(f"Diskon 10%       : Rp {diskon:,}")
        print(f"Total            : Rp {total:,}")
        print(f"Tunai            : Rp {pembayaran:,}")
        print(f"Kembalian        : Rp {kembalian:,}")
        print("="*40)
        print("          Terima Kasih           ")
        print("="*40)

def main():
    kasir = Kasir()
    while True:
        print("\n=== PROGRAM KASIR ===")
        print("1. Tampilkan Produk & Tambah ke Pesanan")
        print("2. Hapus dari Pesanan")
        print("3. Lihat Pesanan")
        print("4. Proses Pembayaran")

        pilihan = input("\nPilih menu (1-4): ")

        if pilihan == "1":
            kasir.tampilkan_produk()
        elif pilihan == "2":
            kasir.hapus_dari_pesanan()
        elif pilihan == "3":
            if not kasir.pesanan:
                print("\nPesanan masih kosong!")
            else:
                print("\n=== DAFTAR PESANAN ===")
                for produk, jumlah in kasir.pesanan.items():
                    harga = kasir.daftar_produk[produk]
                    print(f"{produk}: {jumlah} x Rp {harga:,} = Rp {jumlah*harga:,}")
                print(f"\nTotal: Rp {kasir.hitung_total()[0]:,}")
                
                print("\nPilih opsi:")
                print("1. Tampilkan Produk & Tambah ke Pesanan")
                print("2. Hapus dari Pesanan")
                print("3. Proses Pembayaran")
                
                opsi = input("Masukkan pilihan (1-3): ")
                if opsi == "1":
                    kasir.tampilkan_produk()
                elif opsi == "2":
                    kasir.hapus_dari_pesanan()
                elif opsi == "3":
                    kasir.proses_pembayaran()
                else:
                    print("\nPilihan tidak valid!")
        elif pilihan == "4":
            kasir.proses_pembayaran()
        else:
            print("\nPilihan tidak valid!")

if __name__ == "__main__":
    main()
