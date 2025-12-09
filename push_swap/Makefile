NAME = push_swap
CC = cc
CFLAGS = -Wextra -Wall -Werror -g
C_FILES = push_swap.c utils/check_sort.c utils/op_swap.c utils/op_push.c utils/op_rotate.c utils/sorting.c utils/operations.c

O_FILES = $(C_FILES:.c=.o)

all: $(NAME)

# --- Dependencies (ft_printf & libft) ---
PRINTF_D = ft_printf/
PRINTF_A = libftprintf.a
PRINTF_PATH = $(PRINTF_D)$(PRINTF_A)
$(PRINTF_PATH):
	@echo "--- Compiling ft_printf and libft dependencies ---"
	$(MAKE) -C $(PRINTF_D) all

$(NAME): $(O_FILES) $(PRINTF_PATH)
	@echo "--------- LINKING -------"
	$(CC) $(CFLAGS) $(O_FILES) -L$(PRINTF_D) -lftprintf -o $(NAME)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(O_FILES)
	$(MAKE) -C $(PRINTF_D) clean

fclean: clean
	rm -f $(NAME)
	$(MAKE) -C $(PRINTF_D) fclean

re: fclean all

.PHONY: all clean fclean re
