#!/bin/bash

CONTAINER_NAME=$1

docker run --platform linux/amd64 --rm -it -v $PWD:/tmp/ ${CONTAINER_NAME} \
        sh -c "cd /tmp/ && \
               make -j8 \
               TARGET_ROCKCHIP=1 \
               CC='arm-rockchip830-linux-uclibcgnueabihf-gcc' \
               CXX='arm-rockchip830-linux-uclibcgnueabihf-g++' "
