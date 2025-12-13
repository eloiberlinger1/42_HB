/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_input.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 18:31:42 by eberling          #+#    #+#             */
/*   Updated: 2025/12/12 20:00:24 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

int contains(char *s, char c)
{
    while (s++)
    {
        if (*s == c)
            return (1);
        }
    return (0);
}

t_list *parse_main(int argc, char **argv)
{
    char **args;
    t_list	*a;
    t_list	*temp;
    int		p;
    int		i;

    i = 1;
    a = NULL;
	p = 0;
    if (argc == 2)
    {
        if (contains(argv[1], ' '))
        {
            printf("basd");
            args = ft_split(argv[1], ' ');
        }
    }
    else
        args = argv;
    while (i < argc)
	{
		while (args[i][p])
		{
			if (!ft_isdigit(args[i][p])) // Ajouter pour les + ou
				ft_printf("Error\n");
			p++;
		}
		temp = ft_lstnew(ft_atoi(args[i]));
		if (!temp)
			return (0);
		ft_lstadd_back(&a, temp);
		i++;
	}
    return (a);
}
