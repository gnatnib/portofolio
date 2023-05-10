#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i;
    int j;
    int n;
    int DNA[50];
    int saudara=0;
    int bukansaudara=0;
    
    scanf("%d", &n);
    if (n>0){
        for (i = 0 ; i <n ; i++){
        scanf("%d", &DNA[i]);
        }
        for ( i = 0 ; i < n ; i++){
            for (j = i+1 ; j<n ; j++){
                if (fabs(DNA[j] - DNA[i]) < 3){
                    saudara++;
                }else{
                    bukansaudara++;
                }
            }
        }
        printf("%d\n", saudara);
        printf("%d", bukansaudara);
    }else {
        printf("Tidak Valid");
    }
    return 0;
}
