.PHONY: data
# Create the penguin chart
penguin:
	mkdir -p figs
	python -B src/penguins.py
data:
	mkdir -p data
	cd data; curl -O "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"

clean:
	rm -rf data
	rm -rf figs
