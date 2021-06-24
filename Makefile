main:
	@echo "Please run 'make all'"


all: install_npm_deps test


install_npm_deps:
	@echo "Installing npm deps..."
	@npm install prompt-sync@4.2.0
	@echo "Done\n"


test:
	@echo "Testing..."
	@echo "running hello world..."
	@echo "\n"
	@python3 Ccode.py examples/hello_world.cc || python Ccode.py examples/hello_world.cc || echo "Error: no python interpreter found!"
	
