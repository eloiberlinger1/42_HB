/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/13 23:11:30 by eberling          #+#    #+#             */
/*   Updated: 2025/05/14 00:03:11 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] != '\0' || s2[i] != '\0')
	{
		if (s1[i] != s2[i])
		{
			return (((unsigned char)(s1[i])) - ((unsigned char)(s2[i])));
		}
		i++;
	}
	return (0);
}

void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		write(1, &str[i], 1);
		i++;
	}
}

void	sort_argv_in_less_than_25_lines_for_holy_norm(int argc, char *argv[])
{
	int		i;
	int		n;
	char	*ptr;

	n = 1;
	while (n < argc)
	{
		i = 1;
		while (i < argc - 1)
		{
			while (ft_strcmp(argv[i], argv[i + 1]) > 0)
			{
				ptr = argv[i];
				argv[i] = argv[i + 1];
				argv[i + 1] = ptr;
			}
			i++;
		}
		n++;
	}
}

int	main(int argc, char *argv[])
{
	int		i;

	sort_argv_in_less_than_25_lines_for_holy_norm(argc, argv);
	i = 1;
	while (i < argc)
	{
		ft_putstr(argv[i++]);
		write(1, "\n", 1);
	}
	return (0);
}
