clean:
	jupyter-book clean book/ --all

build: clean
	jupyter-book build book
	
publish:
	ghp-import -n -p -f book/_build/html

open:
	open file:///Users/felix/Coding/CodingBook/book/_build/html/index.html 

build_open: build open

build_publish: build publish