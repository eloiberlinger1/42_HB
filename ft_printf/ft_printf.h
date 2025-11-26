/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eberling <eberling@student.42heilbronn.    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/22 12:24:46 by eberling          #+#    #+#             */
/*   Updated: 2025/11/04 17:26:53 by eberling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include "libft/libft.h"
# include <stdarg.h>
# include <stdint.h>
# include <stdio.h>
# include <stdlib.h>
# include <unistd.h>

int	process_int(va_list args);
int	process_uint(va_list args);
int	process_hex(va_list arg, int format);
int	process_ptr(va_list arg);
int	process_str(va_list args);
int	process_unknown(char f);
int	process_char(va_list args);
int	process(char s, va_list args);
int	ft_printf(const char *c, ...);

#endif