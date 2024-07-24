import os

import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """Download stock prices from Yahoo Finance for a given year into 
    CSV file. This file will be located under the 'cfg.DATADIR' folder and 
    will be called "gan_prc_YYYY.csv", where 'YYYY' corresponds to the year 
    'year'
    
    Parameters
    -----------
    year : int
        An integer with a four-digit year
    """
    df = yf.download(tic, start=start, end=end, ignore_tz=True)
    df.to_csv(pth)

if __name__ == "__main__":
    tic = 'QAN.AX'
    datadir =C:\Users\xyf20\PycharmProjects\pythonProject\Fins5546 24T2\data
    pth = f'{datadir}/qan_stk_prc.csv'
    yf_prc_to_csv(tic, pth)
    import os
    import toolkit_config as cfg

    tic = "QAN.AX"
    pth = os.path.join(cfg.DATADIR, 'qan_stk_prc.csv')
    yf_prc_to_csv(tic, pth)