/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/10 23:30:03 by eberling          #+#    #+#             */
/*   Updated: 2025/05/11 18:41:08 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

void	ft_putstr(char *str);
void	ft_putchar(char c);
int		**get_array(char *str);
void	display_array(int **array);
int		**calc_array(int **array);
int		ft_strlen(char *str);

int	is_valid_input(char *str)
{
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (str[i])
	{
		if (i % 2 == 0)
		{
			if (str[i] < '1' || str[i] > '4')
			{
				ft_putstr("Args Error\n");
				return (0);
			}
			count++;
		}
		else if (str[i] != ' ')
		{
			ft_putstr("Args Error\n");
			return (0);
		}
		i++;
	}
	if (count != 16 || ft_strlen(str) != 31)
	{
		ft_putstr("Args Error\n");
		return (0);
	}
	return (1);
}

int	main(int argc, char *argv[])
{
	char	*user_input;
	int		**array;


	if (argc == 2 && is_valid_input(argv[1]))
	{
		user_input = argv[1];
		array = get_array(user_input);
		calc_array(array);
		//display_array(array);
	}
	else
	{
		ft_putstr("Args Error"); 
		return (1);
	}

	return (0);
}