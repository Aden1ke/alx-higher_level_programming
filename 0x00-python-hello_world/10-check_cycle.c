#include "lists.h"

/**
 * check_cycle - checks runtime cycle
 * @list: linked list to be checked
 * Return: 1 if the list has a cycle, otherwise 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *p2 = list;;
	listint_t *prev = list;;

	while (list && p2 && p2->next)
	{
		list = list->next;
		p2 = p2->next->next;

		if (list == p2)
		{
			list = prev;
			prev =  p2;
			while (1)
			{
				p2 = prev;
				while (p2->next != list && p2->next != prev)
				{
					p2 = p2->next;
				}
				if (p2->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
