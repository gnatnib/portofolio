/************************************/
/* Program   : titik.c */
/* Deskripsi : realisasi body modul Titik */
/* NIM/Nama  : 24060122120031 - Bintang Syafrian Rizal */
/* Tanggal   : 1 September 2023*/
/***********************************/
#include <stdio.h>
#include <stdlib.h>
#include "titik.h"
#include <math.h>

void makeTitik(Titik *T){
    //kamus lokal

    //algoritma
    (*T).absis = 0;
    (*T).ordinat = 0;
}

int getAbsis(Titik T){
    //kamus lokal

    //algoritma
    return T.absis;
}

int getOrdinat(Titik T){
    //kamus lokal

    //algoritma
    return T.ordinat;
}

void setAbsis(Titik *T, int xx){
    //kamus

    //algoritma
    (*T).absis = xx;
}

void setOrdinat(Titik *T, int yy){
    //kamus lokal

    //algoritma
    (*T).ordinat = yy;
}

boolean isOrigin(Titik T){
    //kamus lokal

    //algoritma
    return T.absis == 0 && T.ordinat == 0;
}

void geserXY(Titik *T, int dx, int dy){
    //kamus lokal

    //algoritma
    (*T).absis += dx;
    (*T).ordinat += dy;
}

void refleksiSumbuX(Titik *T){
    //kamus lokal

    //algoritma
    (*T).absis *= -1;
}

void refleksiSumbuY(Titik *T){
    //kamus lokal

    //algoritma
    (*T).ordinat *= -1;
}

int Kuadran(Titik T){
    if(getAbsis(T) >= 0 && getOrdinat(T) >= 0){
        return 1;
    }else if(getAbsis(T) < 0 && getOrdinat(T) >= 0){
        return 2;
    }else if(getAbsis(T) < 0 && getOrdinat(T) < 0){
        return 3;
    }else{
        return 4;
    }
}

float distance(Titik T1, Titik T2){
    return sqrt(((T2.absis-T1.absis)*(T2.absis-T1.absis)) + ((T2.ordinat-T1.ordinat)*(T2.ordinat-T1.ordinat)));
}



