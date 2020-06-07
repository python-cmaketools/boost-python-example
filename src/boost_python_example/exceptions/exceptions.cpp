#include "Python.h"

struct OutOfSteakException {};

void translateException( const OutOfSteakException& x) {
    PyErr_SetString(PyExc_UserWarning, "The meat is gone, go for the cheese....");
};

void someFunction() {
    throw OutOfSteakException();
};

#include "boost/python.hpp"
using namespace boost::python;

BOOST_PYTHON_MODULE(exceptions)
{
    register_exception_translator<OutOfSteakException>(translateException);

    def("someFunction", &someFunction);
}
