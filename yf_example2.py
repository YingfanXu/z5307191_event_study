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
    tic : str
    Ticker

    pth : str
    Location of the output CSV file

    start: str, optional
    Download start date string (YYYY-MM-DD)
    If None (the default), start is set to '1900-01-01'

    end: str, optional
    Download end date string (YYYY-MM-DD)
    If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end, ignore_tz=True)
    df.to_csv(pth)


if __name__ == "__main__":
    tic = 'QAN.AX'
    datadir = r'C:\Users\xyf20\PycharmProjects\pythonProject\Fins5546 24T2\data'
    pth = fr'{datadir}/qan_stk_prc.csv'
    yf_prc_to_csv(tic, pth)
