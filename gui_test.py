import pandas as pd

def get_data(f,c):
    ticker_list = pd.read_csv(f)
    x = ticker_list[c].tolist()
    return x
def get_annualized_rates(side, offer):
    if side == 'bid':
        rates_table = get_data('markup_list.csv', 'ticker')
    else:
        rates_table = get_data('markup_list.csv', 'ticker')
    return rates_table
rates_r1 = get_annualized_rates('bid', 'basic')
print(rates_r1)
rates_r2 = get_annualized_rates('bid', 'standard')
print(rates_r2)