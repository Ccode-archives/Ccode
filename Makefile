main:
	@echo "Please run 'make all'"


all: install_npm_deps


install_npm_deps:
	@echo "Installing npm deps..."
	@npm install prompt-sync@4.2.0
	@echo "Done\n"
	
