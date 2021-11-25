import MetaTrader5 as mt5
import pandas as pd


TIMEFRAMES = ['M1', 'M5', 'M15', 'M30', 'H1', 'H4', 'D1', 'W1', 'MN1']
TIMEFRAME_DICT = {
    'M1': mt5.TIMEFRAME_M1,
    'M5': mt5.TIMEFRAME_M5,
    'M15': mt5.TIMEFRAME_M15,
    'M30': mt5.TIMEFRAME_M30,
    'H1': mt5.TIMEFRAME_H1,
    'H4': mt5.TIMEFRAME_H4,
    'D1': mt5.TIMEFRAME_D1,
    'W1': mt5.TIMEFRAME_W1,
    'MN1': mt5.TIMEFRAME_MN1,
}


def get_symbol_names():
    # connect to MetaTrader5 platform
    mt5.initialize()

    # get symbols
    symbols = mt5.symbols_get()
    symbols_df = pd.DataFrame(symbols, columns=symbols[0]._asdict().keys())

    symbol_names = symbols_df['name'].tolist()
    return symbol_names