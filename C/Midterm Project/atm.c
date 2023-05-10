/*
Nama Program  : atm.c
Deskripsi     : Subprogram dari driverAtm.c.
Nama Pembuat  : Bintang Syafrian Rizal
NIM           : 24060122120031
Tanggal       : 29 Maret 2023 22:46
*/

#include <stdio.h>
#include <stdlib.h>
#include "atm.h"

void CekSaldo (){
    //Proses    : Menampilkan menu mesin ATM Bank Sodikun
    //I.S       : Sembarang
    //F.S       : Menampilkan informasi jumlah saldo akhir ke layar
   
    //Kamus Lokal
    
    //Algoritma
    printf("Saldo anda sekarang adalah sebesar Rp.%d\n", saldo);
}

void TarikTunai (){
    /*Proses    : Mengurangi nilai saldo dengan nominal yang ditarik,
                  nominal yang ditarik jumlahnya harus kurang dari saldo - 50000 */
    //I.S       : Saldo awal, input nominal jumlah yang ditarik
    //F.S       : Pesan informassi nominal yang ditarik, dan saldo akhir setelah penarikan dilakukan
   
    //Kamus Lokal
    int nominal;

    //Algoritma
    printf("Masukkan nominal yang ingin ditarik: Rp.");
    scanf("%d", &nominal);

    if(saldo > 0){ //Nominal tarik tunai tidak boleh lebih dari saldo, dan saldo yang tersimpan di atm harus lebih dari sama dengan 50.000
        if (saldo <= nominal-50000){
            printf("Maaf saldo anda tidak mencukupi.\n");
        }else {
            printf("Nilai yang ditarik: %d\n", nominal);
            printf("Saldo akhir anda adalah: Rp.%d\n", saldo-nominal);
            saldo -=nominal;
        }
    }else{
        printf("Masukkan nominal yang tepat.");
    }

}

void SetorTunai (){
    //Proses    : Menambahkan nilai saldo dengan nominal uang yang disetorkan
    //I.S       : Saldo awal, input nominal jumlah uang disetorkan
    //F.S       : Menampilkan informasi tentang nilai yang disetorkan dan saldo akhir setelah setor tunai dilakukan
    
    //Kamus Lokal
    int nominal;

    //Algoritma
    printf("Masukkan nominal yang ingin disetor: Rp. ");
    scanf("%d", &nominal);  
    if (nominal>0){
        saldo += nominal;
        printf("Saldo anda saat ini: Rp.%d\n",saldo);
    }else{
        printf("Masukkan nominal yang tepat.");
    }
}

void Keluar(){
    //Proses    : Menampilkan pesan keluar dari mesin ATM Bank Sodikun
    //I.S       : Sembarang
    //F.S       : Pesan keluar dari mesin ATM Bank Sodikun ditampilkan ke layar
    
    //Kamus Lokal

    //Algoritma
    printf("Terima kasih telah menggunakan mesin ATM Bank Sodikun\n");
    exit(0);
}

void menuJenisTrx(){
    //Proses    : Menampilkan menu mesin ATM Bank Sodikun
    //I.S       : Sembarang
    //F.S       : Menu jenis transaksi ditampilkan di layar

    //Kamus Lokal
    int x;

    //Algoritma
    scanf("%d", &x);
    if (x>=1 && x<=4){
        if (x==1){
            CekSaldo();
        }
        else if (x==2){
            TarikTunai();
        }
        else if (x==3){
            SetorTunai();
        }
        else if (x==4){
            Keluar();
        } else {
            printf("“Pilihan anda tidak valid. Pilihan valid adalah [1|2|3|4]. Silahkan coba lagi\n");
        }
    } else {
        printf("“Pilihan anda tidak valid. Pilihan valid adalah [1|2|3|4]. Silahkan coba lagi\n");
        menuJenisTrx();
    }
}