#include <stdio.h>
#include <stdlib.h>

int cmp(const void* a, const void* b) {
    return *(int*)a - *(int*)b;
}


int main() {
    int a[] = {4,5,3,2,1};
    qsort(a,5,sizeof(int),cmp);
    for(int i = 0 ; i < 5 ; i ++)
    printf("%d",a[i]);
}
