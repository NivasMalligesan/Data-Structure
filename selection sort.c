// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>

void swap(int *array, int i , int j){
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}

int selectionSort(int* array , int size){
    int i , j ;
    for( i = 0 ; i < size ; i ++){
        int min = i;
        for (j = i ; j < size ; j++){
            if(array[min] > array[j]){
                min = j;
            }
        }
        if(min != i){
            swap(array,i,min);
        }
    }
    printf("\n");
      for(int i = 0 ; i < size ; i ++){
        printf("%d ",array[i] );
    }
}


int main() {
    int size = 0 ;
    printf("Size : ");
    scanf("%d",&size);
    int* array = (int*)malloc(size*sizeof(int));
    printf("Enter the numbers : ");
    for(int i = 0 ; i < size ; i ++)
    scanf("%d",&array[i]);
    
    for(int i = 0 ; i < size ; i ++)
    printf("%d ",array[i]);
    
    selectionSort(array,size);
    
  

    return 0;
}
