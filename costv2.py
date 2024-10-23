from datetime import datetime
from typing import Dict, List, Optional

class CostManagement:
    def __init__(self, nama_produk: str):
        self.nama_produk = nama_produk
        self.direct_materials: Dict[str, float] = {}
        self.direct_labor: Dict[str, float] = {}
        self.overhead: Dict[str, float] = {}
        self.history: List[Dict] = []
        self.harga_jual: float = 0
        
    def tambah_material(self, nama: str, jumlah: float, harga_per_unit: float) -> None:
        """Menambahkan biaya material langsung"""
        total = jumlah * harga_per_unit
        self.direct_materials[nama] = total
        
    def tambah_tenaga_kerja(self, posisi: str, jam: float, upah_per_jam: float) -> None:
        """Menambahkan biaya tenaga kerja langsung"""
        total = jam * upah_per_jam
        self.direct_labor[posisi] = total
        
    def tambah_overhead(self, nama: str, biaya: float) -> None:
        """Menambahkan biaya overhead"""
        self.overhead[nama] = biaya
        
    def set_harga_jual(self, harga: float) -> None:
        """Menetapkan harga jual produk"""
        self.harga_jual = harga
        
    def hitung_total_material(self) -> float:
        """Menghitung total biaya material"""
        return sum(self.direct_materials.values())
        
    def hitung_total_labor(self) -> float:
        """Menghitung total biaya tenaga kerja"""
        return sum(self.direct_labor.values())
        
    def hitung_total_overhead(self) -> float:
        """Menghitung total biaya overhead"""
        return sum(self.overhead.values())
        
    def hitung_total_cost(self) -> float:
        """Menghitung total production cost"""
        return self.hitung_total_material() + self.hitung_total_labor() + self.hitung_total_overhead()
        
    def hitung_unit_cost(self, jumlah_unit: int) -> float:
        """Menghitung cost per unit"""
        if jumlah_unit <= 0:
            raise ValueError("Jumlah unit harus lebih dari 0")
        return self.hitung_total_cost() / jumlah_unit
        
    def analisis_profit(self) -> Dict:
        """Menganalisis profit dan margin"""
        if self.harga_jual <= 0:
            raise ValueError("Harga jual belum ditetapkan")
            
        total_cost = self.hitung_total_cost()
        profit = self.harga_jual - total_cost
        margin_percentage = (profit / self.harga_jual) * 100
        
        return {
            "total_cost": total_cost,
            "harga_jual": self.harga_jual,
            "profit": profit,
            "margin_percentage": margin_percentage
        }
        
    def simpan_perhitungan(self, jumlah_unit: int) -> None:
        """Menyimpan perhitungan ke dalam history"""
        tanggal = datetime.now()
        
        perhitungan = {
            "tanggal": tanggal,
            "materials": self.direct_materials.copy(),
            "labor": self.direct_labor.copy(),
            "overhead": self.overhead.copy(),
            "total_cost": self.hitung_total_cost(),
            "unit_cost": self.hitung_unit_cost(jumlah_unit),
            "jumlah_unit": jumlah_unit
        }
        
        if self.harga_jual > 0:
            perhitungan.update(self.analisis_profit())
            
        self.history.append(perhitungan)
        
    def generate_laporan(self) -> None:
        """Membuat laporan lengkap perhitungan cost"""
        print(f"\nLAPORAN PERHITUNGAN COST - {self.nama_produk}")
        print("=" * 50)
        
        # Direct Materials
        print("\nDIRECT MATERIALS:")
        for nama, biaya in self.direct_materials.items():
            print(f"{nama:20}: Rp {biaya:,.2f}")
        print(f"{'Total Materials':20}: Rp {self.hitung_total_material():,.2f}")
        
        # Direct Labor
        print("\nDIRECT LABOR:")
        for posisi, biaya in self.direct_labor.items():
            print(f"{posisi:20}: Rp {biaya:,.2f}")
        print(f"{'Total Labor':20}: Rp {self.hitung_total_labor():,.2f}")
        
        # Overhead
        print("\nOVERHEAD:")
        for nama, biaya in self.overhead.items():
            print(f"{nama:20}: Rp {biaya:,.2f}")
        print(f"{'Total Overhead':20}: Rp {self.hitung_total_overhead():,.2f}")
        
        # Total Manufacturing Cost
        print("\nTOTAL MANUFACTURING COST:")
        print("-" * 50)
        total_cost = self.hitung_total_cost()
        print(f"Total Cost        : Rp {total_cost:,.2f}")
        
        # Profit Analysis
        if self.harga_jual > 0:
            analisis = self.analisis_profit()
            print("\nANALISIS PROFIT:")
            print("-" * 50)
            print(f"Harga Jual       : Rp {analisis['harga_jual']:,.2f}")
            print(f"Total Cost       : Rp {analisis['total_cost']:,.2f}")
            print(f"Profit           : Rp {analisis['profit']:,.2f}")
            print(f"Margin           : {analisis['margin_percentage']:.2f}%")

# Contoh penggunaan
if __name__ == "__main__":
    # Inisialisasi produk
    kemeja = CostManagement("Kemeja Lengan Panjang")
    
    # Tambah biaya materials
    kemeja.tambah_material("Kain", 2, 25000)  # 2 meter @ Rp 25.000
    kemeja.tambah_material("Kancing", 10, 500)  # 10 buah @ Rp 500
    kemeja.tambah_material("Benang", 1, 5000)  # 1 gulung @ Rp 5.000
    
    # Tambah biaya tenaga kerja
    kemeja.tambah_tenaga_kerja("Penjahit", 3, 15000)  # 3 jam @ Rp 15.000
    kemeja.tambah_tenaga_kerja("QC", 0.5, 20000)  # 0.5 jam @ Rp 20.000
    
    # Tambah overhead
    kemeja.tambah_overhead("Listrik", 5000)
    kemeja.tambah_overhead("Perawatan Mesin", 3000)
    kemeja.tambah_overhead("Sewa Tempat", 10000)
    
    # Set harga jual
    kemeja.set_harga_jual(150000)
    
    # Simpan perhitungan untuk 100 unit
    kemeja.simpan_perhitungan(100)
    
    # Generate laporan
    kemeja.generate_laporan()
