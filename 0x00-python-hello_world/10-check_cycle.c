#include "lists.h"
/**
 * check_cycle -    This function checks if
 *a singly linked list has a cycle.
 *     It uses Floyd's Cycle-Finding Algorithm, also known
 *as the tortoise and the hare algorithm.
 *
 *@list: A pointer to the first node of a linked list.
 *
 * Return: int - Returns 1 if there is
 *a cycle in the list, otherwise returns 0.
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	int isCycle = 0;

	if (!list)
		return (isCycle);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			isCycle = 1;
			break;
		}
	}

	return (isCycle);
}
