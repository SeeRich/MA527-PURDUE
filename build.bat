@echo off
SET BUILD_TYPE=Release
if defined DEBUG (
    SET BUILD_TYPE=Debug
)

@REM Build the dependencies using conan
SETLOCAL
conan install . --output-folder=deps/conan --build=missing --settings=build_type=%BUILD_TYPE%
ENDLOCAL

@REM clean the project
rmdir /s /q build

@echo on
@REM Build the project
cmake -S . -B build -G "Visual Studio 17 2022" -DCMAKE_BUILD_TYPE=%BUILD_TYPE%
cmake --build build --config %BUILD_TYPE%
cmake --install build --config %BUILD_TYPE%