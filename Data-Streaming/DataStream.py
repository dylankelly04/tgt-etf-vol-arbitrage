from getInfo import getInfo

tickers = ['SMH','NVDA', 'TSM', 'AVGO', 'TXN', 'QCOM',
    'AMAT', 'ASML', 'MU', 'ADI', 'LRCX', 'INTC', 'KLAC',
    'SNPS', 'CDNS', 'MRVL', 'NXPI', 'MCHP', 'MPWR', 'ON',
    'STM', 'TER', 'SWKS', 'OLED', 'QRVO']

limit = 10

#issue with AMD
#issue with SMH

print(getInfo('SMH', 10))

#for ticker in tickers:
#    print(ticker)
#    print(getInfo(ticker, limit))

print(getInfo('SWKS', 10, 60, '2024-11-22'))