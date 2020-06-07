from cmaketools import setup

setup(
    name="boost_python_example",
    version="0.0.1",
    author="Takeshi (Kesh) Ikuma",
    author_email="tikuam@gmail.com",
    description="A test package using Boost::python",
    url="https://github.com/python-cmaketools/boost-python-example.git",
    license="MIT License",
    src_dir="src",
    ext_module_hint=r"Python3_add_library",
    has_package_data=True,
    configure_opts = ['-DBOOST_ROOT=C:\\Users\\tikum\\AppData\\Local\\Programs\\boost_1_71_0']
)
