#include "lists.h"

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *mid = NULL;
	listint_t *second_half = NULL;
	int isPalindrome = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev->next = NULL;
	reverse_listint(&second_half);

	listint_t *p1 = *head;
	listint_t *p2 = second_half;

	while (p1 != NULL && p2 != NULL)
	{
		if (p1->n != p2->n)
		{
			isPalindrome = 0;
			break;
		}

		p1 = p1->next;
		p2 = p2->next;
	}
	if (mid != NULL)
	{
		prev->next = mid;
		mid->next = second_half;
	}
	else
	{
		prev->next = second_half;
	}
	return (isPalindrome);
}
