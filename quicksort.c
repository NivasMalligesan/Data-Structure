// Online C compiler to run C program online
#include <stdio.h>
int sort(int arr[],int low ,int high){
    int pivot = low;
    int i = low;
    int j = high;
    
    while(i < j){
        while( i <= high && arr[pivot] <= arr[i]){
            i++;
        }
        while( j >= low && arr[pivot] > arr[j]){
            j--;
        }
        // printf("%d ",j);
        if(i<j){
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j]= temp;
        }
    }
    int temp = arr[pivot];
    arr[pivot] = arr[j];
    arr[j] =temp;
    
    return j;
}
void quick(int arr[],int low,int high){
    int partition;
    if(low <high){
        partition=sort(arr,low,high);
        quick(arr,low,partition-1);
        quick(arr,partition+1,high);
    }
}


int main() {
   int arr[6] = {5,5,5,5,5,5};
   quick(arr,0,5);
   for(int i = 0 ; i < 6 ; i ++)
   printf("%d ",arr[i]);
}
