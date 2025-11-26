/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   logic.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dgeiss <dgeiss@student.42heilbronn.de>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/18 11:15:56 by dgeiss            #+#    #+#             */
/*   Updated: 2025/05/18 19:13:13 by dgeiss           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/my_core_bot.h"

void	worker_logic(t_obj *unit, t_obj *node,
						t_obj *closest_enemy, t_obj **units)
{
	t_obj	*core;
	t_obj	*enemy_core;

	core = ft_get_my_core();
	enemy_core = ft_get_first_opponent_core();
	if (kite(unit, units))
		ft_travel_to_obj(unit, core);
	else if (node)
		ft_travel_attack(unit, node);
	else if (closest_enemy)
		ft_travel_attack(unit, closest_enemy);
	else
		ft_travel_attack(unit, enemy_core);
}

void	warrior_logic(int ticks, t_obj *unit, t_obj *closest_enemy,
						t_obj *node)
{
	t_team	*team;
	t_obj	*enemy_core;

	enemy_core = ft_get_first_opponent_core();
	team = ft_get_my_team();
	if (ticks < 400)
	{
		if (team->id == 1)
			ft_travel_to(unit, 2000, 200);
		if (team->id == 2)
			ft_travel_to(unit, 8000, 8000);
	}
	else if (closest_enemy && ticks >= 500)
		ft_travel_attack(unit, closest_enemy);
	else if (node)
		ft_travel_attack(unit, node);
	else
		ft_travel_attack(unit, enemy_core);
}

void	spawn(int ticker)
{
	t_team	*team;

	team = ft_get_my_team();
	if (ticker > 300)
		ft_create_unit(UNIT_WARRIOR);
	if (team->balance > 1500)
	{
		ft_create_unit(UNIT_WARRIOR);
		ft_create_unit(UNIT_WARRIOR);
	}
}
