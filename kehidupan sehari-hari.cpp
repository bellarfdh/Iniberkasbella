#include <iostream>
using namespace std;

int main(void)
{
    int nama;
    cout << "10201020_Bella Nur Rafidah";
    cout << "Menu Makanan" << endl;
    cout << "1. Nasi Padang" << endl;
    cout << "2. Nasi Goreng" << endl;
    cout << "Masukkan Pilihan Anda : ";
    cin >> nama;

    switch (nama)
    {
    case 1:
        cout << "Anda memesan nasi padang" << endl;
        break;
    case 2:
        cout << "Anda memesan nasi goreng" << endl;
        break;
    default:
        cout << "Pasti yang mesan cewe " << endl;
    }
    return 0;
}
