from conans import ConanFile, CMake, tools

class CppsettingsConan(ConanFile):
    name = "cpp-settings"
    version = "0.2"
    license = "BSD"
    url = "https://gitlab.braintwister.eu/bernd/cpp-settings.git"
    description = "C++ library handling and parse settings"
    settings = {
        "os": ["Linux"],
        "compiler": ["gcc", "clang"],
        "build_type": ["Release", "Debug"],
        "arch": ["x86", "x86_64"]
    }
    generators = "cmake"

    def source(self):
        self.run("git clone https://gitlab.braintwister.eu/bernd/cpp-settings.git")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir="%s/cpp-settings" % self.source_folder)
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="cpp-settings")

    def package_info(self):
        self.cpp_info.libs = ["cpp-settings"]
