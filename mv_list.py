mv_list = [["トップガン","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]

import csv
with open("mv_list.csv", "w", encoding="utf-8", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(mv_list[0])
    w.writerow(mv_list[1])
    w.writerow(mv_list[2])
