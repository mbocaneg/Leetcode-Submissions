#include <stdio.h>

// [0,0,1,1,1,2,2,3,3,4]
//  ^P
//      ^Q
     
// [0,1,1,1,1,2,2,3,3,4]
//    ^P
//            ^Q
       
// [0,1,2,1,1,2,2,3,3,4]
//      ^P
//            ^Q

int removeDuplicates(int* nums, int numsSize){
    int *p = nums;
    int *q = nums + 1;

    int *offset = nums + numsSize;
    int count = 1;

    // printf("removing dupes\n");
    while(q < offset){
        if(*p != *q){
            *(p + 1) = *q;
            p += 1;
            count++;
        }
        else if(*p == *q){
            q += 1;
        }
    }

    return count;
}

int main(int argc, char const *argv[])
{
    int nums[] = {0,0,1,1,1,2,2,3,3,4};

    int nu_size = removeDuplicates(nums, sizeof(nums)/sizeof(nums[0]));

    for(int i = 0; i < nu_size; i++){
        printf("%d\n", nums[i]);
    }

    return 0;
}
 