/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 11:41:53 by eberling          #+#    #+#             */
/*   Updated: 2025/12/08 09:24:15 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void affiche(int current)
{
    printf("--- DEBUG LIST --- (valeur: %d)\n", current);
}

int ft_check_dobble(t_list *list)
{
    t_list *current;
    t_list *runner;

    current = list;
    while (current != NULL && current->next != NULL)
    {
        runner = current->next;
        while (runner != NULL)
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
    t_list *b;
    t_list *temp;
    int i;
    int p;

    i = 1;
    a = NULL;
    b = NULL;
    // Recuperer les valeurs entree
    while (i < argc)
    {
        p = 0;
        while (argv[i][p]){
            if(!ft_isdigit(argv[i][p]))
                ft_printf("Quelque chose ici n'est %ppas un nombre.\n", b);
            p++;
        }
        
        // Adding int numbers in the link list
        temp = ft_lstnew(ft_atoi(argv[i]));
        if(!temp)
            return (0);
        ft_lstadd_back(&a, temp);

        i++;
    }

    if (ft_check_dobble(a))
    {
        printf("Comme une impression de schongesehn");
    }

    //ft_swap(&a);
    ft_push(&a, &b);
    //display list
    ft_lstiter(a, affiche);
}
