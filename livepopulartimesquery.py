#!/usr/bin/python
# coding: utf-8

# Copyright (C) 2021 LincolnLandDFIR
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2, as published by the
# Free Software Foundation
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details (http://www.gnu.org/licenses/gpl.txt).


############################        Imports        ############################

import pandas as pd
import livepopulartimes	# python3 -m pip install LivePopularTimes


############################       Pre-Sets        ############################

author = 'LincolnLandDFIR'
description = "query google popular times for a location";
location = '(Chick-fil-A) 2301 N Prospect Ave, Champaign, IL 61822'
# output = 'week.csv'
output = 'PopularTimes.xlsx'
version = '1.0.2'


############################      Sub-Routines     ############################

data = livepopulartimes.get_populartimes_by_address(location)

print('Popular times for: ', location)

d1=data['populartimes']
df = pd.DataFrame()
col_list=[]
for i in range(len(d1)):
   m = d1[i]
   df[i]=m['data']
   col_list.append(m['name'])

df.columns=col_list
# df.to_csv(output)
df.to_excel(output, sheet_name='PopularTimes')

############################   Revision History   #############################

"""
1.0.0 - added excel output
0.1.2 - got module to work
"""


############################   Future Wishlist     ############################

"""
append the location and date run into the file.

"""


############################          Notes          #############################

"""
https://github.com/GrocerCheck/LivePopularTimes
python3 -m pip install LivePopularTimes

"""


############################        The End        ############################

