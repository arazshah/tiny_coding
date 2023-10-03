transations=[
{"product":"A","sales":100},
{"product":"B","sales":200},
{"product":"A","sales":150},
{"product":"C","sales":50},
{"product":"B","sales":300},
{"product":"C","sales":250},
]

from itertools import groupby
from operator import itemgetter

transations.sort(key=itemgetter("product"))
grouped_transaction=groupby(transations,key=itemgetter("product"))
result={}

for product,group in grouped_transaction:
    total_sales=sum(item["sales"]for item in group)
    result[product]=total_sales

print(result)