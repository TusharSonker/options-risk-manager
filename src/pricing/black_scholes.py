import math
from scipy.stats import norm
def option_pricing(S,T,r,sigma,K,option_type):
    d1 = ((math.log(S/K)) + (r + (sigma**2) / 2) * T) / ((sigma) * math.sqrt(T))
    d2 = d1 - ((sigma) * math.sqrt(T))
    if option_type == 'C':
        n_d1 = norm.cdf(d1)
        n_d2 = norm.cdf(d2)
        call_option_price = (S * n_d1) - (K * (math.e ** (-r * T)) * n_d2)
        return round(call_option_price, 4)
    else:
        n_d1 = norm.cdf(-d1)
        n_d2 = norm.cdf(-d2)
        put_option_price = ((K * (math.e**(-r * T)) * n_d2) - (S * n_d1))
        return round(put_option_price, 4)
    

    
