#include <Python.h>

void print_python_list_info(PyObject *p)
{
	int strsize = PyList_Size(p);
	int stralloc = ((PyListObject *)p)->allocated;
	PyObject *item;
	const char *item_type;

	printf("[*] Size of the Python List = %d\n", strsize);
	printf("[*] Allocated = %d\n", stralloc);

	for (int t = 0; t < strsize; t++) {
		item = PyList_GetItem(p, t);
		item_type = Py_TYPE(item)->tp_name;
		printf("Element %d: %s\n", t, item_type);
	}
}
