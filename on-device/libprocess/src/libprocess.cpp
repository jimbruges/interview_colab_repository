#include "../inc/libprocess.hpp"

float process_data(float *signal, float *accelerometer, size_t win_size)
{
    float return_value = 0;

    for (size_t i = 0; i < win_size; ++i)
    {
        return_value += *(signal + i) + *(accelerometer + i * 3)
                                      + *(accelerometer + i * 3 + 1)
                                      + *(accelerometer + i * 3 + 2);
    }

    return return_value;
}
