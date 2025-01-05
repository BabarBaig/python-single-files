import numpy as np
import pandas as pd
from scipy.stats import norm, jarque_bera

def annualized_return(rets_m: pd.Series) -> float:
    """
    Calculate annualized return from a Panda Series of monthly returns.
    Parameters:
    - rets_m: a Panda Series of monthly returns
    Returns:
    - float: Annualized return
    """
    # First, calculate the cumulative return
    cum_return = (1 + rets_m).prod()
    # Next, calculate the number of months
    n_months   = rets_m.shape[0]
    n_months_2 = len(rets_m)
    assert n_months == n_months_2
    # Finally, calculate the annualized return
    annualized_return = cum_return**(12/n_months) - 1
    return annualized_return

def annualized_volatility(rets_m: pd.Series) -> float:
    """
    Calculate annualized volatility from a Panda Series of monthly returns.
    Parameters:
    - rets_m: a Panda Series of monthly returns
    Returns:
    - float: Annualized volatility
    """
    # First, calculate the monthly volatility
    monthly_vol = rets_m.std()
    # Next, calculate the annualized volatility
    annualized_vol = monthly_vol * np.sqrt(12)
    return annualized_vol

def ffme_returns(filepath: str, series1: str, series2: str) -> pd.DataFrame:
    """
    Get Fama & French Market Equity-based returns.  Convert from percentage to
    decimal format.  Convert the index to a PeriodIndex.
    Load the FF dataset for the returns of series1 and series2.
    """
    me_m = pd.read_csv(filepath, header=0, index_col=0, na_values=-99.99,
                       parse_dates=True, date_format="%Y%m")
    # print(me_m.head())
    rets = me_m[[series1, series2]]
    # rets.columns = ['sm_cap', 'lg_cap']
    rets /= 100
    # In following choices we can either have a PeriodIndex yyyy-mm
    # Or we can have a DateTime index yyyy-mm-dd.  This works with plotting
    # functions, but incorrectly shows monthly returns as daily returns.
    # PeriodIndex  : 1110 entries, 1926-07 to 2018-12
    # rets.index = pd.to_datetime(rets.index, format="%Y%m").to_period('M')
    # DatetimeIndex: 1110 entries, 1926-07-01 to 2018-12-01
    # rets.index = pd.to_datetime(rets.index, format="%Y%m")
    # PeriodIndex  : 1110 entries, 1926-07 to 2018-12
    # rets.index = rets.index.to_period('M')
    # DatetimeIndex: 1110 entries, 1926-07-01 to 2018-12-01
    # rets.index = rets.index.to_period('M').to_timestamp()
    rets.index = rets.index.to_period('M')
    # print("rets.head(): ****************")
    # print(rets.head())
    # print("rets.info(): ****************")
    # print(rets.info())
    return rets

# ************************************************************
# Deviations from Normality
# ************************************************************

def hfi_returns(filepath: str) -> pd.DataFrame:
    """
    Load and format the EDHEC Hedge Fund Index Returns.
    Return a DataFrame with the returns in decimal format.
    """
    # This csv file uses date format dd/mm/yyyy
    hfi = pd.read_csv(filepath, header=0, index_col=0, parse_dates=True,
                      dayfirst=True)
    hfi /= 100
    hfi.index = hfi.index.to_period('M')
    # print(hfi.info)
    # print(hfi.head)
    return hfi

def drawdown(return_series: pd.Series) -> pd.DataFrame:
    """
    Take a pd.Series time series of asset returns.
    Compute and return a DataFram that contains:
        Wealth index
        Previous peaks
        Percent drawdowns
    """
    wealth_idx = (1 + return_series).cumprod() * 1000
    prev_peaks = wealth_idx.cummax()
    drawdowns = (wealth_idx - prev_peaks) / prev_peaks  # pct drawdowns
    return pd.DataFrame({
        "Wealth"  : wealth_idx,
        "Peaks"   : prev_peaks,
        "Drawdown": drawdowns
    })

def semi_deviation(r):
    """
    Returns the semideviation of r, r is a Series or DataFrame
    """
    is_negative = r < 0
    return r[is_negative].std(ddof=0)

def skewness(r):
    """
    Alternative to scipy.stats.skew()
    Computes the skewness of the supplied Series or DataFrame
    Returns a float or a Series
    """
    demeaned_r = r - r.mean()
    # use the population standard deviation, so set ddof=0
    sigma_r = r.std(ddof=0) # set ddof=0 for population std deviation
    exp = (demeaned_r**3).mean()
    return exp/sigma_r**3

def kurtosis(r):
    """
    Alternative to scipy.stats.kurtosis()
    Computes the kurtosis of the supplied Series or DataFrame
    Return a float or a Series
    """
    demeaned_r = r - r.mean()
    # use the population standard deviation, so set ddof=0
    sigma_r = r.std(ddof=0) # set ddof=0 for population std deviation
    exp = (demeaned_r**4).mean()
    return exp/sigma_r**4

def is_normal(r, level=0.01):
    """
    Applies the Jarque-Bera test to determine if a Series is normal or not
    Test is applied at the 1% level by default
    Returns True if the hypothesis of normality is accepted, False otherwise
    """
    # The Jarque-Bera test null hypothesis is that the data is normally
    # distributed. We want a high p-value to accept the null hypothesis.
    # The p-value is the second element of the tuple. Default value of 0.01
    # implies 1% level of significance. If p-value is less than that, then
    # the null hypothesis is rejected and the data is not normally distributed.
    statistic, p_value = jarque_bera(r)
    return p_value > level

def var_historical(r, level=5):
    """
    Returns the historic Value at Risk at a specified level i.e. returns the
    number such that "level" percent (say 5%) of the returns fall below that
    number, and the (100-level) percent (95%) are above
    """
    if isinstance(r, pd.DataFrame):
        return r.aggregate(var_historic, level=level)
    elif isinstance(r, pd.Series):
        return -np.percentile(r, level)
    else:
        raise TypeError("Expected r to be Series or DataFrame")

def var_gaussian(r, level=5, modified=False):
    """
    Returns the Parametric Gaussian VaR of a Series or DataFrame
    If "modified" is True, then the modified VaR is returned using the
       Cornish-Fisher modification
    """
    # Compute the Z score assuming it was Gaussian
    z = norm.ppf(level/100)
    if modified:
        # Modify the Z score based on observed skewness and kurtosis
        s = skewness(r)
        k = kurtosis(r)
        z = (z +
            (z**2 - 1)*s/6 +
            (z**3 - 3*z)*(k-3)/24 -
            (2*z**3 - 5*z)*(s**2)/36
        )
    return -(r.mean() + z*r.std(ddof=0))

def cvar_historical(r, level=5):
    """
    Computes the Conditional VaR of Series or DataFrame
    """
    if isinstance(r, pd.Series):
        is_beyond = r <= -var_historic(r, level=level)
        return -r[is_beyond].mean() # type(is_beyond) is Series
    elif isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level=level)
    else:
        raise TypeError("Expected r to be a Series or DataFrame")

def semi_deviation(r):
    """
    Returns the semi-deviation of r, r is a Series or DataFrame
    """
    excess = r - r.mean()   # demeaned return
    excess_negative = excess[excess < 0]  # returns below mean
    # square demeaned returns below mean:
    excess_negative_squared = excess_negative**2
    n_negtive = (excess < 0).sum()  # number of negative returns
    return (excess_negative_squared.sum() / n_negtive)**0.5 # semi-deviation
#
