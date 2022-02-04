# Ramu Vallapurapu
# Mapper

import sys 


for line in sys.stdin:
  datalist = line.strip().split(",")

  if (len(datalist) == 5) : 
    Series_Title,Released_Year,IMDB_Rating,Meta_score,No_of_Votes = datalist

    print(Series_Title,"\t",IMDB_Rating)