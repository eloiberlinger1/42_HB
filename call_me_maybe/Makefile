MAIN = src/main.py
PYTHON = python3
STORAGE_PATH = /goinfre/eberling
VENV_PATH = $(STORAGE_PATH)/.venv
# UV_CACHE_DIR is default variable for UV package
export UV_CACHE_DIR = $(STORAGE_PATH)/.cache/uv


.PHONY: all install run clean

all: install

install:
	@echo "Creating .venv in $(VENV_PATH)..."
	@uv venv $(VENV_PATH)
	@echo "Installing dependencies..."
	@$(VENV_PATH)/bin/uv pip install pydantic numpy
	@echo "Done."

run:
	@$(VENV_PATH)/bin/python -m src

clean:
	@echo "Tidying up..."
	@rm -rf $(VENV_PATH)
	@rm -rf $(STORAGE_PATH)/.cache/uv
