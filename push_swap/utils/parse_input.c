/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   parse_input.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 18:31:42 by eberling          #+#    #+#             */
/*   Updated: 2025/12/13 16:50:10 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../push_swap.h"

/*
freelist = 1 if the list has to be freed
*/
static void	*stop_and_free(int must_free, char **args, t_list **a, int freelist)
{
	ft_putstr_fd("Error\n", 2);
	if (must_free)
		free_words(args, ft_lstsize(*a));
	if (freelist)
		ft_lstclear_no_funct(a);
	return (NULL);
}

static int	contains(char *s, char c)
{
	while (*s)
	{
		if (*s++ == c)
			return (1);
	}
	return (0);
}

static char	**get_args_list(int argc, char **argv, int *must_free, int *i)
{
	char	**args;

	args = NULL;
	*must_free = 0;
	*i = 1;
	if (argc == 2)
	{
		*i = 1;
		if (contains(argv[1], ' ') || ft_strlen(argv[1]) > 0)
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

static void	*input_to_list(char **args, int *i, int *must_free, t_list **a)
{
	t_list	*temp;
	int		value;
	int		p;
	int		has_digit;

	while (args[*i])
	{
		if (args[*i][0] == '\0')
			return (stop_and_free(*must_free, args, a, 0));
		p = 0;
		has_digit = 0;
		if (args[*i][p] == '+' || args[*i][p] == '-')
			p++;
		while (args[*i][p])
		{
			if (!ft_isdigit(args[*i][p]))
				return (stop_and_free(*must_free, args, a, 0));
			has_digit = 1;
			p++;
		}
		if (!has_digit)
			return (stop_and_free(*must_free, args, a, 0));
		if (ft_atoi(args[*i], &value) == NULL)
			return (NULL);
		temp = ft_lstnew(value);
		if (!temp)
			return (stop_and_free(*must_free, args, a, 1));
		ft_lstadd_back(a, temp);
		(*i)++;
	}
	return (*args);
}

t_list	*parse_main(int argc, char **argv)
{
	t_list	*a;
	char	**args;
	int		i;
	int		must_free;

	a = NULL;
	args = get_args_list(argc, argv, &must_free, &i);
	if (args == NULL)
		return (NULL);
	if (input_to_list(args, &i, &must_free, &a) == NULL)
		return (NULL);
	if (must_free == 1)
		free_words(args, ft_lstsize(a));
	return (a);
}
