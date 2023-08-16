#include "lists.h"

/**
 * check_cycle - checks runtime cycle
 * @list: linked list to be checked
 * Return: 1 if the list has a cycle, otherwise 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (list && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);

}
