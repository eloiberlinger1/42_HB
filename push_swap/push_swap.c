/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 11:41:53 by eberling          #+#    #+#             */
/*   Updated: 2025/12/12 18:35:47 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	display(t_list *list)
{
	t_list *current;

	current = list;
	while (current != NULL)
	{
		printf("--- DEBUG LIST --- (valeur: %d | index: %d)\n", current->content, current->index);
		current = current->next;
	}
}

int	ft_check_dobble(t_list *list)
{
	t_list	*current;
	t_list	*runner;

	current = list;
	while (current != NULL && current->next != NULL)
	{
		runner = current->next;
		while (runner != NULL)
		{
			if (runner->content == current->content)
				return (1);
			runner = runner->next;
		}
		current = current->next;
	}
	return (0);
}

int	main(int argc, char **argv)
{
	t_list	*b;
	t_list	*a;

	b = NULL;
	a = parse_main(argc, argv);
	// Recuperer les valeurs entree
	if (ft_check_dobble(a))
	{
		ft_printf("Error\n");
		return (0);
	}
	// ft_swap(&a);
	// ft_sswap(&a, &b);
	// ft_push(&a, &b);
	// ft_push(&a, &b);
	// ft_rotate(&a);
	// ft_rev_rotate(&a);
	// ft_rrotate(&a);
	// ft_rrev_rotate(&a);
	// ft_rotate(&a);
	// lst_affect_index(a);
	// sort_small(&a, &b);
	// sort_main(&a, &b);
	
	// display list
	ft_printf("===============VALEURS a======================\n");
	display(a);
	ft_printf("===============VALEURS b======================\n");
	display(b);
	ft_printf("====================is sorted ? ==  %d ===========\n");
	// 	check_sort(a));
}

