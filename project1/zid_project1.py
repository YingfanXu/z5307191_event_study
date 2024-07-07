""" zid_project1.py

"""
import os
import json
import pandas as pd

# ----------------------------------------------------------------------------
# Location of files and folders
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' strings with the appropriate
#   expressions.
# IMPORTANT:
#   - Use the appropriate method from the `os` module to combine paths
#   - Do **NOT** include full paths like "C:\\User...". You **MUST* combine
#     paths using methods from the `os` module
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
ROOTDIR = os.path.join(os.getcwd(), 'data')
DATDIR = ROOTDIR  # Data files are in the 'data' directory
TICPATH = 'TICKERS.txt'

# ----------------------------------------------------------------------------
# Variables describing the contents of ".dat" files
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' string with the appropriate
#     expression.
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
# NOTE: `COLUMNS` must be a list, where each element is a column name in the
# order they appear in the ".dat" files
COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']

# NOTE: COLWIDTHS must be a dictionary with {<col> : <width>}, where
# - Each key (<col>) is a column name in the `COLUMNS` list
# - Each value (<width>) is an **integer** with the width of the column, as
#   defined in your README.txt file
#
COLWIDTHS = {
    'Volume': 14,
    'Date': 11,
    'Adj Close': 19,
    'Close': 10,
    'Open': 6,
    'High': 20
}


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def get_tics(pth):
    """ Reads a file containing tickers and their corresponding exchanges.
    Each non-empty line of the file is guaranteed to have the following format:

    "XXXX"="YYYY"

    where:
        - XXXX represents an exchange.
        - YYYY represents a ticker.

    This function should return a dictionary, where each key is a properly formatted
    ticker, and each value the properly formatted exchange corresponding to the ticker.

    Parameters
    ----------
    pth : str
        Full path to the location of the TICKERS.txt file.

    Returns
    -------
    dict
        A dictionary with format {<tic> : <exchange>} where
            - Each key (<tic>) is a ticker found in the file specified by pth (as a string).
            - Each value (<exchange>) is a string containing the exchange for this ticker.

    Notes
    -----
    The keys and values of the dictionary returned must conform with the following rules:
        - All characters are in lower case
        - Only contain alphabetical characters, i.e. does not contain characters such as ", = etc.
        - No spaces
        - No empty tickers or exchanges

    """
    with open(pth, 'r') as file:
        lines = file.readlines()
    tics = {}
    for line in lines:
        exchange, ticker = line.strip().split('=')
        tics[ticker.replace('"', '').strip().lower()] = exchange.replace('"', '').strip().lower()
    return tics


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def read_dat(tic):
    """
    Read a stock price data file for a given ticker and return its contents as a list of lines.
    """
    pth = ROOTDIR

    with open(pth, 'r') as file:
        lines = file.readlines()
    return lines


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def line_to_dict(line):
    """
    Convert a line from the .dat file into a dictionary based on COLUMNS and COLWIDTHS.
    """
    data = {}
    start = 0
    for col in COLUMNS:
        width = COLWIDTHS[col]
        data[col] = line[start:start + width].strip()
        start += width
    return data


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_tickers(tic_exchange_dic, tickers_lst=None):
    """
    Verify that the column names in cols_lst are present in COLUMNS.
    Raise an Exception if any column name is not found.
    """
    for col in cols_lst:
        if col not in COLUMNS:
            raise Exception(f"Column {col} not found in columns list.")


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_cols(col_lst=None):
    """
    Verify that the column names in cols_lst are present in COLUMNS.
    Raise an Exception if any column name is not found.
    """
    for col in cols_lst:
        if col not in COLUMNS:
            raise Exception(f"Column {col} not found in columns list.")


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_data_dict(tic_exchange_dic, tickers_lst=None, col_lst=None):
    """
    Transform the data found in the .dat files into a single dictionary.
    """
    data_dict = {}
    for tic in tickers_lst:
        exchange = tic_exchange_dic[tic]
        file_path = os.path.join(DATDIR, f'{tic}_prc.dat')
        lines = read_dat(file_path)
        tic_data = []
        for line in lines:
            line_data = line_to_dict(line)
            filtered_data = {col: line_data[col] for col in col_lst}
            tic_data.append(filtered_data)
        data_dict[tic] = {'exchange': exchange, 'data': tic_data}
    return data_dict


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_json(data_dict, pth):
    """
        Save the given dictionary into a JSON file.
        """
    with open(output_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)

    # ----------------------------------------------------------------------------
    #    Please put your answers for the last question here:
    # ----------------------------------------------------------------------------
    """
    '''
1. Explanation for Configuring Paths (Step 1):
Configuring the paths using the `os` module ensures that the code is portable and can run on any operating system without modification.
By combining paths using methods from the `os` module, we avoid hardcoding absolute paths, which might differ across different environments (such as Windows vs. macOS vs. Linux).
This approach makes the code more robust and adaptable to different directory structures and enhances collaboration by preventing path-related errors when sharing the code with others.


2. Evaluation of Hypotheses:
Hypothesis 1: Journalists' articles are based on investors' evaluations of those firms.
Hypothesis 2: Journalists' articles contain valuable information beyond firm fundamentals.

When evaluating the content of journalists' articles, especially when articles contain more negative words, we observe that stock returns tend to decrease in the short run without a reversal in the long run.
This behavior suggests that the articles likely contain valuable information beyond what is already reflected in the firm's fundamentals.
If the articles were merely reflecting investors' evaluations, we would expect the stock returns to adjust quickly and potentially reverse if the initial reaction was an overreaction.
However, the lack of reversal indicates that the negative sentiment in the articles provides new information that the market considers important, leading to a sustained impact on stock prices.
Thus, Hypothesis 2 is more likely to be true: Journalists' articles contain valuable information beyond firm fundamentals.


3. Short-Run Predictability for Trading Volume:
Given the chosen hypothesis that journalists' articles contain valuable information beyond firm fundamentals, we can infer that the trading volume in the short run is likely to be predictable based on the sentiment expressed in these articles.
Negative sentiment articles would likely lead to an increase in trading volume as investors react to the new information.
This increase in volume can be attributed to both the selling pressure from those reacting to the negative news and the buying interest from investors who might view the price drop as a buying opportunity.
Therefore, short-run trading volume is positively correlated with the sentiment of the articles, making it predictable based on the content of the journalists' reports.
'''
# ----------------------------------------------------------------------------

    """


# ----------------------------------------------------------------------------
#   Test functions:
#   The purpose of these functions is to help you test the functions above as
#   you write them.
#   IMPORTANT:
#   - These functions are optional, you do not have to use them
#   - These functions do not count as part of your assessment (they will not
#     be marked)
#   - You can modify these functions as you wish, or delete them altogether.
# ----------------------------------------------------------------------------
def _test_get_tics():
    """ Test function for the `get_tics` function. Will print the tickers as
    returned by the `get_tics` function.
    """
    pth = TICPATH
    tics = get_tics(pth)
    print(tics)


def _test_read_dat():
    """ Test function for the `read_dat` function. Will read the lines of the
    first ticker in `TICPATH` and print the first line in the list.
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    tic = tics[0]
    lines = read_dat(tic)
    # Print the first line in the file
    print(f'The first line in the dat file for {tic} is:')
    print(lines[0])


def _test_line_to_dict():
    """ Test function for the `read_dat` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Read the lines of the ".dat" file for the first ticker
    - Convert the first line of this file to a dictionary
    - Print this dictionary
    """
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    lines = read_dat(tics[0])
    dic = line_to_dict(lines[0])
    print(dic)


def _test_create_data_dict():
    """ Test function for the `create_data_dict` function. This function will perform
    the following operations:
    - Get the tickers using `get_tics`
    - Call `create_data_dict` using
        - tickers_lst =  ['aapl', 'baba']
        - col_lst = ['Date', 'Close']
    - Print out the dictionary returned, but only the first 3 items of the data list for each ticker for brevity

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)

    for tic in tickers_lst:
        data_dict[tic]['data'] = data_dict[tic]['data'][:3]

    print(data_dict)


def _test_create_json(json_pth):
    """ Test function for the `create_json_ function.
    This function will save the dictionary returned by `create_data_dict` to the path specified.

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)
    create_json(data_dict, json_pth)
    print(f'Data saved to {json_pth}')


# ----------------------------------------------------------------------------
#  Uncomment the statements below to call the test and/or main functions.
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    # Test functions
    # _test_get_tics()
    # _test_read_dat()
    # _test_line_to_dict()
    # _test_create_data_dict()
    # _test_create_json(os.path.join(DATDIR, 'data.json'))  # Save the file to data/data.json
    pass
