EI_SDK?=edge-impulse-sdk
PYTHON_CROSS_PATH?=

UNAME_S := $(shell uname -s)

CFLAGS +=  -Wall -Wno-strict-aliasing
CFLAGS += -I.
CFLAGS += -I./libprocess/inc
CFLAGS += -O3
CFLAGS += -DNDEBUG
CFLAGS += -DEI_CLASSIFIER_ENABLE_DETECTION_POSTPROCESS_OP=1
ifeq (${CC}, clang)
	CFLAGS += -Wno-asm-operand-widths
endif
CXXFLAGS += -std=c++14
LDFLAGS += -lm -lstdc++

# Enable address sanitizer
CFLAGS += -fno-omit-frame-pointer -fsanitize=address
LDFLAGS += -fsanitize=address

CSOURCES = 
CXXSOURCES = test.cpp libprocess/src/libprocess.cpp
CCSOURCES =

ifeq (${DEBUG},1)
CFLAGS += -g
LDFLAGS += -g
endif

# Host specific
ifeq ($(OS),Windows_NT)
	MKDIR_BUILD = if not exist build mkdir build
else

ifeq ($(TARGET_ROCKCHIP),1)
	BUILD_DIR = build-rockchip
else
	BUILD_DIR = build
endif
	MKDIR_BUILD = mkdir -p $(BUILD_DIR)
endif
#end host specific

COBJECTS := $(patsubst %.c,%.o,$(CSOURCES))
CXXOBJECTS := $(patsubst %.cpp,%.o,$(CXXSOURCES))
CCOBJECTS := $(patsubst %.cc,%.o,$(CCSOURCES))

all: executable

.PHONY: runner clean executable

$(COBJECTS) : %.o : %.c
$(CXXOBJECTS) : %.o : %.cpp
$(CCOBJECTS) : %.o : %.cc

%.o: %.c
	$(CC) $(CFLAGS) -c $^ -o $@

%.o: %.cc
	$(CXX) $(CFLAGS) $(CXXFLAGS) -c $^ -o $@

%.o: %.cpp
	$(CXX) $(CFLAGS) $(CXXFLAGS) -c $^ -o $@

executable: $(COBJECTS) $(CXXOBJECTS) $(CCOBJECTS)
	$(MKDIR_BUILD)
	$(warning LDFLAGS is now $(LDFLAGS))
	$(CXX) -o $(BUILD_DIR)/$@  $(COBJECTS) $(CXXOBJECTS) $(CCOBJECTS) $(LDFLAGS)

clean:
	rm -f $(COBJECTS)
	rm -f $(CCOBJECTS)
	rm -f $(CXXOBJECTS)
	rm -f $(BUILD_DIR)/executable
