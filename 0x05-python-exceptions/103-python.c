#include <Python.h>


void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);


/**
 *print_python_list - a function takes a Python list object
 * as input and displays its information.
 * It first checks if the input object is a valid Python list.
 * If not, it prints an error message and returns.
 * If the input is a valid Python list, it prints
 * a size of the list and the allocated size.
 * Then it iterates over each element in the list.
 * For each element, it checks its type.
 * If the element is of type Bytes, it calls a
 * function print_python_bytes.
 * If the element is of type Float,
 * it calls the function print_python_float.
 * For any other type, it prints the
 *type name of the element.
 *@p: python list object
 *Return : return null for error otherwise print python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, f;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	const char *var_invalid_msg = "  [ERROR] Invalid List Object\n";
	const char *str_list_info_msg = "[*] Python list info\n";
	const char *varsize_msg = "[*] Size of the Python List = %ld\n";
	const char *varalloc_msg = "[*] Allocated = %ld\n";
	const char *strelement_msg = "Element %ld: %s\n";

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);

	printf("%s", str_list_info_msg);
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("%s", var_invalid_msg);
		return;
	}

	printf(varsize_msg, size);
	printf(varalloc_msg, alloc);

	for (f = 0; f < size; f++)
	{
		type = list->ob_item[f]->ob_type->tp_name;
		printf(strelement_msg, f, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[f]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[f]);
	}
}



/**
 * print_python_bytes - This function takes a Python bytes
 * object as input and displays its information.
 * It first checks if the input object is a valid Python bytes object.
 *  If not, it prints an error message and returns.
 * If the input is a valid Python bytes object,
 *  it prints the size of the bytes object.
 * Then it tries to convert the bytes object to a string and prints it.
 * Finally, it prints the first 10 bytes of
 *a bytes object in hexadecimal format.
 * @p: python list object
 *
 *Return : return null for error display python bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t varsize, r;
	PyBytesObject *bytes = (PyBytesObject *)p;
	const char *b_info_msg = "[.] bytes object info\n";
	const char *varinvalid_msg = "  [ERROR] Invalid Bytes Object\n";
	const char *size_msg = "  size: %ld\n";
	const char *varstring_msg = "  trying string: %s\n";
	const char *varf_bytes_msg = "  first %ld bytes: ";

	fflush(stdout);

	printf("%s", b_info_msg);
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("%s", varinvalid_msg);
		return;
	}

	printf(size_msg, ((PyVarObject *)p)->ob_size);
	printf(varstring_msg, bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		varsize = 10;
	else
		varsize = ((PyVarObject *)p)->ob_size + 1;

	printf(varf_bytes_msg, varsize);
	for (r = 0; r < varsize; r++)
	{
		printf("%02hhx", bytes->ob_sval[r]);
		if (r == (varsize - 1))
			printf("\n");
		else
			printf(" ");
	}
}



/**
 * print_python_float - a function takes a Python float object
 * as input and displays its information.
 * .
 * If the input is a valid Python float object,
 *it prints the value of the float object.
 * @p: python list object
 *
 * Return: It first checks if the input object is a valid Python float object.
 * If not, it prints an error message and returns
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;
	PyFloatObject *varfloat_obj = (PyFloatObject *)p;
	const char *f_info_msg = "[.] float object info\n";
	const char *varinvalid_msg = "  [ERROR] Invalid Float Object\n";
	const char *varvalue_msg = "  value: %s\n";

	fflush(stdout);

	printf("%s", f_info_msg);
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("%s", varinvalid_msg);
		return;
	}

	buffer = PyOS_double_to_string(varfloat_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf(varvalue_msg, buffer);
	PyMem_Free(buffer);
}


