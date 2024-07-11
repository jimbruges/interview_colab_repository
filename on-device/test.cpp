
#include <vector>
#include <stdlib.h>
#include <stdio.h>

#include "libprocess.hpp"

#include "my_data.h"

#define ARRAY_LENGTH(array) (sizeof((array)) / sizeof((array)[0]))

// Same for accelerometer and signal
#define FS 100
#define WIN_SIZE 2 * FS
#define WIN_INC 2 * FS

int main(int argc, char *argv[])
{
    size_t sig_len = ARRAY_LENGTH(test_signal);
    size_t acc_len = ARRAY_LENGTH(test_accelerometer); // 3 axis

    float *signal = test_signal;
    float *accelerometer = test_accelerometer;

    printf("%d\n", sizeof(test_signal));

    printf("Before loop, SIG_LEN = %d, ACC_LEN = %d\n", sig_len, acc_len);
    for (int i = 0; i + WIN_SIZE <= sig_len; i += WIN_INC)
    {
        process_data(signal + i, accelerometer + i * 3, WIN_SIZE);
    }
    printf("After loop\n");

    return 0;
}
