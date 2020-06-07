#include <iostream>
#include <string>
#include <sstream>

class Base 
{
public:
    virtual std::string name() const { return "Base"; }
    virtual ~Base() {}
};

std::string identify(Base *b)
{
    std::stringstream ss;
    ss << b->name() << " called.";
    return ss.str();
}

#include <boost/python.hpp>
using namespace boost::python;

struct BaseWrap : Base, wrapper<Base>
{
    virtual std::string name() const
    {
        if (override n = this->get_override("name"))
            return n();
        return Base::name();
    }
    std::string default_name() const
    {
        return this->Base::name();
    }
};

BOOST_PYTHON_MODULE(virtualfunctionsinpython)
{
    class_<BaseWrap, boost::noncopyable>("Base")
        .def("name", &Base::name, &BaseWrap::default_name)
    ;

    def("identify", identify);
}	
