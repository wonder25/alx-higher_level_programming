#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if singly linked list is a palindrome
 * @head: double pointer to head node of linked list
 * Return: 1 if palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *reverse_half = NULL;
	listint_t *temp;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = reverse_half;
		reverse_half = temp;
	}

	if (fast)
		slow = slow->next;

	while (reverse_half && slow)
	{
		if (reverse_half->n != slow->n)
			return (0);
		reverse_half = reverse_half->next;
		slow = slow->next;
	}
	return (1);
}
