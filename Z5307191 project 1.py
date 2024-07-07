import os
import json
import pandas as pd

# Constants
ROOTDIR = os.path.join(os.getcwd(), 'data')
DATDIR = ROOTDIR  # Data files are in the 'data' directory
TICPATH = 'TICKERS.txt'

# Column details from README.txt
COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']
COLWIDTHS = {
    'Volume': 14,
    'Date': 11,
    'Adj Close': 19,
    'Close': 10,
    'Open': 6,
    'High': 20
}


def get_tics(pth):
    """
    Read a file with tickers and return a list with formatted tickers.
    """
    with open(pth, 'r') as file:
        lines = file.readlines()
    tics = {}
    for line in lines:
        exchange, ticker = line.strip().split('=')
        tics[ticker.replace('"', '').strip().lower()] = exchange.replace('"', '').strip().lower()
    return tics


def read_dat(pth):
    """
    Read a stock price data file for a given ticker and return its contents as a list of lines.
    """
    with open(pth, 'r') as file:
        lines = file.readlines()
    return lines


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


def verify_tickers(tics_lst, tics_dic):
    """
    Verify that the tickers in tics_lst are present in tics_dic.
    Raise an Exception if any ticker is not found.
    """
    for tic in tics_lst:
        if tic not in tics_dic:
            raise Exception(f"Ticker {tic} not found in ticker dictionary.")


def verify_cols(cols_lst):
    """
    Verify that the column names in cols_lst are present in COLUMNS.
    Raise an Exception if any column name is not found.
    """
    for col in cols_lst:
        if col not in COLUMNS:
            raise Exception(f"Column {col} not found in columns list.")


def create_data_dict(tic_exchange_dic, tickers_lst, col_lst):
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


def create_json(data_dict, output_path):
    """
    Save the given dictionary into a JSON file.
    """
    with open(output_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)


# Execute the implemented functions to test
tics_dic = get_tics(TICPATH)
print(f"Tickers Dictionary: {tics_dic}")

# Verify all tickers from the dictionary
verify_tickers(list(tics_dic.keys()), tics_dic)
verify_cols(COLUMNS)

# Create data dictionary for all tickers in the TICKERS.txt file
data_dict = create_data_dict(tics_dic, list(tics_dic.keys()), COLUMNS)

# Define the output path for the JSON file
output_path = os.path.join(ROOTDIR, 'output.json')

# Create JSON file from the data dictionary
create_json(data_dict, output_path)

print(f"Data saved to {output_path}")

"""# ----------------------------------------------------------------------------
#    Answers for the last question:
# ----------------------------------------------------------------------------

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
