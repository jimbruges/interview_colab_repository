
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <cassert>

#include "libprocess.hpp"

#include "my_data.h"

#define ARRAY_LENGTH(array) (sizeof((array)) / sizeof((array)[0]))

// Same for accelerometer and signal
#define FREQ 100
#define WIN_SIZE 2 * FREQ // ?
#define WIN_STRIDE 2 * FREQ // ?

int main(int argc, char *argv[])
{
    size_t sig_len = ARRAY_LENGTH(test_signal); // 1 axis
    size_t acc_len = ARRAY_LENGTH(test_accelerometer); // 3 axis

    float *signal = test_signal;
    float *accelerometer = test_accelerometer;

    for (int i = 0; i + WIN_SIZE <= sig_len; i += WIN_STRIDE)
    {
        process_data(signal + i, accelerometer + i * 3, WIN_SIZE);
    }
    printf("After loop\n");

    return 0;
}
