/************************************/
/* Program   : maintitik.c */
/* Deskripsi : aplikasi driver modul Titik */
/* NIM/Nama  : 24060122120031 - Bintang Syafrian Rizal */
/* Tanggal   : 1 September 2023*/
/***********************************/
#include <stdio.h>
#include "titik.h"
#include "titik.c"

int main() {
	//kamus main
    Titik A;
    Titik B;

	//algoritma
    printf("Halo, ini driver modul Titik\n");
	makeTitik(&A);
    setAbsis(&A,-3);
    setOrdinat(&A,4);
	printf("Absis A = %d\n", getAbsis(A));
    printf("Ordinat A = %d\n", getOrdinat(A));


    if (isOrigin(A)){
        printf("Titik A berada di origin\n");
    }
    else{
        printf("Titik A tidak berada di origin\n");
    }

    geserXY(&A, -6, 2);
    printf("Untuk menggeser, absis A menjadi = %d\n", getAbsis(A));
    printf("Untuk menggeser, ordinat A menjadi = %d\n", getOrdinat(A));

    refleksiSumbuX(&A);
    refleksiSumbuY(&A);
    printf("Untuk refleksi, absis A menjadi = %d\n", getAbsis(A));
    printf("Untuk refleksi, ordinat A menjadi = %d\n", getOrdinat(A));
    printf("Kuadran A = %d\n", Kuadran(A));

    setAbsis(&B, 6);
    setOrdinat(&B, -9);
    printf("Jarak A dan B = %.2f", distance(A, B));

	return 0;
}
