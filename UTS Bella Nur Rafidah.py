class Student:
    def __init__(self, nama, umur,tinggi,berat_badan,jenis_kelamin,matkul):
        self.nama  = nama
        self.umur = umur
        self.tinggi = tinggi
        self.berat = berat_badan
        self.gender = jenis_kelamin
        self.matkul = matkul
        
    def belajar(self,pelajaran):
        print("Mahasiswa yang bernama "+ self.nama +" sedang belajar "+pelajaran.matkul+" di gedung A")
        
    def membaca(self,buku):
        print("Mahasiswa yang bernama "+ self.nama +" sedang membaca sebuah buku "+buku.matkul+" di ruang perpustakaan")

    def berdiri(self,tugas):
        print(self.nama +" sedang dihukum berdiri di depan kelas karna tidak mengerjakan tugas "+tugas.matkul)

    def berjalan(self,lab,teman):
        print(self.nama +" sedang berjalan menuju lab "+lab.matkul+" bersama "+teman.nama)

student1 = Student("Bella",19,153,43,"perempuan","Biologi")
student2 = Student("Budi",24,160,59,"laki-laki","Fisika")
student3 = Student("Cintia",26,168,57,"perempuan","Kimia")

print("----- Mahasiswa Pertama -----")
student1.belajar(student1)
student1.membaca(student1)
student1.berdiri(student1)
student1.berjalan(student1,student2)
print("jumlah berat badan ketiganya adalah : ",student1.berat+student2.berat+student3.berat, "kg")
print("jumlah umur ketiganya adalah : ",student1.umur+student2.umur+student3.umur,"tahun")
print("")

print("----- Mahasiswa kedua -----")
student2.belajar(student2)
student2.membaca(student2)
student2.berdiri(student2)
student2.berjalan(student2,student3)
print("jumlah berat badan ketiganya adalah : ",student1.berat+student2.berat+student3.berat, "kg")
print("jumlah umur ketiganya adalah : ",student1.umur+student2.umur+student3.umur,"tahun")
print("")

print("----- Mahasiswa ketiga -----")
student3.belajar(student3)
student3.membaca(student3)
student3.berdiri(student3)
student3.berjalan(student3,student1)
print("jumlah berat badan ketiganya adalah : ",student1.berat+student2.berat+student3.berat, "kg")
print("jumlah umur ketiganya adalah : ",student1.umur+student2.umur+student3.umur,"tahun")
