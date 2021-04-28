#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - intsrt a node
 * @head: the header
 * @n: the number
 * Return: NULL.
 */
listint_t *insert_node(listint_t **head, int n)
{
listint_t *new, *head2 = *head;
new = malloc(sizeof(listint_t));
if (new == '\0')
return ('\0');
new->n = n;
new->next = NULL;
if (head == NULL)
return ('\0');
while (head2->next != '\0' && head2->next->n < new->n)
head2 = head2->next;
new->next = head2->next;
head2->next = new;
return (new);
}
