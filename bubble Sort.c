#include <stdio.h>

int main() {
    int a[] = {5,4,2,3,1};
    int size = 5;
    for (int steps = 0 ; steps < size-1 ; i ++){
        int swapped = 0;
        for(int i = 0 ; i < size - steps - 1 ; i++){
            if(a[i] > a[i+1]){
                int temp = a[i];
                a[i+1] = a[i];
                a[i] = temp;
                swapped =1 ;
            }
        }
        if(swapped == 0){
            break;
        }
    }
    for(int i = 0 ; i < size ; i ++){
        printf("%d ",a[i]);
    }
    
    
    return 0;
}
