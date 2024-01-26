all: folder

folder:
	python3 ./src/run.py

file:
	@read -p "Enter file name: " file_name; \
	python3 ./src/run.py ./data/$$file_name.csv

test:
	@read -p "Enter file name: " file_name; \
	pytest ./tests/test_$$file_name.py -s
