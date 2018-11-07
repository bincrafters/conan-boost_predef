#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires
import os


base = python_requires("boost_base/1.67.0@bincrafters/stable")

class BoostPredefConan(base.BoostBaseConan):
    name = "boost_predef"
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
        