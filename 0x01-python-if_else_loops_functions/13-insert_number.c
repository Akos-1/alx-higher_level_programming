#include "lists.h"
/**
 * @head: pointer of the linked list head
 * @number: inputed number
 * Return: NULL if fail
 * Otherwise - a pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *current;
	current = malloc(sizeof(listint_t));

	if (current == NULL)
		return (NULL);
	current->n = number;
	if (node == NULL || node->n >= number)
	{
		current->next = node;
		*head = current;
		return (current);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	current->next = node->next;
	node->next = current;
	return (current);
}
