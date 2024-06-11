from conan import ConanFile
from conan.tools.cmake import cmake_layout


class MA527(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"

    def requirements(self):
        self.requires("fmt/10.2.1")

    def layout(self):
        cmake_layout(self)
