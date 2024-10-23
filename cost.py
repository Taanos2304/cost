def cek_cost_produk(nama_produk, biaya_bahan, biaya_produksi, biaya_lainnya):
    """
    Fungsi untuk menghitung total cost suatu produk
    
    Parameters:
    nama_produk (str): Nama produk yang akan dihitung
    biaya_bahan (float): Biaya bahan baku
    biaya_produksi (float): Biaya produksi/pembuatan
    biaya_lainnya (float): Biaya tambahan lainnya
    
    Returns:
    dict: Dictionary berisi breakdown cost dan total
    """
    # Hitung total cost
    total_cost = biaya_bahan + biaya_produksi + biaya_lainnya
    
    # Buat breakdown dalam persentase
    persen_bahan = (biaya_bahan / total_cost) * 100
    persen_produksi = (biaya_produksi / total_cost) * 100
    persen_lainnya = (biaya_lainnya / total_cost) * 100
    
    # Buat laporan dalam bentuk dictionary
    hasil = {
        "nama_produk": nama_produk,
        "breakdown_biaya": {
            "biaya_bahan": {
                "nominal": biaya_bahan,
                "persentase": round(persen_bahan, 2)
            },
            "biaya_produksi": {
                "nominal": biaya_produksi,
                "persentase": round(persen_produksi, 2)
            },
            "biaya_lainnya": {
                "nominal": biaya_lainnya,
                "persentase": round(persen_lainnya, 2)
            }
        },
        "total_cost": total_cost
    }
    
    return hasil

def tampilkan_hasil(hasil):
    """
    Fungsi untuk menampilkan hasil perhitungan dengan format yang rapi
    """
    print(f"\nHasil Perhitungan Cost untuk {hasil['nama_produk']}")
    print("-" * 50)
    
    for kategori, data in hasil['breakdown_biaya'].items():
        print(f"{kategori.title():15}: Rp {data['nominal']:10,.2f} ({data['persentase']}%)")
    
    print("-" * 50)
    print(f"Total Cost      : Rp {hasil['total_cost']:10,.2f}")

# Contoh penggunaan
if __name__ == "__main__":
    # Input data produk
    hasil = cek_cost_produk(
        nama_produk="Kemeja",
        biaya_bahan=50000,
        biaya_produksi=30000,
        biaya_lainnya=20000
    )
    
    # Tampilkan hasil
    tampilkan_hasil(hasil)