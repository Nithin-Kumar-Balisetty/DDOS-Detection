import pandas as pd
import numpy as np

def UDPfloodfun(table_name):
    main_table = pd.read_csv(table_name)
    iterator = main_table['Source'].unique()
    uli = main_table["Length"].unique().tolist()
    if (main_table.shape[0] == main_table[main_table['Protocol'] == 'UDP'].shape[0]) or (main_table[main_table['Protocol'] == 'UDP'].shape[0] == len(uli)):
        print("UDP Flooding")
        for key in iterator:
            print(key + " is trying to UDP flood the server")


UDPfloodfun("./UDPFlood.csv")
