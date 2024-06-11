#include <cuda_runtime.h>
#include <fmt/format.h>

int main()
{
    // Check if there are any CUDA devices available
    int deviceCount;
    cudaGetDeviceCount(&deviceCount);
    if(deviceCount == 0) {
        fmt::print("No CUDA devices found\n");
        return 1;
    }

    // Print information about the currently selected CUDA device
    int cudaDevice;
    cudaGetDevice(&cudaDevice);
    cudaDeviceProp deviceProp;
    cudaGetDeviceProperties(&deviceProp, cudaDevice);
    fmt::print("CUDA Device {}:\n", cudaDevice);
    fmt::print("\tName: {}\n", deviceProp.name);
    fmt::print("\tCompute Capability: {}.{}\n", deviceProp.major, deviceProp.minor);
    fmt::print("\tTotal Global Memory: {}\n", deviceProp.totalGlobalMem);

    return 0;
}