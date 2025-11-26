/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_convert_base.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/14 22:23:20 by eberling          #+#    #+#             */
/*   Updated: 2025/05/18 16:22:17 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int		ft_strlen(char *str);
int		char_in_base(char c, char *base);
int		checkbase(char *str);
int		get_index(char c, char *base);
char	*ft_strcpy(char *dest, char *src);

int	ft_atoi_base(char *str, char *base)
{
	long int	result;
	int			digit;
	int			i;

	digit = 1;
	result = 0;
	i = 0;
	while ((str[i] == '\t' || str[i] == '\n' || str[i] == '\v'
			|| str[i] == '\f' || str[i] == '\r' || str[i] == ' '))
		i++;
	while (str[i] == '+' || str[i] == '-')
	{
		if (str[i] == '-')
			digit = digit * (-1);
		i++;
	}
	while (i < ft_strlen(str) && str[i] != '\0')
	{
		if (!char_in_base(str[i], base))
			break ;
		result = (result * ft_strlen(base)) + get_index(str[i], base);
		i++;
	}
	return (digit * result);
}

void	handleminus(long int *nb, char *result_rev)
{
	if (*nb < 0)
	{
		result_rev[0] = '-';
		*nb = -*nb;
	}
}

char	*ft_putnbr_base(char *result, int nbr, char *base)
{
	int			base_len;
	int			i;
	char		result_rev[1000];
	long int	longnbr;

	base_len = ft_strlen(base);
	longnbr = nbr;
	handleminus(&longnbr, result);
	i = 0;
	while (longnbr > 0)
	{
		result_rev[i++] = base[longnbr % base_len];
		longnbr = longnbr / base_len;
	}
	if (longnbr == 0 && i == 0)
	{
		result[0] = result_rev[0];
		return (result);
	}
	i--;
	base_len = ft_strlen(result);
	while (i >= 0)
		result[base_len++] = result_rev[i--];
	result[base_len] = '\0';
	return (result);
}

char	*ft_convert_base(char *nbr, char *base_from, char *base_to)
{
	long int		int_val;
	char			*result;
	char			*result_test;

	result = (char *) malloc(1000);
	result[0] = '\0';
	if (!checkbase(base_from) || !checkbase(base_to) || result == NULL)
		return (NULL);
	int_val = ft_atoi_base(nbr, base_from);
	if (int_val == 0)
	{
		result[0] = base_to[0];
		result[1] = '\0';
		return (result);
	}
	ft_putnbr_base(result, int_val, base_to);
	result_test = (char *) malloc(ft_strlen(result));
	ft_strcpy(result_test, result);
	free(result);
	return (result_test);
}

/* #include <stdio.h>
int main(void)
{
	printf("%s\n", ft_convert_base("i", "i~pv", "gYhQ_zUVuv"));
} */