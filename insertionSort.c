// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int a[] = {4,1,2,3,5};
    int size = 5;
    for(int i = 1 ; i < size ; i ++){
        int st = a[i];
        int j = i-1;
        while(j >= 0 && a[j]>st){
            a[j+1]=a[j];
            j = j -1;
        }
        a[j+1] = st;
    }
    for(int i = 0 ; i < size ; i ++){
        printf("%d ",a[i]);
    }
    
    return 0;
}
