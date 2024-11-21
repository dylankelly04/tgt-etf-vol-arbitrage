from getInfo import getOverallInfo, getSpecificInfo

tickers = ['SMH','NVDA', 'TSM', 'AVGO', 'TXN', 'QCOM',
    'AMAT', 'ASML', 'MU', 'ADI', 'LRCX', 'INTC', 'KLAC',
    'SNPS', 'CDNS', 'MRVL', 'NXPI', 'MCHP', 'MPWR', 'ON',
    'STM', 'TER', 'SWKS', 'OLED', 'QRVO']

limit = 10


for ticker in tickers:
    print(ticker)
    print(getOverallInfo(ticker, limit))

print(getSpecificInfo('SWKS', 10, 60, '2024-11-22'))