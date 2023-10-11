#include <stdio.h>
#include <Python.h>

/**
 * display_python_bytes - the func Displays byte
 * information of a Python object
 *
 * @p: Python Object
 * Return: no return
 */
void display_python_bytes(PyObject *p)
{
	char *var_byte_str;
	long int varbyte_size, varindex_, var_max_lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	varbyte_size = ((PyVarObject *)(p))->ob_size;
	var_byte_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", varbyte_size);
	printf("  trying string: %s\n", var_byte_str);

	if (varbyte_size >= 10)
		var_max_lim = 10;
	else
		var_max_lim = varbyte_size + 1;

	printf("  first %ld bytes:", var_max_lim);

	for (varindex_ = 0; varindex_ < var_max_lim; varindex_++)
		if (var_byte_str[varindex_] >= 0)
			printf(" %02x", var_byte_str[varindex_]);
		else
			printf(" %02x", 256 + var_byte_str[varindex_]);

	printf("\n");
}

/**
 * display_python_list - Displays list information of a Python object
 *
 * @p: Python Object
 * Return: no return
 */
void display_python_list(PyObject *p)
{
	long int list_size, varindex_;
	PyListObject *py_list;
	PyObject *item;

	list_size = ((PyVarObject *)(p))->ob_size;
	py_list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", py_list->allocated);

	for (varindex_ = 0; varindex_ < list_size; varindex_++)
	{
		item = ((PyListObject *)p)->ob_item[varindex_];
		printf("Element %ld: %s\n", varindex_, ((item)->ob_type)->tp_name);
		if (PyBytes_Check(item))
			display_python_bytes(item);
	}
}

