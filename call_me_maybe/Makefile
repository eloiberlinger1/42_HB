MAIN = src/__main__.py
STORAGE_PATH = /home/eberling/goinfre
STORAGE_PATH = /workspaces/42_HB/call_me_maybe
STORAGE_PATH = /Users/eloi/Documents/42/projects/call_me_maybe
VENV_PATH = $(STORAGE_PATH)/.venv
# UV_CACHE_DIR is a default variable for UV package
export UV_CACHE_DIR = $(STORAGE_PATH)/.cache/uv
export UV_PROJECT_ENVIRONMENT = $(VENV_PATH)
export UV_LINK_MODE = copy
UV = uv

.PHONY: all install run clean help lint

all: install

debug: install
	@echo "Running debug mode (pdb)..."
	@$(UV) run python -m pdb -m src $(ARGS)

help:
	@echo "\
	\n\
	=========== HELP ===========\n\
	- make install    Install all requirements\n\
	- make run        Install and run the programm with default parameters\n\
	- make lint       Check code files for mypy and flake8 conventions\n\
	- make clean      Clean the installation files\n\
	\n\
	In order to run the script with specific parameters:\n\
	uv run python -m src [--functions_definition <function_definition_file>] [--input <input_file>] [--output <output_file>]\
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
	@$(UV) run python -m src $(ARGS)

clean:
	@echo "Tidying up..."
	@rm -rf $(VENV_PATH)
	@rm -rf $(STORAGE_PATH)/.cache/uv

lint:
	@echo "Running flake8"
	@flake8 src/
	@echo "Running mypy"
	@mypy src/

