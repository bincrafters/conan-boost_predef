#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires
import os.path


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostPredefConan(base.BoostBaseConan):
    name = "boost_predef"
    version = "1.70.0"

    def package(self):
        super(BoostPredefConan, self).package()
        for subdir in ("check", "tools"):
            src_dir = os.path.join('predef', subdir)
            self.copy(
                pattern="*.jam",
                dst=os.path.join('predef', "lib", subdir),
                src=src_dir)
            self.copy(
                pattern="*.c*",
                dst=os.path.join('predef', "lib", subdir),
                src=src_dir)
            self.copy(
                pattern="*.m*",
                dst=os.path.join('predef', "lib", subdir),
                src=src_dir)
