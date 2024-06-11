@echo off
SET BUILD_TYPE=Release
if defined DEBUG (
    SET BUILD_TYPE=Debug
)

@echo on
@REM Build the project
cmake --build build --config %BUILD_TYPE%
cmake --install build --config %BUILD_TYPE%