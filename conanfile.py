from conans import ConanFile, tools, os

class BoostPredefConan(ConanFile):
    name = "Boost.Predef"
    version = "1.64.0"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-predef"
    source_url = "https://github.com/boostorg/predef"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["predef"]

    def source(self):
        for lib_short_name in self.lib_short_names:
            self.run("git clone --depth=1 --branch=boost-{0} https://github.com/boostorg/{1}.git"
                     .format(self.version, lib_short_name)) 

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()