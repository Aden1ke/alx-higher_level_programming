#include "list.h"
int is_palindrome(listint_t **head)
{
	listint_t *back, *front = *head;
	listint_t *tmp = *head;

	if (head == NULL && *head ==  NULL)
		return (1);
	while (*head)
	{
		back = back->next;
		front = head->next;
		if (back->next == NULl)
		{
			if (tmp->next == back)
				continue;
			tmp = tmp->next;
		}
		if (front->n == back->n)
		{
			back = tmp;
			front = front->next
		}

	}
}
