#include "lists.h"
/**
 * check_cycle - checks if cycle is found in a linked list
 * @list: linked list to be checked
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *slower = list;
	listint_t *faster = list;

	if (!list)
		return (0);
	while (slower && faster && faster->next)
	{
		slower = slower->next;
		faster = faster->next->next;
		if (slower == faster)
			return (1);
	}
	return (0);
}
