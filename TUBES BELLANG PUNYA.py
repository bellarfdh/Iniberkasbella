from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
font_ku = QFont("Times New Roman")
font_ku.setPointSize(8)
font_ku.setBold(True)

window = QMainWindow()
window.setGeometry(485, 300, 500, 160)
window.setWindowTitle('Sistem Informasi ITK')


# myfont = Qfont()
# myfont.setBold(True)
# myfont.setPointSize(14)

# username = QLabel(window)
# username.setText("Username : ")
# username.setFixedWidth(100)
# username.move(20, 20)
# ledit_username = QLineEdit(window)
# ledit_username.setText('')
# ledit_username.setToolTip('silahkan masukkan username anda')
# ledit_username.move(100, 20)
# ledit_username.setFixedWidth(300)
#
# password = QLabel(window)
# password.setText("Password : ")
# password.setFixedWidth(180)
# password.move(20, 60)
# ledit_password = QLineEdit(window)
# ledit_password.setText('')
# ledit_password.setToolTip('silahkan masukkan password anda')
# ledit_password.move(100, 60)
# ledit_password.setFixedWidth(300)
#


#HMSI
tombol_HMSI = QPushButton(window)
tombol_HMSI.move(200, 15)
tombol_HMSI.setText("HMSI")
tombol_HMSI.setFixedWidth(115)
tombol_HMSI.setFixedHeight(40)
tombol_HMSI.setFont(font_ku)

#DOSEN
tombol_Civitas = QPushButton(window)
tombol_Civitas.move(200, 59)
tombol_Civitas.setText("Civitas HMSI")
tombol_Civitas.setFixedWidth(115)
tombol_Civitas.setFixedHeight(40)
tombol_Civitas.setFont(font_ku)


#SI
tombol_SI = QPushButton(window)
tombol_SI.move(200, 103)
tombol_SI.setText("SI")
tombol_SI.setFixedWidth(115)
tombol_SI.setFixedHeight(40)
tombol_SI.setFont(font_ku)

# #Tumis kangkung
# tombol_Tumis = QPushButton(window)
# tombol_Tumis.move(200, 225)
# tombol_Tumis.setText("Tumis Kangkung")
# tombol_Tumis.setFixedWidth(100)
# tombol_Tumis.setFixedHeight(50)
#
# #Chookies
# tombol_Chookies = QPushButton(window)
# tombol_Chookies.move(200, 295)
# tombol_Chookies.setText("Chookies")
# tombol_Chookies.setFixedWidth(100)
# tombol_Chookies.setFixedHeight(50)

#Kodingan HMSI
secwindow = QMdiSubWindow()
secwindow.setGeometry(450, 300, 570, 160)
secwindow.setWindowTitle("Informasi Seputar HMSI")

username = QLabel(secwindow)
username.setText("Apa yang kalian ketahui tentang HMSI : ")
username.setFixedWidth(550)
username.move(13, 45)
username.setFont(font_ku)
ledit_username = QLineEdit(secwindow)
ledit_username.setText('')
ledit_username.setToolTip('silahkan masukkan jawaban anda')
ledit_username.move(235, 45)
ledit_username.setFixedWidth(300)

button_jawab = QPushButton(secwindow)
button_jawab.setText('Jawab')
button_jawab.move(345, 80)

thirdwindow = QMdiSubWindow()
thirdwindow.setGeometry(450, 300, 570, 160)
thirdwindow.setWindowTitle("Informasi Seputar HMSI")

username2 = QLabel(thirdwindow)
username2.setText("Apa kepanjangan dari HMSI : ")
username2.setFixedWidth(550)
username2.move(13, 45)
username2.setFont(font_ku)
ledit_username2 = QLineEdit(thirdwindow)
ledit_username2.setText('')
ledit_username2.setToolTip('silahkan masukkan jawaban anda')
ledit_username2.move(175, 45)
ledit_username2.setFixedWidth(300)

button_jawab2 = QPushButton(thirdwindow)
button_jawab2.setText('Jawab')
button_jawab2.move(285, 80)

Fourdwindow = QMdiSubWindow()
Fourdwindow.setGeometry(450, 300, 570, 160)
Fourdwindow.setWindowTitle("Informasi Seputar HMSI")

username3 = QLabel(Fourdwindow)
username3.setText("Kapan HMSI dibentuk di ITK : ")
username3.setFixedWidth(550)
username3.move(13, 45)
username3.setFont(font_ku)
ledit_username3 = QLineEdit(Fourdwindow)
ledit_username3.setText('')
ledit_username3.setToolTip('silahkan masukkan jawaban anda')
ledit_username3.move(187, 45)
ledit_username3.setFixedWidth(300)

button_jawab3 = QPushButton(Fourdwindow)
button_jawab3.setText('Jawab')
button_jawab3.move(287, 80)

Fivedwindow = QMdiSubWindow()
Fivedwindow.setGeometry(450, 300, 570, 160)
Fivedwindow.setWindowTitle("TABEL INFORMASI")

username4 = QLabel(Fivedwindow)
username4.setText("DISINI DIMASUKAN PENJELASAN LEBIH RINCI DARI KETIGA PERTANYAN TSB")
username4.setFixedWidth(550)
username4.move(13, 45)
username4.setFont(font_ku)

#Kodingan Civitas
sixdwindow = QMdiSubWindow()
sixdwindow.setGeometry(415, 300, 650, 160)
sixdwindow.setWindowTitle("Informasi seputar Civitas HMSI")


username5 = QLabel(sixdwindow)
username5.setText(" siapakah nama tenaga pendidik prodi SI? : ")
username5.setFixedWidth(550)
username5.move(13, 45)
username5.setFont(font_ku)
ledit_username5 = QLineEdit(sixdwindow)
ledit_username5.setText('')
ledit_username5.setToolTip('silahkan masukkan jawaban anda')
ledit_username5.move(315, 45)
ledit_username5.setFixedWidth(300)

button_jawab1_2 = QPushButton(sixdwindow)
button_jawab1_2.setText('Jawab')
button_jawab1_2.move(425, 80)

sevendwindow = QMdiSubWindow()
sevendwindow.setGeometry(455, 300, 590, 160)
sevendwindow.setWindowTitle("Informasi seputar Civitas HMSI")

username6 = QLabel(sevendwindow)
username6.setText(" Apakah kalian tau siapa nama ketua HMSI  : ")
username6.setFixedWidth(550)
username6.move(13, 45)
username6.setFont(font_ku)
ledit_username6 = QLineEdit(sevendwindow)
ledit_username6.setText('')
ledit_username6.setToolTip('silahkan masukkan jawaban anda')
ledit_username6.move(255, 45)
ledit_username6.setFixedWidth(300)

button_jawab2_2 = QPushButton(sevendwindow)
button_jawab2_2.setText('Jawab')
button_jawab2_2.move(365, 80)

eightdwindow = QMdiSubWindow()
eightdwindow.setGeometry(500, 300, 505, 160)
eightdwindow.setWindowTitle("Informasi seputar Civitas HMSI")

username7 = QLabel(eightdwindow)
username7.setText(" Berapa jumlah dosen SI? : ")
username7.setFixedWidth(550)
username7.move(13, 45)
username7.setFont(font_ku)
ledit_username7 = QLineEdit(eightdwindow)
ledit_username7.setText('')
ledit_username7.setToolTip('silahkan masukkan jawaban anda')
ledit_username7.move(165, 45)
ledit_username7.setFixedWidth(300)

button_jawab3_2 = QPushButton(eightdwindow)
button_jawab3_2.setText('Jawab')
button_jawab3_2.move(275, 80)

ninewindow = QMdiSubWindow()
ninewindow.setGeometry(450, 300, 570, 160)
ninewindow.setWindowTitle("TABEL INFORMASI")

username8 = QLabel(ninewindow)
username8.setText("DISINI DIMASUKAN PENJELASAN LEBIH RINCI DARI KETIGA PERTANYAN TSB")
username8.setFixedWidth(550)
username8.move(13, 45)
username8.setFont(font_ku)

#Kodingan SI
tenwindow = QMdiSubWindow()
tenwindow.setGeometry(450, 300, 570, 160)
tenwindow.setWindowTitle("Informasi Seputar SI")

username9 = QLabel(tenwindow)
username9.setText("Apa yang kalian ketahui tentang SI : ")
username9.setFixedWidth(550)
username9.move(13, 45)
username9.setFont(font_ku)
ledit_username9 = QLineEdit(tenwindow)
ledit_username9.setText('')
ledit_username9.setToolTip('silahkan masukkan jawaban anda')
ledit_username9.move(215, 45)
ledit_username9.setFixedWidth(300)

button_jawab1_3 = QPushButton(tenwindow)
button_jawab1_3.setText('Jawab')
button_jawab1_3.move(325, 80)

elevenwindow = QMdiSubWindow()
elevenwindow.setGeometry(440, 300, 590, 160)
elevenwindow.setWindowTitle("Informasi Seputar SI")

username10 = QLabel(elevenwindow)
username10.setText("Sebutkan bidang minat apa saja yang ada di SI : ")
username10.setFixedWidth(550)
username10.move(13, 45)
username10.setFont(font_ku)
ledit_username10 = QLineEdit(elevenwindow)
ledit_username10.setText('')
ledit_username10.setToolTip('silahkan masukkan jawaban anda')
ledit_username10.move(265, 45)
ledit_username10.setFixedWidth(300)

button_jawab2_3 = QPushButton(elevenwindow)
button_jawab2_3.setText('Jawab')
button_jawab2_3.move(375, 80)

# twelevewindow = QMdiSubWindow()
# twelevewindow.setGeometry(450, 300, 570, 160)
# twelevewindow.setWindowTitle("Informasi Seputar SI")
#
# username11 = QLabel(twelevewindow)
# username11.setText(" Siapakah nama tenaga pendidik prodi SI : ")
# username11.setFixedWidth(550)
# username11.move(13, 45)
# username11.setFont(font_ku)
# ledit_username11 = QLineEdit(twelevewindow)
# ledit_username11.setText('')
# ledit_username11.setToolTip('silahkan masukkan jawaban anda')
# ledit_username11.move(240, 45)
# ledit_username11.setFixedWidth(300)
#
# button_jawab3_3 = QPushButton(twelevewindow)
# button_jawab3_3.setText('Jawab')
# button_jawab3_3.move(350, 80)


# soal2 = QLabel(thirdwindow)
# soal2.setText("Apa itu HMSI : ")
# soal2.setFixedWidth(550)
# soal2.move(20, 100)
# ledit_soal2 = QLineEdit(thirdwindow)
# ledit_soal2.setText('')
# ledit_soal2.setToolTip('silahkan masukkan jawaban anda')
# ledit_soal2.move(220, 20)
# ledit_soal2.setFixedWidth(300)

# password = QLabel(QMdiSubWindow)
# password.setText("Password : ")
# password.setFixedWidth(180)
# password.move(20, 60)
# ledit_password = QLineEdit(QMdiSubWindow)
# ledit_password.setText('')
# ledit_password.setToolTip('silahkan masukkan password anda')
# ledit_password.move(100, 60)
# ledit_password.setFixedWidth(300)




#
# Sixdwindow = QMdiSubWindow()
# Sixdwindow.setGeometry(500, 185, 500, 365)
# Sixdwindow.setWindowTitle("Resep Tumis kangkung ")
#
# Sevendwindow = QMdiSubWindow()
# Sevendwindow.setGeometry(500, 185, 500, 365)
# Sevendwindow.setWindowTitle("Resep Chookies")

# daftar = QPushButton(secwindow)
# daftar.setText('lihat daftar Buku')
# daftar.move(350, 450)

#belum berguna
# font_welcome = QFont()
# font_welcome.setBold(True)
# font_welcome.setPointSize(18)
#Jawaban Tombol 1
def jawab_1():
    u = ['HMSI merupakan himpunan mahasiswa prodi sistem informasi']
    user = ledit_username.text()
    message_box = QMessageBox(secwindow)
    message_box.setWindowTitle('Kesalahan')
    if user in u:
        thirdwindow.show()
    else:
        message_box.setText('Jawaban anda kurang tepat ! Periksa kembali jawaban anda ')
        message_box.exec_()

button_jawab.clicked.connect(jawab_1)

def jawab_2():
    u = ['Himpunan mahasiswa sistem informasi']
    user = ledit_username2.text()
    message_box = QMessageBox(thirdwindow)
    message_box.setWindowTitle('Kesalahan')
    if user in u:
        Fourdwindow.show()
    else:
        message_box.setText('Jawaban anda kurang tepat ! Periksa kembali jawaban anda ')
        message_box.exec_()

button_jawab2.clicked.connect(jawab_2)

def jawab_3():
    u = ['AKU NGK TAU BEL WKWK']
    user = ledit_username3.text()
    message_box = QMessageBox(Fourdwindow)
    message_box.setWindowTitle('Kesalahan')
    if user in u:
        Fivedwindow.show()
    else:
        message_box.setText('Jawaban anda kurang tepat ! Periksa kembali jawaban anda ')
        message_box.exec_()

button_jawab3.clicked.connect(jawab_3)

#Jawaban tombol 2
def jawab2_1():
    u = ['ngak tau bel wkwk']
    user = ledit_username5.text()
    message_box = QMessageBox(sixdwindow)
    message_box.setWindowTitle('Kesalahan')
    if user in u:
        sevendwindow.show()
    else:
        message_box.setText('Jawaban anda kurang tepat ! Periksa kembali jawaban anda ')
        message_box.exec_()

button_jawab1_2.clicked.connect(jawab2_1)

def jawabb2_2():
    u = ['ngak tau bel wkwk']
    user = ledit_username6.text()
    message_box = QMessageBox(sevendwindow)
    message_box.setWindowTitle('Kesalahan')
    if user in u:
        eightdwindow.show()
    else:
        message_box.setText('Jawaban anda kurang tepat ! Periksa kembali jawaban anda ')
        message_box.exec_()

button_jawab2_2.clicked.connect(jawabb2_2)

def jawabb3_2():
    u = ['ngak tau bel wkwk']
    user = ledit_username7.text()
    message_box = QMessageBox(eightdwindow)
    message_box.setWindowTitle('Kesalahan')
    if user in u:
        ninewindow.show()
    else:
        message_box.setText('Jawaban anda kurang tepat ! Periksa kembali jawaban anda ')
        message_box.exec_()

button_jawab3_2.clicked.connect(jawabb3_2)

#Jawaban tombol 3
def jawabb1_3():
    u = ['ngak tau bel wkwk']
    user = ledit_username9.text()
    message_box = QMessageBox(tenwindow)
    message_box.setWindowTitle('Kesalahan')
    if user in u:
        elevenwindow.show()
    else:
        message_box.setText('Jawaban anda kurang tepat ! Periksa kembali jawaban anda ')
        message_box.exec_()

button_jawab1_3.clicked.connect(jawabb1_3)

def jawabb2_3():
    u = ['ngak tau bel wkwk']
    user = ledit_username9.text()
    message_box = QMessageBox(elevenwindow)
    message_box.setWindowTitle('Kesalahan')
    if user in u:
        twelevewindow.show()
    else:
        message_box.setText('Jawaban anda kurang tepat ! Periksa kembali jawaban anda ')
        message_box.exec_()

button_jawab2_3.clicked.connect(jawabb2_3)


def Pil1_ac():
    secwindow.show()

tombol_HMSI.clicked.connect(Pil1_ac)

def Pil2_ac():
    sixdwindow.show()

tombol_Civitas.clicked.connect(Pil2_ac)

def Pil3_ac():
    tenwindow.show()

tombol_SI.clicked.connect(Pil3_ac)

# def kangkung_ac():
#     Sixdwindow.show()
#
# tombol_Tumis.clicked.connect(kangkung_ac)
#
# def kue_ac():
#     Sevendwindow.show()
#
# tombol_Chookies.clicked.connect(kue_ac)

# font_ku = QFont("Verdana")
# font_ku.setPointSize(8)

window.show()
app.exec_()

