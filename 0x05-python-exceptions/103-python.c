#!/usr/bin/python3
#include <stdio.h>
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
	int varindex = 0;
	int VarL_size = PyList_Size(p);
	int varall_size = PyList_GetAllocated(p);

	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", VarL_size);
	printf("[*] Allocated = %d\n", varall_size);

	for (varindex = 0; varindex < VarL_size; varindex++)
	{
		PyObject *element = PyList_GetItem(p, varindex);

		printf("Element %d: ", varindex);

		if (PyBytes_Check(element))
		{
			print_python_bytes(element);
		}
		else if (PyFloat_Check(element))
		{
			print_python_float(element);
		}
		else
		{
			printf("%s\n", Py_TYPE(element)->tp_name);
		}
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
	int k = 0;
	int b_size = PyBytes_GET_SIZE(p);
	PyObject *str_obj = PyObject_Str(p);

	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("  size: %d\n", b_size);



	if (str_obj != NULL)
	{
		printf("  trying string: %s\n", PyUnicode_AsUTF8(str_obj));
		Py_DECREF(str_obj);
	}

	printf("  first 10 bytes: ");
	for (k = 0; k < 10 && k < b_size; k++)
	{
		printf("%02x ", PyBytes_AS_STRING(p)[k]);
	}
	printf("\n");
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
	double float_value = PyFloat_AS_DOUBLE(p);

	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf("  value: %f\n", float_value);
}

