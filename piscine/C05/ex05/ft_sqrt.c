/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/12 23:06:39 by eberling          #+#    #+#             */
/*   Updated: 2025/05/14 17:14:12 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_sqrt(int nb)
{
	int	i;
	int	res;

	if (nb < 0)
		return (0);
	i = 1;
	res = 0;
	while (res < nb)
	{
		res = i * i;
		if (res == nb)
			return (i);
		i++;
	}
	return (0);
}
/* 
int main(void)
{
	printf("square root of 99000 = %d", ft_sqrt(99000));
} */