NAME = push_swap
CC = cc
CFLAGS = -Wextra -Wall -Werror

C_FILES = push_swap.c \
utils/ft_lstutils.c \
utils/check_sort.c \
utils/op_swap.c \
utils/parse_input.c \
utils/op_push.c utils/op_rev_rotate.c \
utils/op_rotate.c utils/sorting_small.c utils/sorting_main.c

O_FILES = $(C_FILES:.c=.o)

.PHONY: printf_deps

all: $(NAME)

# --- Dependencies (ft_printf & libft) ---
PRINTF_D = ft_printf/
PRINTF_A = libftprintf.a
PRINTF_PATH = $(PRINTF_D)$(PRINTF_A)
printf_deps:
	@echo "--- Compiling ft_printf and libft dependencies ---"
	$(MAKE) -C $(PRINTF_D) all

$(NAME): $(O_FILES) printf_deps
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

.PHONY: all clean fclean re printf_deps
