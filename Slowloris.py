import pandas as pd
import numpy as np

def SlowLoris(table_name, limit):
    main_table = pd.read_csv(table_name)
    src_IP = main_table['Source'].unique().tolist()
    src_IP.remove("192.168.2.5")
    iterator = np.array(src_IP)

    for key in iterator:
        tb = main_table[main_table[['Source', 'Destination']].apply(tuple, axis=1).isin([(key, "192.168.2.5"), ("192.168.2.5", key)])]
        ft_keys = tb["Src Port"].unique().tolist()
        ft_keys.remove(80.0)
        if len(ft_keys) == 1:
            continue
        for ft_key in ft_keys:
            main_tb = tb[tb[['Src Port', 'Dst Port']].apply(tuple, axis=1).isin([(ft_key, 80.0), (80.0, ft_key)])]
            if main_tb.loc[main_tb['Info'].str.contains("\[PSH, ACK\]")].shape[0] > 2 and main_tb.loc[main_tb['Info'].str.contains("\[FIN, ACK\]")]['Time'].iloc[0] > limit:
                print(key + " with port: "+str(ft_key)+" is sending partial requests of "+str(main_tb.loc[main_tb['Info'].str.contains("\[PSH, ACK\]")].shape[0])+" and exceeding threshold of "+str(limit))
                print('Port Connection Terminated at '+str(main_tb.loc[main_tb['Info'].str.contains("\[FIN, ACK\]")]['Time'].iloc[0]))

SlowLoris("./SlowlorisCap.csv", 20)
