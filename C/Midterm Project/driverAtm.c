/*
Nama Program  : driverAtm.c
Deskripsi     : Program yang berupa implementasi dari cara kerja sebuah ATM.
Nama Pembuat  : Bintang Syafrian Rizal
NIM           : 24060122120031
Tanggal       : 29 Maret 2023 22:46
*/

#include <stdio.h>
#include <stdlib.h>
#include "atm.h"
#include "atm.c"

int main(){
    
    //Kamus Lokal
    int PIN;        //Inisialisasi PIN Pengguna = 9999
    int i;          //Iterator
    int option;     //Opsi Menu ATM 1-4
    char confirm;   //Opsi Konfirmasi Transaksi Ulang

    //Algoritma
    do{
        for (i=0 ; i<3 ; i++){
            printf("Masukkan PIN Anda: \n");
            scanf("%d", &PIN);

            if(PIN == 9999){
                break;
            } else{
                printf("Maaf PIN salah, silahkan coba lagi.\n");
            }
        }
        if (i == 3 && PIN != 9999){
            printf("Maaf kartu ATM anda diblokir, silahkan hubungi Bank Sodikun.\n");
            exit(0);
        }

        printf("            SELAMAT DATANG          \n");
        printf("        MESIN ATM BANK SODIKUN      \n");
        printf("=====================================\n");
        printf("<1> Cek Saldo\n");
        printf("<2> Tarik Tunai\n");
        printf("<3> Setor Tunai\n");
        printf("<4> Keluar\n");

        printf("Pilih menu ATM: ");
        menuJenisTrx();

        printf("Apakah anda ingin bertransaksi lagi?(Y/N)\n");
        scanf(" %c", &confirm);
    
    }while (confirm=='Y' || confirm=='y');

    printf("Terimakasih sudah menggunakan layanan mesin ATM Bank Sodikun.");

    return 0;
}