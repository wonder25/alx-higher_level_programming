#include "lists.h"

/**
 * insert_node - inserts number into list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: function fails return NULL, otherwise return pointer
 * to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;

	if (node == NULL || node-> n >= number)
	{
		temp->next = node;
		*head = temp;
		return (temp);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;
	temp->next = node->next;
	node->next = temp;

	return (temp);
}
