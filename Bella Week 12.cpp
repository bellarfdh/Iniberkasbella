#include <iostream> 
#include <fstream> 
using namespace std;

int main(void){
    int buatarray[2][3] = {{2, 7, 1},{2,0,1}};


	ofstream CreateSave ("BellaNR27.txt"); 
	int row, colum;
	for (row = 0; row < 2; row++){
		for (colum = 0; colum < 3; colum++){
			CreateSave << buatarray [row][colum] << " ";

			}
			CreateSave << endl;
	}
	CreateSave.close();


	cout << "Array yang dimasukkan Telah tersimpan, Segera cek di File Project ";

	return 0;
}

