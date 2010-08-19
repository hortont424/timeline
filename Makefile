.PHONY: all clean

all:
	./src/main.py

clean:
	find . -name *.pyc | xargs rm -f