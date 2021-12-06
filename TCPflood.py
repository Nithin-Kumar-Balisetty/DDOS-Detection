import pandas as pd
import numpy as np

def TCPfloodfun(table_name):
    main_table = pd.read_csv(table_name)
    src_IP = main_table['Source'].unique().tolist()
    src_IP.remove("192.168.2.3")
    iterator = np.array(src_IP)
    if main_table.loc[main_table['Info'].str.contains("\[SYN\]")].shape[0] < main_table.loc[main_table['Info'].str.contains("\[SYN, ACK\]")].shape[0]:
        print("TCP Flooding")
        for key in iterator:
            tb = main_table[main_table[['Source', 'Destination']].apply(tuple, axis=1).isin([("192.168.2.3", key), (key, "192.168.2.3")])]
            # print(tb.loc[tb['Info'].str.contains('\[SYN, ACK\]')])
            if tb.loc[tb['Info'].str.contains("\[SYN\]")].shape[0] < tb.loc[tb['Info'].str.contains("\[SYN, ACK\]")].shape[0]:
                print(key + " is trying to TCP flood the server with [SYN] of "+str(tb.loc[tb['Info'].str.contains("\[SYN\]")].shape[0])+" and [SYN, ACK] of "+str(tb.loc[tb['Info'].str.contains("\[SYN, ACK\]")].shape[0]))

TCPfloodfun("./TCPFlood.csv")
