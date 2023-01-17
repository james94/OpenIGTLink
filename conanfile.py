from conans import ConanFile, CMake, tools
from conan.tools.cmake import CMakeToolchain
from conan.tools.layout import cmake_layout

def get_version():
    git = tools.Git()
    try:
        t = git.get_tag()
        print("t = {}".format(t))
        if t is not None:
            return "{}".format(t[1:])
        else:
            return "{}".format(git.get_revision())
    except:
        return None

class OpenIGTLinkConan(ConanFile):
    name = "OpenIGTLink"
    version = "3.1.0" #get_version()
    # Do I need requires and build_requires?

    build_requires = "gtest/1.11.0"
    generators = "cmake", "cmake_paths"

    # Optional metadata
    license = "BSD-3-Clause license"
    author = "James Guzman jamesmguzman94@gmail.com"
    url = "https://github.com/openigtlink/OpenIGTLink"
    description = "Free, open-source network communication library for image-guided therapy"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "Source/*", "Testing/*", "Examples/*", "Tools/*", "CMake/*", "*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
        
    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        cmake.install()
    
    def package_info(self):
        self.cpp_info.libs = ["OpenIGTLink"]
