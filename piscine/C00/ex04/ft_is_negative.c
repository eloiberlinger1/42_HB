/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_negative.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/04/30 00:46:50 by eberling          #+#    #+#             */
/*   Updated: 2025/04/30 14:00:35 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_is_negative(int n)
{
	char	result_p;
	char	result_n;

	result_p = 'P';
	result_n = 'N';
	if (n >= 0)
	{
		write(1, &result_p, 1);
	}
	else
	{
		write(1, &result_n, 1);
	}
}
