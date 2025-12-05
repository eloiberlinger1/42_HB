NAME = push_swap
CC = cc
CFLAGS = -Wextra -Wall -Werror
DFLAGS = -g
C_FILES = push_swap.c utils/operations.c utils/sa_sb_ss.c

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
