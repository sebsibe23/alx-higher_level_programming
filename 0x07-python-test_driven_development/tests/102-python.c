#include "Python.h"

/**
 * print_python_string - This function prints details about Python string objects.
 * @python_obj: A PyObject string object.
 */
void print_python_string(PyObject *python_obj)
{
	long int str_length;

	fflush(stdout);  /* Clears the output buffer of stdout */

	printf("[.] string object info\n");  /* Prints the header for string object information */

	/* Verifies if the type of the PyObject is a string */
	if (strcmp(python_obj->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");  /* If not a string, prints an error message and returns */
		return;
	}

	str_length = ((PyASCIIObject *)(python_obj))->length;  /* Retrieves the length of the string */

	/* Determines if the string is a compact ascii or a compact unicode object */
	if (PyUnicode_IS_COMPACT_ASCII(python_obj))
		printf("  type: compact ascii\n");  /* If it's a compact ascii, prints this information */
	else
		printf("  type: compact unicode object\n");  /* If not, prints that it's a compact unicode object */

	printf("  length: %ld\n", str_length);  /* Prints the length of the string */

	/* Prints the value of the string */
	printf("  value: %ls\n", PyUnicode_AsWideCharString(python_obj, &str_length));
}

