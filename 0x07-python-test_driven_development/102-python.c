#include <Python.h>

/**
 * print_python_string - Print the information
 * about Python strings.
 * @p: A PyObject string object.
 *
 * This function takes a Python string
 * object as an argument and prints
 * detailed information about the string.
 * The information includes the type
 * of the string (either "compact ascii"
 * or "compact unicode object"),
 * the
 * length of the string, and the value of the string.
 *
 * If the input object is not a valid
 * Python Unicode string, the function
 * prints an error message and returns without
 * printing any further information.
 *
 * The function does not return a value.
 */
void print_python_string(PyObject *p)
{
	long int length;

	printf("[.] string object info\n");

	/* Validate input */
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	/* Get string length and value */
	length = PyUnicode_GET_LENGTH(p);

	/* Print string type, length, and value */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}

