#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);
/**
 * reverse_listint - Reverses the linked list.
 * @head: This is the double pointer to a
 * head of linked list.
 * Description: This function takes
 * a double pointer to the head of a linked
 * list and reverses the order of a nodes in the list.
 * a function returns
 * a pointer to a first node in a reversed list.
 *
 * Return: This function returns a pointer to
 * a first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{

	listint_t *node = *head, *next = NULL, *prev = NULL;
	int count = 0;

	while (node != NULL)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;


		count++;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - checks if the singly
 * linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Description: This function checks if the singly
 * linked list is a palindrome.
 * It first calculates the size of the list,
 * then checks if a list is a
 * palindrome by comparing elements from the start
 * and end of a list.
 *
 * Return: 1 if the list is a palindrome, and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *strtmp, *strrev, *strmid, *cur_str;
	size_t strsize = 0, f, strhalf;
	int s = 1;
	int e = 0;

	if (!*head || !(*head)->next)
		return (s);
	strtmp = cur_str = *head;
	while (cur_str)
	{
		strsize++;
		cur_str = cur_str->next;
	}
	strhalf = (strsize / 2) - 1;
	for (f = 0; f < strhalf; f++)
		strtmp = strtmp->next;
	if ((strsize % 2) == 0 && strtmp->n != strtmp->next->n)
		return (e);
	strtmp = strtmp->next->next;
	strrev = reverse_listint(&strtmp);
	strmid = strrev;
	cur_str = *head;
	while (strrev)
	{
		if (cur_str->n != strrev->n)
			return (e);
		cur_str = cur_str->next;
		strrev = strrev->next;
	}
	reverse_listint(&strmid);
	return (s);
}
