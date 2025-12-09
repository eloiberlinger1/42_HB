/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 11:41:53 by eberling          #+#    #+#             */
/*   Updated: 2025/12/09 09:11:27 by eberling         ###   ########.fr       */
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
            if(!ft_isdigit(argv[i][p])) // Ajouter pour les + ou - ?? ==================================== ATTENTION
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
        printf("ERROR : 2 times same value");
        return (0);
    }

    //ft_swap(&a);
    //ft_push(&a, &b);
    ft_rotate(&a);
    ft_rev_rotate(&a);
    //display list
    ft_printf("===============VALEURS======================\n");
    ft_lstiter(a, affiche);
    ft_printf("=====================================\n");
    ft_lstiter(b, affiche);
    ft_printf("====================is sorted ? ==  %d ===========\n", check_sort(a));
}
