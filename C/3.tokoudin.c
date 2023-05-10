#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdalign.h>

int main(){

    int promo=0;
    int reguler=0;
    int uang;
    int permen;

    scanf("%d", &uang);
    scanf("%d", &permen);

    if (permen * 5000 == uang){
        reguler += uang/5000;
    } else{
        promo += permen/5;
        reguler += permen%5;
    }

    printf("%d %d", promo, reguler);

    return 0;
}