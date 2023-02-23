/*
Nama Program  : jarakPBola.c
Deskripsi     : Menghitung dan menampilkan jarak yang ditempuh suatu benda yang mengalami gerak lurus berubah beraturan dengan rumus S = v0 * t + 1/2 * (a * t˛)
Nama Pembuat  : Bintang Syafrian Rizal
NIM           : 24060122120031
Tanggal       : Selasa, 21 Februari 2023 20:44 WIB
*/
#include <stdio.h>

int main()
{
    //Kamus Lokal
    float vnol, t, a, s;
    
    //Algoritma
    printf("Masukkan Angka: \n");
    scanf("%f",&vnol);
    scanf("%f",&t);
    scanf("%f",&a);
    
    s = vnol*t+0.5*(a*t*t);
    printf("Jaraknya yaitu: %f\n",s);
    return 0;
} 