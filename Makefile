all: validate_json validate_yaml test_query
.PHONY : validate_json validate_yaml test_query

validate_json : equation-database.json Makefile
	json_verify < equation-database.json
	#jparse equation-database.json > /dev/null

validate_yaml : equation-database.yml validate-yaml.py Makefile
	python validate-yaml.py equation-database.yml

test_query : equation-database.txt equation-search.py
	equation-search.py "quadratic formula" > /dev/null
