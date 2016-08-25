import pandas as pd


class model:

    def __init__(self):
        self.final_table = pd.read_csv('base_file2.csv', sep=";")
    def get_annualized_rates(self, offer):
            self.final_table['short'+'_'+offer] = self.final_table['ask'] * ((1 + self.final_table['quote_bid'] - self.final_table[offer] / 2) / 360) / (
                (1 + self.final_table['base_ask'] + self.final_table[offer] / 2) / 360)
            self.final_table['long'+'_'+offer] = self.final_table['bid'] * ((1 + self.final_table['quote_bid'] - self.final_table[offer] / 2) / 360) / (
                (1 + self.final_table['base_ask'] + self.final_table[offer] / 2) / 360)
            return self.final_table
start = model()
print(start.get_annualized_rates('Offer3'))
