#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>

uint32_t reverseBits(uint32_t n) {
    if(n == 0)
        return 0;
    uint32_t reversed = 0;

    int i = 31;

    while(n){
        if(1 & n)
            reversed |= (1 << i);

        i -= 1;
        n >>= 1;
    }
    return reversed;
}

int main(int argc, char const *argv[])
{
    /* code */

    uint32_t n = 0b00000010100101000001111010011100;
    uint32_t rev = reverseBits(n);

    printf("reversed bits: %" PRIu32 "\n", rev );

    return 0;
}
