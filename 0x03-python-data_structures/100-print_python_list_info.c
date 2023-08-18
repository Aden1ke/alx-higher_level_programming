#include <Python.h>
/**
 * print_python_list_info - basic info about Python lists.
 * @p: PyObject pointer.
 * Return:void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, mv;
	PyObject *item;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (mv = 0; mv < size; mv++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", mv, Py_TYPE(item)->tp_name);
	}
}
