
# hw-fcc

Process and plot FCC broadband data for one county subdivision (Millinocket).

## Exercise #0

* Download all the files needed for the calculation into in a local data directory
* .gitignore the data directory, but make sure you document original data sources so they're easily downloaded again
* Provide clear instructions for getting all the data and reproducing all results

## Exercise #1

* Compute the maximum `max_advertised_download_speed` for each block in Maine
* Use: cable, copper and fiber to premises
* Save this intermediate result to a file called `data/speeds.csv`

## Exercise #2

* Use the result of Exercise #1 to compute the average speed for Millinocket
* Mapping from block to county subdivision is available as txt files on census.gov
* [block maps](https://www.census.gov/geographies/reference-maps/2020/geo/2020-census-block-maps.html) -- census.gov
* Use these mappings to compute broadband speeds for county subdivisions

## Exercise #3

* Merge the census geographies and the FCC data by census block
* Compute maximum `max_advertised_download_speed` for each block in all of Maine
* Save the merged file to `data/speeds.json`

## Exercise #4

Read `data/speeds.json` and plot speeds for the entire state

## Exercise #5

Read `data/speeds.json`, compute average speed and plot the block-level speeds for Millinocket

## How to Construct
```
make data
```
Downloads the datasets. Datasets are found by fcc.gov and census.gov but pulled from Phillip Bogden's repo

```
make max
```
Make a dataset of the maximum download speed in each block
```
make millinocket
```
computes the average speed for millinocket
```
make picture
```
