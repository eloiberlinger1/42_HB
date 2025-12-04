/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 11:41:53 by eberling          #+#    #+#             */
/*   Updated: 2025/12/04 21:00:28 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int ft_check_dobble(t_list *list)
{
    t_list *current;
    t_list *runner;

    current = list;
    while (current != NULL && current->next != NULL)
    {
        runner = current;
        while (runner->next)
        {
            if(runner->content == current->content)
            {
                return (1);
            }
            runner = runner->next;
        }
        current = current->next;
    }
    return (0);
}

int main(int argc, char **argv)
{
    t_list *a;
    // t_int_list *b;
    int i;
    int p;
    int current;

    i = 1;
    a = NULL;
    // Recuperer les valeurs entree
    while (i < argc)
    {
        p = 0;
        while (argv[i][p]){
            if(!ft_isdigit(argv[i][p]))
                ft_printf("Quelque chose ici n'est pas un nombre.\n");
            p++;
        }
        
        // Adding int numbers in the link list
        current = ft_atoi(argv[i]);
        ft_lstadd_back(&a, ft_lstnew(current));

        i++;
    }

    if (!ft_check_dobble(a))
    {
        printf("Comme une impression de schongesehn");
    }
}
