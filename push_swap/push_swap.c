/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 11:41:53 by eberling          #+#    #+#             */
/*   Updated: 2025/12/10 10:15:31 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	display(int current)
{
	printf("--- DEBUG LIST --- (valeur: %d)\n", current);
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
	t_list	*a;
	t_list	*b;
	t_list	*temp;
	int		i;
	int		p;

	i = 1;
	a = NULL;
	b = NULL;
	// Recuperer les valeurs entree
	while (i < argc)
	{
		p = 0;
		while (argv[i][p])
		{
			if (!ft_isdigit(argv[i][p])) // Ajouter pour les + ou
				ft_printf("Quelque chose ici n'est %ppas un nombre.\n", b);
			p++;
		}
		// Adding int numbers in the link list
		temp = ft_lstnew(ft_atoi(argv[i]));
		if (!temp)
			return (0);
		ft_lstadd_back(&a, temp);
		i++;
	}
	if (ft_check_dobble(a))
	{
		printf("ERROR : 2 times same value");
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
	sort_small(&a, &b);
	//sort_main(&a, &b);
	
	// display list
	ft_printf("===============VALEURS a======================\n");
	ft_lstiter(a, display);
	ft_printf("===============VALEURS b======================\n");
	ft_lstiter(b, display);
	ft_printf("====================is sorted ? ==  %d ===========\n",
		check_sort(a));
}