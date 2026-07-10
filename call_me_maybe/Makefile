MAIN = src/__main__.py
STORAGE_PATH = /home/eberling/goinfre
# STORAGE_PATH = /Users/eloi/Documents/42/projects/call_me_maybe
VENV_PATH = $(STORAGE_PATH)/.venv
# UV_CACHE_DIR is a default variable for UV package
export UV_CACHE_DIR = $(STORAGE_PATH)/.cache/uv
export UV_PROJECT_ENVIRONMENT = $(VENV_PATH)
export UV_LINK_MODE = copy
UV = uv

.PHONY: all install dev run clean

all: install

install:
	@echo "Syncing environment with uv..."
	@$(UV) sync
	@echo "Done."

dev: install
	@echo "Installing development dependencies..."
	@$(UV) sync
	@echo "Dev environment ready."
	uv run python -m src

run: install
	@$(UV) run python -m src

clean:
	@echo "Tidying up..."
	@rm -rf $(VENV_PATH)
	@rm -rf $(STORAGE_PATH)/.cache/uv
