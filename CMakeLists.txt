cmake_minimum_required(VERSION 3.29)

project("MA527" VERSION 1.0.0 LANGUAGES CXX CUDA)

include(deps/conan/build/Release/generators/conan_toolchain.cmake)
include(GNUInstallDirs)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
set(CMAKE_CUDA_STANDARD 20)
set(CMAKE_CUDA_STANDARD_REQUIRED ON)
set(CMAKE_CUDA_EXTENSIONS OFF)

set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>DLL")

find_package(fmt REQUIRED)
find_package(CUDAToolkit REQUIRED)

set(EXE_NAME ma527)
add_executable(${EXE_NAME}
    src/Main.cpp)

target_link_libraries(${EXE_NAME} PRIVATE fmt::fmt)
target_link_libraries(${EXE_NAME} PRIVATE CUDA::cudart_static CUDA::cusolver)

if(MSVC)
    target_compile_options(${EXE_NAME} PRIVATE /W4 /WX)
    target_compile_options(${EXE_NAME} PRIVATE /arch:AVX2 /arch:AVX512)
endif()

install(TARGETS ${EXE_NAME}
    DESTINATION ${CMAKE_CURRENT_LIST_DIR}/install/${CMAKE_INSTALL_BINDIR})