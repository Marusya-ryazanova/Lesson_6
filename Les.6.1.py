coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')
new_dict = {key: value for key, value in zip(coin, code)}
print(new_dict)