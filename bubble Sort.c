// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


void bubblesort(int *array,int size){
    bool swapped = 1;
    int len = size;
    
    for(int j = 0 ; j < len ; j ++){
        swapped =0 ;
        for(int i = 0 ; i < len-1 ; i++){
        if(array[i] > array[i+1]){
            int temp = array[i];
            array[i] = array[i+1];
            array[i+1] = temp;
            swapped = 1 ;
        }
    if(swapped == 0)break;
        }
    }
    printf("\n");
    for(int i = 0 ; i < len ; i ++){
        printf("%d ",array[i]);
    }
}



int main() {
    int size = 0;
    
    printf("Enter thye number of Size : ");
    scanf("%d",&size);
    
    int* array = (int*)malloc(size*sizeof(int));
    
    printf("Enter the Numbers ");
    for(int i = 0 ; i < size ; i ++){
        scanf("%d",&array[i]);
    }
    for(int i = 0 ; i < size ; i ++){
        printf("%d ",array[i]);
    }
    
    bubblesort(array, size);

  return 0;
}
