# Carbon-Intensity-API-wrapper
A python wrapper for the UK Carbon Intensity API.

https://api.carbonintensity.org.uk/

## Example usage:
```python
import ci_api_wrapper as ci

x = ci.CarbonIntensityAPI(date='2020-08-25T15:30Z', #  Create carbon intensity api object to hold the data
                          period='5',
                          start='2020-08-20T15:30Z',
                          end='2020-08-22T15:30Z',
                          block='2',
                          postcode='CV5')

print(x.factors) #  Print current carbon intensity factors
print(x.intensity_pt24h) #  Print carbon intensity for 24h before the specified date
```

Use help(ci_api_wrapper) for a list of attributes and methods.
