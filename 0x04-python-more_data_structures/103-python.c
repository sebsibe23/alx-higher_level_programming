#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints some basic info
 * about the Python lists.
 * @p: a pointer to the Python object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t var_siz, h;
	PyObject *str_item;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		var_siz = PyList_Size(p);
		printf("[*] Size of the Python List = %ld\n", var_siz);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (h = 0; h < var_siz; h++)
		{
			str_item = PyList_GetItem(p, h);
			printf("Element %ld: %s\n", h, str_item->ob_type->tp_name);
			if (PyBytes_Check(str_item))
				print_python_bytes(str_item);
		}
	}
	else
	{
		printf(" Invalid List Object try again\n");
	}
}

/**
 * print_python_bytes - the func prints some basic info about
 * the Python bytes objects
 * @p: a pointer to a Python object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t var_siz, k;
	char *varstr;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		var_siz = PyBytes_Size(p);
		varstr = PyBytes_AsString(p);
		printf("  size: %ld\n", var_siz);
		printf("  trying string: %s\n", varstr);
		if (var_siz < 10)
			printf("  first %ld bytes: ", var_siz + 1);
		else
			printf("  first 10 bytes: ");
		for (k = 0; k <= var_siz && k < 10; k++)
		{
			printf("%02hhx", varstr[k]);
			if (k < var_siz && k < 9)
				printf(" ");
			else
				printf("\n");
		}
	}
	else
	{
		printf(" Invalid List Object try again\n");
	}
}

