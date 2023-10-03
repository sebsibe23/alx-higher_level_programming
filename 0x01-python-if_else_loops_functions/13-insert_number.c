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
	listint_t *current = *head;
	listint_t *new_node;
	int is_head = (current == NULL || current->n >= number) ? 1 : 0;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (is_head)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	new_node->next = current->next;
	current->next = new_node;

	return (new_node);
}
