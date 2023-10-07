#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @PyOb: A PyObject list.
 */
void print_python_list_info(PyObject *PyOb)
{
	int strsize, stralloc, t;
	PyObject *obj;

	strsize = Py_SIZE(PyOb);
	stralloc = ((PyListObject *)PyOb)->allocated;

	printf("[*] Size of the Python List = %d\n", strsize);
	printf("[*] Allocated = %d\n", stralloc);

	for (t = 0; t < strsize; t++)
	{
		printf("Element %d: ", t);

		obj = PyList_GetItem(PyOb, t);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
