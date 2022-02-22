# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:28:17 2022

"""

import numpy as np
import pandas as pd

def weekRange(df):
    '''
    Parameters
    ----------
    df : Series, np.datetime64 object
        DESCRIPTION.

    Returns
    -------
    TYPE : str
        DESCRIPTION.
    
    每年第一天以ISOCALENDAR.YEAR一致
    每周起始日期 = 每年第一天日期 + 对应日期周数 * 7 + 第一天星期数 - 1
    每周结束日期 = 每年第一天日期 + 对应日期周数 * 7 + 第一天星期数 - 1 + 6
    '''
    first_day_of_year = pd.to_datetime(str(df.isocalendar().year)+'-01-01')
    week_of_year = df.weekofyear
    weeknum_of_first_day_of_year = first_day_of_year.dayofweek
    自然周第一天 = first_day_of_year + \
            pd.Timedelta(days=week_of_year*7 + weeknum_of_first_day_of_year)
    自然周最后一天 = first_day_of_year + \
            pd.Timedelta(days=week_of_year*7 + weeknum_of_first_day_of_year + 6)
    return str(自然周第一天).replace('-','.')[2:10]+'-' \
               +str(自然周最后一天).replace('-','.')[2:10]