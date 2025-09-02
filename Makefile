.ONESHELL:
SHELL = /bin/bash
.PHONY: help clean environment kernel teardown

YML = environmental-remote-sensing.yml
PREFIX = $(CURDIR)/.conda_envs
CONDA_ENV_DIR := $(PREFIX)/environmental-remote-sensing
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; \
	conda activate ; conda activate $(CONDA_ENV_DIR)
KERNEL_DIR = $(shell jupyter --data-dir)/kernels/environmental-remote-sensing

help:
	@echo "Makefile for setting up environment, kernel, and pulling notebooks"
	@echo ""
	@echo "Usage:"
	@echo "  make environment  - Create Conda environments"
	@echo "  make kernel       - Create Conda environments and Jupyter kernels"
	@echo "  "
	@echo "  make teardown     - Remove Conda environments and Jupyter kernels"
	@echo "  make clean        - Removes ipynb_checkpoints"
	@echo "  make help         - Display this help message"

clean:
	rm --force --recursive .ipynb_checkpoints/

teardown:
	$(CONDA_ACTIVATE)
	jupyter kernelspec uninstall -y environmental-remote-sensing
	conda deactivate
	conda remove --prefix $(CONDA_ENV_DIR) --all -y
	rm -r $(PREFIX)

$(CONDA_ENV_DIR): $(YML)
	conda create --clone base --prefix $@
	conda env update --file $^ -p $@

environment: $(CONDA_ENV_DIR)
	@echo -e "conda environments are ready."

$(KERNEL_DIR): $(CONDA_ENV_DIR)
	$(CONDA_ACTIVATE)
	python -m ipykernel install --user --name environmental-remote-sensing --display-name environmental-remote-sensing
	conda deactivate

kernel: $(KERNEL_DIR)
	@echo -e "conda jupyter kernel is ready."
