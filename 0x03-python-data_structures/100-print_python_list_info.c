#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info -  print info of list of python
 *@p: python object
 *Return: return 0
 */
void print_python_list_info(PyObject *p)
{
int size = PyList_Size(p);
int i = 0;
int allocated = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", allocated);
for (i = 0; i < size; i++)
{
printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
}
