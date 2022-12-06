#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * add_node_front - function to add node
 * @head: list
 * @n: number to add
 */
void add_node_front(listint_t **head, int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return;
	new->n = n;
	new->next = *head;
	*head = new;
}

/**
 * is_palindrome - function to see if a linked list is palindrom
 * @head: list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp1, *temp2, *head1;

	temp1 = *head;
	head1 = NULL;
	while (temp1->next != NULL)
	{
		add_node_front(&head1, temp1->n);
		temp1 = temp1->next;
	}
	add_node_front(&head1, temp1->n);

	temp1 = *head;
	temp2 = head1;
	while (temp2->next != NULL)
	{
		if (temp2->n != temp1->n)
		{
			free_listint(head1);
			return (0);
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	if (temp2->n != temp1->n)
	{
		free_listint(head1);
		return (0);
	}
	free_listint(head1);
	return (1);
}
