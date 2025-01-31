#include <stdlib.h>

int cmp(const void* a,const void* b){
    return *(int*)a-*(int*)b;
}

int largestSumAfterKNegations(int* nums, int numsSize, int k) {
    int total = 0 ;
    qsort(nums,numsSize,sizeof(int),cmp);
    for(int i = 0 ; k > 0 && i < numsSize ; i++){
        if(nums[i] < 0){
           nums[i] = -nums[i]; 
           k--;
        }
    }
    qsort(nums,numsSize,sizeof(int),cmp);
    if(k % 2 == 1 ){
        nums[0] = -nums[0];
    }
    for(int i = 0 ; i < numsSize ; i ++){
        total+= nums[i];
    }
    return total;
}
