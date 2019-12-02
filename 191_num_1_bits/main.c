#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>

// int hammingWeight(uint32_t n) {
//     if(n == 0)
//         return 0;

//     uint8_t count = 0;

//     for(uint8_t i = 0; i < 32; i++){
//         uint32_t bit = ((uint32_t)1 << i) & n;
//         if(bit)
//             count += 1;
//     }

//     return count;
// }

int hammingWeight(uint32_t n) {
    if(n == 0)
        return 0;
    int count = 0;
    while(n){
        if(1 & n)
            count += 1;
        n = n >> 1;
    }
    return count;
}

int main(int argc, char const *argv[])
{
    // uint32_t n = 11;
    // uint32_t n = 128;

    uint32_t n = 0b11111111111111111111111111111101;

    int hamming_weight = hammingWeight(n);
    printf("hamming weight: %d\n", hamming_weight);
    /* code */
    return 0;
}
