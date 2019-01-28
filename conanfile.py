#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires
import os


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostPredefConan(base.BoostBaseConan):
    name = "boost_predef"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_predef"
    lib_short_names = ["predef"]
    header_only_libs = ["predef"]

    def package_additional(self):
        for lib_short_name in self.lib_short_names:
            for subdir in ("check","tools"):
                src_dir = os.path.join(lib_short_name, subdir)
                self.copy(pattern="*.jam", dst=os.path.join(lib_short_name, "lib", subdir), src=src_dir)
                self.copy(pattern="*.c*", dst=os.path.join(lib_short_name, "lib", subdir), src=src_dir)
                self.copy(pattern="*.m*", dst=os.path.join(lib_short_name, "lib", subdir), src=src_dir)

    def package_info_additional(self):
        # boost_generator finds .jam files for this library using libdirs variable
        for lib_short_name in self.lib_short_names:
            self.cpp_info.libdirs.append(os.path.join(lib_short_name, "lib"))
