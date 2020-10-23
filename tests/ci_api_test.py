# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:07:29 2020.

@author: Joshu
"""

import sys

import ci_api_wrapper as ci


def ci_test():
    """Test for ci api wrapper."""
    x = ci.CarbonIntensityAPI(date='2020-08-25T15:30Z',
                              period='5',
                              start='2020-08-20T15:30Z',
                              end='2020-08-22T15:30Z',
                              block='2',
                              postcode='CV5')

    dno = 'London'

    print(x.intensity_now(),
          x.window_now(),
          x.intensity_today(),
          x.window_today(),
          x.intensity_date(),
          x.window_date(),
          x.intensity_fw24h(),
          x.window_fw24h(),
          x.intensity_fw48h(),
          x.window_fw48h(),
          x.intensity_pt24h(),
          x.window_pt24h(),
          x.intensity_period(),
          x.window_period(),
          x.stats_block(),
          x.generation(),
          x.generation_pt24h(),
          x.generation_from_to(),
          x.regional_generation_from_to(dno),
          x.postcode_generation_from_to(),
          x.england(),
          x.scotland(),
          x.wales(),
          x.region(dno),
          x.region_fw24h(dno),
          x.region_fw48h(dno),
          x.region_pt24h(dno),
          x.postcode_generation(),
          x.postcode_intensity(),
          x.postcode_fw24h(),
          x.postcode_fw48h(),
          x.postcode_pt24h())

    y = ci.CarbonIntensityAPI(date='2020-08-25T15:30Z',
                              period='5',
                              start='2020-08-20T15:30Z',
                              end='2020-08-22T15:30Z',
                              postcode='CV5')
    print(y.stats())


original_stdout = sys.stdout

with open('testfile.txt', 'w') as f:
    sys.stdout = f
    print(ci_test())
    sys.stdout = original_stdout
