/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   my_core_bot.h                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dgeiss <dgeiss@student.42heilbronn.de>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/18 11:36:46 by dgeiss            #+#    #+#             */
/*   Updated: 2025/05/18 19:03:49 by dgeiss           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef MY_CORE_BOT_H
# define MY_CORE_BOT_H

# include "/core/con_lib.h"
# include <stdio.h>

void	worker_logic(t_obj *unit, t_obj *node, t_obj *closest_enemy,
			t_obj **units);
void	warrior_logic(int ticks, t_obj *unit, t_obj *closest_enemy,
			t_obj *node);
void	spawn(int ticker);
int		kite(t_obj *unit, t_obj **units);

#endif