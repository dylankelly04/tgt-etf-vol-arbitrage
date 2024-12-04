#generates the data for volatility surfaces

from getInfo import getOverallInfo, getSpecificInfo, get_info_range
from datetime import datetime, timedelta
import numpy as np

component_tickers = ['NVDA', 'TSM', 'AVGO', 'TXN', 'QCOM',
    'AMAT', 'ASML', 'MU', 'ADI', 'LRCX', 'INTC', 'KLAC',
    'SNPS', 'CDNS', 'MRVL', 'NXPI', 'MCHP', 'MPWR', 'ON',
    'STM', 'TER', 'SWKS', 'OLED', 'QRVO']

weights = {}
weights['NVDA'] = 0.224
weights['TSM'] = 0.1346
weights['AVGO'] = 0.0768
weights['AMD'] = 0.0478
weights['TXN'] = 0.0429
weights['QCOM'] = 0.0424
weights['AMAT'] = 0.0415
weights['ASML'] = 0.0415
weights['MU'] = 0.0414
weights['ADI'] = 0.0399
weights['LRCX'] = 0.037
weights['INTC'] = 0.036
weights['KLAC'] = 0.0333
weights['SNPS'] = 0.0287
weights['CDNS'] = 0.025
weights['MRVL'] = 0.0226
weights['NXPI'] = 0.0191
weights['MCHP'] = 0.0146
weights['MPWR'] = 0.0145
weights['ON'] = 0.009
weights['STM'] = 0.0085
weights['TER'] = 0.0059
weights['SWKS'] = 0.0054
weights['OLED'] = 0.0036
weights['QRVO'] = 0.0033

def days_from_today(date_string):
    
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")
    today = datetime.today()
    delta = date_obj - today
    return delta.days + 1 # idk why we have to add 1 but we do

def n_days_out(num_out):
    today = datetime.today()
    target = today + timedelta(days=num_out)
    return target.strftime("%Y-%m-%d")

# generate data for SMH surface:

def generate_SMH_data():

    date_list = []
    strike_list = []
    vol_list = []

    data = getOverallInfo('SMH', 250)

    for i in data:
        strike_list.append(i[0])
        date_list.append(days_from_today(i[1]))
        vol_list.append(i[2])
    
    
    return date_list, strike_list, vol_list

# doesnt work
def generate_ticker_data(ticker, exp_min, exp_max, strike_min, strike_max):

    date_list = []
    strike_list = []
    vol_list = []

    # FIXME
    data = get_info_range(ticker, 250, exp_min, exp_max, strike_min, strike_max)

    for i in data:
        strike_list.append(i[0])
        date_list.append(days_from_today(i[1]))
        vol_list.append(i[2])
    
    
    return date_list, strike_list, vol_list

def generate_component_data1():

    smh_dates, smh_strikes, smh_vols = generate_SMH_data()

    component_vols = []

    for i in range(0, len(smh_dates)):

        iv_total = 0

        for ticker in component_tickers:

            print(ticker)

            data = getSpecificInfo(ticker, 1, smh_strikes[i], n_days_out(smh_dates[i]))
            #print(data)

            if len(data) == 0:
                #print('failed to get IV, using SMH iv')
                iv_total += weights[ticker] * smh_vols[i]
            else:
                iv_total += weights[ticker] * data[0][2]

        component_vols.append(iv_total)

        print(iv_total)


    return smh_dates, smh_strikes, smh_vols, component_vols

def generate_all_data():

    smh_dates, smh_strikes, smh_vols = generate_SMH_data()

    component_vols = []

    for i in range(0, len(smh_dates)):

        iv_total = 0

        for ticker in component_tickers:
            print(ticker)
            data = getSpecificInfo(ticker, 1, smh_strikes[i], n_days_out(smh_dates[i]))
            #print(data)

            if len(data) == 0:
                #print('failed to get IV, using SMH iv')
                iv_total += weights[ticker] * smh_vols[i]
            else:
                iv_total += weights[ticker] * data[0][2]

        component_vols.append(iv_total)

        print(i)


    return smh_dates, smh_strikes, smh_vols, component_vols


if __name__ == '__main__':
    #times, strikes, ivs = generate_SMH_data()

    print(generate_component_data1()[3])



    #print(get_info_range('NVDA', 250, n_days_out(min(times)), n_days_out(max(times)), min(strikes), max(strikes)))

    print("done")
