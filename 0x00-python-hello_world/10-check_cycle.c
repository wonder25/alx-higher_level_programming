#include "lists.h"

/**
 * check_cycle - checks whether linked lists contains a cycle
 * @list: linked list
 * Return: 1 if linked lists has a cycle, 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (!list)
		return (0);

	while (a && b && b->next)
	{
		a = a->next;
		b = b->next->next;

		if (a == b)
			return (1);
	}

	return (0);
}
