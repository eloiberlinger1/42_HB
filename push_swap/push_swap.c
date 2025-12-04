/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 11:41:53 by eberling          #+#    #+#             */
/*   Updated: 2025/12/04 19:57:06 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int main(int argc, char **argv)
{
    // t_int_list *a;
    // t_int_list *b;
    int i;
    //int j;
    int p;

    i = 1;
    // Recuperer les valeurs entree
    while (i < argc)
    {
        // ft_input_check(argc, argv);
        p = 0;
        while (argv[i][p])
            if(!ft_isdigit(argv[i][p++]))
                ft_printf("Quelque chose ici n'est pas un nombre.\n");

        // checking for two times the same
        // j = 0;
        // while (j < argc)
        // {
        //     if (argv[i] == argv[j] && i != j)
        //         return (0);
        //     j++;
        // }

        i++;
    }
}
