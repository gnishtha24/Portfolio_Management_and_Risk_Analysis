##to make a module with some of the finance related terms

import numpy as np 

def skewness(data): 
    data= np.array(data)  #convert data in array form

    mean= np.mean(data)   #calculate mean and standard deviation of the data
    std= np.std(data)
    n = len(data)

    skewnes= (1/n) * np.sum(((data-mean)/ std) ** 3)    #formula

    return skewness

def kurtosis(data):
    data= np.array(data)   ##convert data in array form
    n = len(data)          


    kurtosis= (1/n) * np.sum(((data-mean)/ std) ** 4)- 3    #formula

    return kurtosis

def annualised_return(cumulative_return, days_held):
    
    annualised_return= ((1+ cumulative_return)** (365/days_held)) -1    #formula

    return annualised_return

def annualised_volatility(data):

    std= np.std(data)   #calculating standard deviation of database
    annualised_volatility = std * np.sqrt(252)  #formula

    return annualised_volatility

def sharpe_ratio(returns):

    avg_return= np.mean(returns)    #calculating average return in data

    #here, i am taking risk free rate as 3%
    sharpe_ratio= (avg_return - 0.03)/ annualised_volatility    #formula

    return sharpe_ratio

def jarque_bera(data):
    n = len(data)
    jarque_bera= (1/n)* ((skewness)**2 + ((kurtosis-3)**2)/4)   #formula

    return jarque_bera

def drawdown(initial_inv, returns):

    wealth_index= initial_inv*(1+returns).cumprod()     #calcualting and plotting wealth index
    wealth_index.plot()

    previous_peaks= wealth_index.cummax()   #calculating and plotting prev peaks
    previous_peaks.plot()

    drawdown= (wealth_index - previous_peaks)/previous_peaks    #plotting drawdown
    drawdown.plot()

    return pd.Dataframe({"Wealth": wealth_index,
    "Previous Peak": previous_peaks,
    "Drawdown": drawdown})

def semi_deviation (returns):

    n = len(returns)
    mean = np.mean(returns) #calculating mean of returns

    squared_diff = [(ret - mean) ** 2 for ret in returns if ret < mean]
    semi_dev = (sum(squared_diff) / n) ** 0.5    #formula

    return semi_dev

def historical_VaR(returns, alpha):
    returns = np.array(returns)
    sorted_returns = np.sort(returns)

    ind = int(alpha * len(sorted_returns))  #ind=index
    hVaR = -sorted_returns[ind]

    return hVaR

def historical_CVaR(returns, alpha):
    returns = np.array(returns)
    sorted_returns = np.sort(returns)

    ind = int(alpha * len(sorted_returns))
    hCVaR = -sorted_returns[ind]

    return hCVaR

def gaussian_VaR(returns, alpha):

    mean = np.mean(returns)
    std = np.std(returns)

    gVaR = -mean - std * np.percentile(np.random.normal(0, 1, 100000), alpha * 100) #formula

    return gVaR

def gaussian_CVaR(returns, alpha):

    mean = np.mean(returns)
    std = np.std(returns)

    gCVaR = -mean - std * (np.exp(-0.5 * (np.percentile(np.random.normal(0, 1, 100000), alpha * 100)) ** 2) / (1 - alpha))  #formula

    return gCVaR


