#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostAnyConan(base.BoostBaseConan):
    name = "boost_any"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_any"
    lib_short_names = ["any"]
    header_only_libs = ["any"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_mpl",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_index",
        "boost_type_traits"
    ]
