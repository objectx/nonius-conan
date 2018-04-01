from conans import ConanFile, CMake, tools


class Nonius(ConanFile):
    name = "nonius"
    version = "1.2.0"
    license = "CC0"
    url = "https://github.com/libnonius/nonius"
    description = "A C++ micro-benchmarking framework"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = ("boost_lexical_cast/1.66.0@bincrafters/stable",
                "boost_optional/1.66.0@bincrafters/stable",
                "boost_math/1.66.0@bincrafters/stable",
                "boost_algorithm/1.66.0@bincrafters/stable")
    def source(self):
        tools.download("https://github.com/libnonius/nonius/releases/download/v1.2.0-beta.1/nonius-1.2.0-beta.1.zip",
                       "nonius.zip")
        tools.unzip("nonius.zip", "nonius")

    def package(self):
        self.copy("*.h++", dst="include", src="nonius")
