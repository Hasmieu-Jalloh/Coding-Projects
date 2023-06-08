#include <stdio.h>

int binarysearch(int nums[10], int target);

int main{
    int target = 9;
    int array[10] = {1,2,3,4,5,6,7,8,9,10};
    return 0;
}

int binarysearch(int nums[10], int target){
    int array_length = sizeof(nums) / sizeof(nums[0]);
    int upper_bound = array_length - 1;
    int lower_bound = 0;
    while (lower_bound <= upper_bound){
        int middle_val = (lower_bound + upper_bound) / 2;
        if (nums[middle_val] == target){
            return middle_val;
        } else if(nums[middle_val] < target){
            lower_bound = middle_val + 1;
        } else{
            upper_bound = middle_val - 1;
        }
    }
}