/*
Nama Program  : atm.h
Deskripsi     : Header.
Nama Pembuat  : Bintang Syafrian Rizal
NIM           : 24060122120031
Tanggal       : 29 Maret 2023 22:46
*/

#ifndef ATM_H
#define ATM_H

/* Prototype */

int saldo = 5000000;

void menuJenisTrx();
//Proses    : Menampilkan menu mesin ATM Bank Sodikun
//I.S       : Sembarang
//F.S       : Menu jenis transaksi ditampilkan di layar


void CekSaldo();
//Proses    : Menampilkan nilai saldo akhir
//I.S       : Sembarang
//F.S       : Menampilkan informasi jumlah saldo akhir ke layar

void TarikTunai();
/*Proses    : Mengurangi nilai saldo dengan nominal yang ditarik,
              nominal yang ditarik jumlahnya harus kurang dari saldo - 50000 */
//I.S       : Saldo awal, input nominal jumlah yang ditarik
//F.S       : Pesan informassi nominal yang ditarik, dan saldo akhir setelah penarikan dilakukan

void SetorTunai();
//Proses    : Menambahkan nilai saldo dengan nominal uang yang disetorkan
//I.S       : Saldo awal, input nominal jumlah uang disetorkan
//F.S       : Menampilkan informasi tentang nilai yang disetorkan dan saldo akhir setelah setor tunai dilakukan

void Keluar();
//Proses    : Menampilkan pesan keluar dari mesin ATM Bank Sodikun
//I.S       : Sembarang
//F.S       : Pesan keluar dari mesin ATM Bank Sodikun ditampilkan ke layar

#endif