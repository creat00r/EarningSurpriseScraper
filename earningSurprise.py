#from multiprocessing import Pool, TimeoutError
import multiprocessing as mp
import time
import os
from bs4 import BeautifulSoup
#import requests
import time
#import pandas as pd
import re
from scraper import ES
import csv

if __name__ == '__main__':
    # start 8 worker processes
    with mp.Pool(processes=8) as pool:

        lines = []
        with open("nasdaqlisted.txt") as file_in:

            for line in file_in:
                var = line.split("|",1)[0]
                if (len(var) < 5):
                    lines.append(var)
                    print(var)


        with open('racks.csv', 'a') as csvfile:
            fieldnames = ['Symbol', 'q1', 'q2', 'q3', 'q4', 'av', 'var', 'si']#last 4 quarter surprises, their average, variance, and the sustainability index
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            results = {}
            for symbol in lines:
                csvfile.flush()
                try:

                        print("Processing for symbol ", symbol)
                        result = pool.apply_async(ES, [symbol])
                        output = result.get()#timeout=12
                        #print(output)
                        quarters = output[0]
                        q1 = quarters[0]
                        q2 = quarters[1]
                        q3 = quarters[2]
                        q4 = quarters[3]
                        av = output[1]
                        var = output[2]
                        si = output[3]
                        #print (si)
                        #csvfile.open()
                        writer.writerow({'Symbol': symbol, 'q1': q1, 'q2': q2,'q3': q3,'q4': q4,'av': av,'var': var,'si': si})

                except:
                    print("No data for: " + symbol)
                    writer.writerow({'Symbol': symbol, 'q1': '?', 'q2': '?','q3': '?','q4': '?','av': '?','var': '?','si': '?'})

            #csvfile.close()#automatic

    print("Done!")
