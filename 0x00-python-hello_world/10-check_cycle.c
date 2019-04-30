#include "lists.h"
/**
 *check_cycle - verify if a linked list is circle
 *@list - pointer to list
 *Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *one_jump;
	listint_t *double_jump;
	
	one_jump = list;
	double_jump = list;
	while (one_jump != NULL && double_jump != NULL && double_jump->next != NULL)
	{
		one_jump = one_jump->next;
		double_jump = double_jump->next->next;
        
		return(one_jump == double_jump ? 1 : 0);
	}
	return (0);
}
