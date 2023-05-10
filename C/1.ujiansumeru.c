#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h> 

int main(){
    int i;
    int n;
    int j;
    int barismax=0;
    int kolommax=0;
    int max=0;
    int matrix[50][50];


    scanf("Masukkan matrix berapa dimensi: %d", &n);
    for (i = 0 ; i < n ; i++){
        for (j = 0 ; j<n ; j++){
            scanf("Masukkan isi baris dan kolom matrix: %d", &matrix[i][j]);
        }
    }
    for (i = 0 ; i<n ; i++){
        barismax=0;
        kolommax=0;
        for (j = 0 ; j<n ; j++){
            barismax += matrix[i][j];
            kolommax += matrix [j][i];
        }
        if (barismax > max){
            max = barismax;
        } if (kolommax > max){
            max = kolommax;
        }
    }
    printf("%d", max);
    return 0;
}