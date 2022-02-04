# map-reduce-ramuvallapurapu
This is practice for map and reduce

## Data Description:
- This Data Set consists details of all the ***Movies and IMDB Ratings, available in IMDB website***.
- The Dataset is a free resource from ***[Kaggle](https://www.kaggle.com)*** and can be viewed ***[here](imdb_top_1000.csv)***.

## Study:
- For this Dataset, I want to find out the ratings of  Movies released each year.

## Execution:
- A ***Mapper Script*** extracts the movie name from each row in the dataset, which is used as a ***Key*** and a ***Value*** of Rating is assigned to each Key. This is given as input to the ***Sorter*** which sorts all the years in descending order. Based on the output of the Sorter, which is passed as input to the ***Reducer Script***, combines all the ratings.

## Powershell Command:
- ***cat netflix_titles.csv | python 01mapper.py | python 02sorter.py | python 03reducer.py > output.txt***

## Summary:
- By examining the final output, I can Conclude that movies above 7 and below 8 rating are in high number.


![image](https://user-images.githubusercontent.com/77760915/152479608-3157783a-aa90-41f6-b11e-c9a7889f1aa6.png)

