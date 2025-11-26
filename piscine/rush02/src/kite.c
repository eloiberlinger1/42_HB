/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   kite.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dgeiss <dgeiss@student.42heilbronn.de>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/18 16:10:18 by dgeiss            #+#    #+#             */
/*   Updated: 2025/05/18 20:55:48 by dgeiss           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/my_core_bot.h"

t_obj	*ft_get_nearest_opponent_warr(t_obj *unit)
{
	t_obj	**enemies;
	t_obj	*near_op_w;
	int		i;

	enemies = ft_get_opponent_units();
	i = -1;
	while (enemies[++i] && !near_op_w)
		if (enemies[i]->s_unit.type_id == UNIT_WARRIOR)
			near_op_w = enemies[i];
	if (!near_op_w)
	{
		free(enemies);
		return (0);
	}
	i = -1;
	while (enemies[++i])
		if (ft_distance(unit, enemies[i]) < ft_distance(unit, near_op_w)
			&& enemies[i]->s_unit.type_id == UNIT_WARRIOR)
			near_op_w = enemies[i];
	free(enemies);
	return (near_op_w);
}

int	kite(t_obj *unit, t_obj **units)
{
	int		i;
	t_obj	*nearest_warr;

	nearest_warr = malloc(sizeof(t_obj));
	if (!nearest_warr)
		return (0);
	i = -1;
	while (units[++i] && !nearest_warr)
	{
		if (units[i]->s_unit.type_id == UNIT_WARRIOR && units[i]->state == 2)
			nearest_warr = units[i];
	}
	i = -1;
	while (units[++i])
	{
		if (ft_distance(unit, units[i]) < ft_distance(unit, nearest_warr)
			&& units[i]->s_unit.type_id == UNIT_WARRIOR && units[i]->state == 2)
			nearest_warr = units[i];
	}
	if (ft_distance(unit, nearest_warr) < 1200)
		return (0);
	if (ft_distance(unit, ft_get_nearest_opponent_warr(unit)) < 1200)
		return (1);
	return (0);
}
