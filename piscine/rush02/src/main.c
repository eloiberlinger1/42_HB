/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: nweber <nweber@student.42Heilbronn.de>     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/05/18 10:44:16 by dgeiss            #+#    #+#             */
/*   Updated: 2025/05/18 19:29:44 by nweber           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/my_core_bot.h"

void	ft_init_func(void *data);
void	ft_user_loop(void *data);

int	main(int argc, char **argv)
{
	int	won;
	int	ticks;

	ft_init_con("atiwari", &argc, argv);
	ticks = 0;
	won = ft_loop(&ft_init_func, &ft_user_loop, NULL, &ticks);
	ft_close_con();
	if (won)
		return (0);
	return (1);
}

void	ft_init_func(void *data)
{
	(void)data;
	ft_create_unit(UNIT_WORKER);
	ft_create_unit(UNIT_WORKER);
	ft_create_unit(UNIT_WORKER);
	ft_create_unit(UNIT_WORKER);
	ft_print_unit_config(ft_get_unit_config(UNIT_WARRIOR));
	ft_print_unit_config(ft_get_unit_config(UNIT_WORKER));
	printf("init CORE Bot\n");
}

void	ft_user_loop(void *data)
{
	int		*ticker;
	int		i;
	t_obj	**units;

	units = ft_get_my_units();
	ticker = (int *)data;
	i = -1;
	*ticker += 1;
	spawn(*ticker);
	while (units[++i])
	{
		if (units[i]->s_unit.type_id == UNIT_WARRIOR)
			warrior_logic(*ticker, units[i],
				ft_get_nearest_opponent_unit(units[i]),
				ft_get_nearest_resource(units[i]));
		if (units[i]->s_unit.type_id == UNIT_WORKER)
			worker_logic(units[i],
				ft_get_nearest_resource(units[i]),
				ft_get_nearest_opponent_unit(units[i]),
				units);
	}
	free(units);
}
