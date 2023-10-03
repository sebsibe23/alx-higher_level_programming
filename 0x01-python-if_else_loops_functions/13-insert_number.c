#include "lists.h"

/**
 * insert_node - the func Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the head of the linked list.
 * @number: a number to insert.
 *
 * Return: return If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *cunode = *head;
	listint_t *strn_node = malloc(sizeof(listint_t));

	if (strn_node == NULL) {
		return NULL;
	}

	strn_node->n = number;

	if (cunode == NULL || cunode->n >= number)
	{
		strn_node->next = cunode;
		*head = strn_node;
		return strn_node;
	}

	while (cunode && cunode->next && cunode->next->n < number)
	{
		cunode = cunode->next;
	}

	strn_node->next = cunode->next;
	cunode->next = strn_node;

	return strn_node;
}
