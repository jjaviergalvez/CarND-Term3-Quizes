project(naive)

cmake_minimum_required (VERSION 3.5)

add_definitions(-std=c++0x)

set(sources
    src/main.cpp
    src/classifier.cpp
    src/classifier.h)

add_executable(naive ${sources})
