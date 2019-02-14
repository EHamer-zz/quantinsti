"""
momentum.py
===========================
    author: erichamer

    use the sixty day momentum to
"""
# import necessary Packages below:
import numpy as np

##### Do not change this function definition #####
def myTradingSystem(DATE, CLOSE, settings):
    ''' This system uses mean reversion techniques to allocate capital into the desired equities '''

    # This strategy evaluates two averages over time of the close over a long/short
    # scale and builds the ratio. For each day, "smaQuot" is an array of "nMarkets"
    # size.
    n_markets = np.shape(CLOSE)[1]
    momentum_period = settings['lookback']
    momentum = np.divide(CLOSE[(momentum_period - 1):], CLOSE[:np.shape(CLOSE)[0] - (momentum_period - 1)])
    threshold = np.ones(n_markets)

    long_pos = momentum > threshold
    short_pos = ~long_pos

    pos = np.zeros(n_markets)
    pos[long_pos[0]] = 1
    pos[short_pos[0]] = -1

    # For the position sizing, we supply a vector of weights defining our
    # exposure to the markets in settings['markets']. This vector should be
    # normalized.
    pos = pos/np.nansum(abs(pos))

    return pos, settings


##### Do not change this function definition #####
def mySettings():
    ''' Define your trading system settings here '''
    settings = {}

    # Futures Contracts
    settings['markets'] = ['CASH', 'F_AD', 'F_AE', 'F_AH', 'F_AX', 'F_BC', 'F_BG', 'F_BO', 'F_BP', 'F_C',  'F_CA',
                           'F_CC', 'F_CD', 'F_CF', 'F_CL', 'F_CT', 'F_DL', 'F_DM', 'F_DT', 'F_DX', 'F_DZ', 'F_EB',
                           'F_EC', 'F_ED', 'F_ES', 'F_F',  'F_FB', 'F_FC', 'F_FL', 'F_FM', 'F_FP', 'F_FV', 'F_FY',
                           'F_GC', 'F_GD', 'F_GS', 'F_GX', 'F_HG', 'F_HO', 'F_HP', 'F_JY', 'F_KC', 'F_LB', 'F_LC',
                           'F_LN', 'F_LQ', 'F_LR', 'F_LU', 'F_LX', 'F_MD', 'F_MP', 'F_ND', 'F_NG', 'F_NQ', 'F_NR',
                           'F_NY', 'F_O',  'F_OJ', 'F_PA', 'F_PL', 'F_PQ', 'F_RB', 'F_RF', 'F_RP', 'F_RR', 'F_RU',
                           'F_RY', 'F_S',  'F_SB', 'F_SF', 'F_SH', 'F_SI', 'F_SM', 'F_SS', 'F_SX', 'F_TR', 'F_TU',
                           'F_TY', 'F_UB', 'F_US', 'F_UZ', 'F_VF', 'F_VT', 'F_VW', 'F_VX',  'F_W', 'F_XX', 'F_YM',
                           'F_ZQ']

    settings['lookback'] = 504
    settings['budget'] = 10**6
    settings['slippage'] = 0.05

    return settings


# Evaluate trading system defined in current file.
if __name__ == '__main__':
    from quantiacsToolbox import quantiacsToolbox
    results = quantiacsToolbox.runts(__file__)
