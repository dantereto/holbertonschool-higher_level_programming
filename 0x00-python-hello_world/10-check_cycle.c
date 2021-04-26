#include "lists.h"
/**
 * check_cycle -find a cycle
 * @list: the header
 * Return: NULL.
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list, *fast = list;
while (slow != '\0' && fast != '\0' && fast != '\0')
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
slow = slow->next;
fast = fast->next->next;
}
return (0);
}
