cmake_minimum_required(VERSION 3.4.0)
project(BoostPythonExamples)


# when installing directly in CMake, redirect its intall root to dist dir
if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
    set (CMAKE_INSTALL_PREFIX "${CMAKE_SOURCE_DIR}/dist" CACHE PATH "default install path" FORCE )
endif()

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# get the suffix for python extension module and store in PYTHON_MODULE_EXTENSION
execute_process (COMMAND "${Python3_EXECUTABLE}" -c "from distutils import sysconfig;print(sysconfig.get_config_var('EXT_SUFFIX'))"
RESULT_VARIABLE _result
OUTPUT_VARIABLE PYTHON_MODULE_EXTENSION
ERROR_QUIET
OUTPUT_STRIP_TRAILING_WHITESPACE)

# be careful if using prebuilt Boost binary for Windows. It may not include one for your python version
set(BOOST_PYTHON_COMPONENT "python${Python3_VERSION_MAJOR}${Python3_VERSION_MINOR}")
set(BOOST_PYTHON_LIBRARY "Boost::${BOOST_PYTHON_COMPONENT}")
find_package(Boost REQUIRED COMPONENTS ${BOOST_PYTHON_COMPONENT})

add_subdirectory("src")
