/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush00.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/03 13:25:56 by eberling          #+#    #+#             */
/*   Updated: 2025/05/04 15:19:22 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_putchar(char c);

void	handle_condition(int n_line, int n_col, int y, int x)
{
	if (n_line == 0 || n_line == y - 1)
	{
		if (n_col == 0 || n_col == x - 1)
		{
			ft_putchar('o');
		}
		else
		{
			ft_putchar('-');
		}
	}
	else
	{
		if (n_col == 0 || n_col == x - 1)
		{
			ft_putchar('|');
		}
		else
		{
			ft_putchar(' ');
		}
	}
}

void	rush(int x, int y)
{
	int	n_line;
	int	n_col;

	if ((x < 0) || (y < 0))
	{
		return ;
	}
	n_line = 0;
	while (n_line < y)
	{
		n_col = 0;
		while (n_col < x)
		{
			handle_condition(n_line, n_col, y, x);
			n_col ++;
		}
		ft_putchar('\n');
		n_line ++;
	}
}
