#include <stdio.h>
#include <stdbool.h>

/*

c = 0, a = 1, b = 1
sum = 0, c = 1

c = 0, a = 1, b = 0
sum = 1, c = 0

c = 1, a = 1, b = 0
sum = 1, c = 0

c = 1, a = 1, b = 1
sum = 1, c = 1



  11
  11


 110


 */

bool bit_at(int num, int pos){
    return ((unsigned int)1 << pos) & num;
}

void set_bit(int *num, int pos){
    *num |= ((unsigned int)1 << pos);
}

int getSum(int a, int b){

    bool carry = false;
    int sum = 0;

    for(int i = 0; i < (sizeof(int) * 8); i++){

        bool bit_sum = carry ^ (bit_at(a, i) ^ bit_at(b, i));
        carry = (bit_at(a, i) & bit_at(b, i)) | (bit_at(b, i) & carry) + (bit_at(a, i) & carry);

        if(bit_sum)
            sum |= ((unsigned int)1 << i);
    }

    return sum;
}


int main(int argc, char const *argv[])
{
    /* code */

    int a = 13;
    int b = 100;

    int c = getSum(a, b);

    printf("a + b is: %d\n", c);
    return 0;
}
