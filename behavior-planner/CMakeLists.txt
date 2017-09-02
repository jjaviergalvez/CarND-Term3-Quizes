project(planner)

cmake_minimum_required (VERSION 3.5)

add_definitions(-std=c++0x)

set(sources
    src/main.cpp
    src/vehicle.cpp
    src/vehicle.h
    src/road.cpp
    src/road.h)

add_executable(planner ${sources})
