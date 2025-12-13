/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_input.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 18:31:42 by eberling          #+#    #+#             */
/*   Updated: 2025/12/13 14:26:12 by eberling         ###   ########.fr       */
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

static void *stop_and_free_list(int must_free, char **args, t_list *a)
{
    ft_printf("Error\n");
    if (must_free)
        free(args);
    // free all the list
    return (NULL);
}

static int contains(char *s, char c)
{
    while (s++)
    {
        if (*s == c)
            return (1);
        }
    return (0);
}

static char **get_args_list(int argc, char **argv, int *must_free, int *i)
{
    char **args;
    
    args = NULL;
    *must_free = 0;
    *i = 1;
    if (argc == 2)
    {
        *i = 1;
        if (contains(argv[1], ' '))
        {
            *must_free = 1;
            args = ft_split(argv[1], ' ');
            if (args == NULL)
                return (NULL);
            *i = 0;
        }
    }
    else
        args = argv;
    return (args);
}

t_list *parse_main(int argc, char **argv)
{
    char **args;
    t_list	*a;
    t_list	*temp;
    int		p;
    int		i;
    int     must_free;

    a = NULL;
    args = get_args_list(argc, argv, &must_free, &i);
    while (args[i])
	{
        p = 0;
		while (args[i][p])
		{
			if (!ft_isdigit(args[i][p]) && args[i][p] != '-' && args[i][p] != '+')
				return (stop_and_free(must_free, args));
			p++;
		}
		temp = ft_lstnew(ft_atoi(args[i]));
		if (!temp)
			return (stop_and_free_list(must_free, args, a));
		ft_lstadd_back(&a, temp);
		i++;
	}
    if (must_free)
        free(args);
    return (a);
}
