#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle -find a cycle
 * @list: the header
 * Return: NULL.
 */
listint_t *insert_node(listint_t **head, int n)
{
  listint_t *new;
  new = malloc(sizeof(listint_t));
  if (new == '\0')
    return ('\0');
  new->n = n;
  new->next = *head;
  *head = new;
  return (new);
}
