# variable to hold the path to src folder to compute relative path of its decendents
set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR})

add_subdirectory("boost_python_example")

# copy all the py modules to dist folder
file(RELATIVE_PATH DST_DIR ${SRC_DIR} "${CMAKE_CURRENT_SOURCE_DIR}")
install(FILES ${PYFILES} DESTINATION ${DST_DIR} COMPONENT "PY") # copy all the py-files in dir
