names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict={
    "country": names,
    "driver_right" : dr,
    "cars_per_cap" : cpc
}

import pandas as pd
cars= pd.DataFrame(my_dict)

print(cars)

