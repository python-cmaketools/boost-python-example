#include <iostream>
#include <string>
#include <sstream>

class Base 
{
public:
    virtual std::string name() const { return "Base"; }
    virtual ~Base() {}
};

class Derived : public Base
{
public:
    virtual std::string name() const { return "Derived"; }
};

std::string fb(Base *b)
{
    std::stringstream ss;
    ss << b->name() << " called.";
    return ss.str();
}

std::string fd(Derived *d)
{
    std::stringstream ss;
    ss << "Derived " << d->name() << " called.";
    return ss.str();
}

Base* factory()
{
    return new Derived;
}

#include <boost/python.hpp>
using namespace boost::python;

BOOST_PYTHON_MODULE(inheritance)
{
    class_<Base, boost::noncopyable>("Base")
        .def("name", &Base::name)
    ;

    class_<Derived, bases<Base> >("Derived")
    ;

    def("fb", fb);
    def("fd", fd);
    def("factory", factory, return_value_policy<manage_new_object>());
}	
