import ffn

prices = ffn.get('aapl,msft', start='2010-01-01')

ax = prices.rebase().plot()

returns = prices.to_returns().dropna()

stats = prices.calc_stats()
stats.display()

# end of file
