MAIN = src/__main__.py
MAP ?= maps/easy/01_linear_path.txt

# ON 42 PC
STORAGE_PATH = /home/eberling/goinfre
# Github Workspaces
# STORAGE_PATH = /workspaces/42_HB/fly_in
# On MAC
# STORAGE_PATH = /Users/eloi/Documents/42/projects/fly_in

VENV_PATH = $(STORAGE_PATH)/.venv
# UV_CACHE_DIR is a default variable for UV package
export UV_CACHE_DIR = $(STORAGE_PATH)/.cache/uv
export UV_PROJECT_ENVIRONMENT = $(VENV_PATH)
export UV_LINK_MODE = copy
UV = uv

.PHONY: all install run clean help lint debug fclean

all: install

debug: install
	@echo "Running debug mode (pdb)..."
	@$(UV) run python -m pdb -m src

help:
	@echo "\
	\n\
	=========== HELP ===========\n\
	- make install    Install all requirements\n\
	- make run        Install and run the programm with default parameters\n\
	- make lint       Check code files for mypy and flake8 conventions\n\
	- make clean      Clean the installation files\n\
	\n\
	Parameters : MAP=<path to a specific map>
	\n\
	"

install:
	@echo "Syncing environment with uv..."
	@pip install uv
	@$(UV) sync
	@echo "Done."

run: install
	@echo "Installing dependencies..."
	@$(UV) sync
	@echo "Environment ready."
	@$(UV) run python -m src $(MAP)

dev: run

clean:
	@echo "Cleaning temporary files and caches..."
	@rm -rf .mypy_cache
	@rm -rf .pytest_cache
	@find . -type d -name "__pycache__" -exec rm -rf {} +
	@find . -type f -name "*.pyc" -delete
	@echo "Cleanup complete!"

fclean: clean
	@echo "Deep cleaning virtual environment and uv cache..."
	@rm -rf $(VENV_PATH)
	@rm -rf $(STORAGE_PATH)/.cache/uv
	@echo "Deep cleanup complete!"

lint: install
	@echo "Running flake8..."
	@$(UV) run flake8 src
	@echo "Running mypy..."
	@$(UV) run mypy src --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict: lint
	@$(UV) run mypy src --strict

test:
	echo "setup the tests"