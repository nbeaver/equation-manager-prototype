all: validate_json test_query
.PHONY : validate_json test_query

validate_json : equation-database.json Makefile
	json_verify < equation-database.json
	#jparse equation-database.json > /dev/null

test_query : equation-database.txt equation-search.py
	equation-search.py "quadratic formula" > /dev/null
