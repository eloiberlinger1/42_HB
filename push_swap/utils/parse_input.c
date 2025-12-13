/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_input.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 18:31:42 by eberling          #+#    #+#             */
/*   Updated: 2025/12/13 14:16:35 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

static void *stop_and_free(int must_free, char **args)
{
    ft_printf("Error\n");
    if (must_free)
        free(args);
    return (NULL);
}

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
    int     must_free;

    must_free = 0;
    i = 1;
    a = NULL;
    args = NULL;
	p = 0;
    if (argc == 2)
    {
        i = 1;
        if (contains(argv[1], ' '))
        {
            must_free = 1;
            args = ft_split(argv[1], ' ');
            if (args == NULL)
                return (NULL);
            i = 0;
        }
    }
    else
        args = argv;


    while (args[i])
	{
        p = 0;
		while (args[i][p])
		{
            // "654" "123" "-879" "45"
			if (!ft_isdigit(args[i][p]) && args[i][p] != '-' && args[i][p] != '+') // Ajouter pour les + ou
				return (stop_and_free(must_free, args));
			p++;
		}
		temp = ft_lstnew(ft_atoi(args[i]));
		if (!temp)
			return (0);
		ft_lstadd_back(&a, temp);
		i++;
	}
    if (must_free)
        free(args);
    return (a);
}
