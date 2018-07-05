import csv
with open("mv_list.csv" ,"r", encoding="utf-8") as f:
     r = csv.reader(f, delimiter=",")
     for row in r:
         print(",".join(row))
