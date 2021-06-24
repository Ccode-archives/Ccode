main:
	@echo "Please run 'make all'"


all: install_npm_deps test


install_npm_deps: get_ready
	@echo "Installing npm deps..."
	./bootstrap

get_ready:
	@echo "Getting ready..."
	chmod +x bootstrap


test:
	@echo "Testing..."
	@echo "\n\n"
	@echo "running hello world..."
	@echo "\n\n\n\n"
	@python3 Ccode.py examples/hello_world.cc || python Ccode.py examples/hello_world.cc || echo "Error: no python interpreter found!"
	
