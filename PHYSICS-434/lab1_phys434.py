import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import pylab
from pylab import *
import scipy
from scipy import stats
import plotly.graph_objects as go

#*** PART 1 --> A LITTLE STATISTICS ***

#SECTION 1.1

#A.
# The normal distribution or gaussian, is the standard distribution for
# most probabilistic data. It is a bell-shaped curve that centers around
# an average value with the highest incidence, with values far from the
# average decreasing in incidence.

#B.
# Below is the integration of the standard normal distribution.
# This integration goes from negative infinity to the given value of z.
z = 1
table = stats.norm.cdf(z)
print(table)
# For z = 1, python outputed the value 0.841 which matches the z-table
# found on wikipedia at https://en.wikipedia.org/wiki/Standard_normal_table.

#C.
# In this example we calculate the inverse function of above. Instead of
# entering a sigma value we enter a probability and want the associated
# sigma. To show this, I saved the value given by th cdf function and entere
# it into the ppf function and received the original val;ue (z = 1) back.
percentage = stats.norm.ppf(table)
print(percentage)

#D.
# The ppf function returns a sigma value that is centered around a mean
# of zero. So if the sigma value returned is negative it just means the
# sigma associated with that probability is on the left of the mean. 


#SECTION 1.2

#A.
# I chose the Lognormal distribution. In this distribution, the data
# variable x is distributed such that if you take log(x) = y, y is normally
# distributed. This distribution is fairly common and used to model the time
# it takes to solve a Rubik's cube, the size of living tissues and city size.
# https://en.wikipedia.org/wiki/Log-normal_distribution#Occurrence_and_applications

#B. See Figure 1
s1 = 0.340
s2 = 0.626
s3 = 0.954

r1 = stats.lognorm.rvs(s1, size = 100000)
r2 = stats.lognorm.rvs(s2, size = 100000)
r3 = stats.lognorm.rvs(s3, size = 100000)

figure(1)
plt.hist(r1, 50, density=True)
plt.xlim([0, 3.5])
x1 = np.linspace(0,3.5,100000)
plt.plot(x1,stats.lognorm.pdf(x1,s1))

figure(2)
plt.hist(r2, 50, density=True)
plt.xlim([0, 7])
x2 = np.linspace(0,7,100000)
plt.plot(x2,stats.lognorm.pdf(x2,s2))

figure(3)
plt.hist(r3, 50, density=True)
plt.xlim([0, 12])
x3 = np.linspace(0,12,100000)
plt.plot(x3,stats.lognorm.pdf(x3,s3))

plt.show()

#SECTION 1.3

#A.
# I have selected a value relevant to my first graph (Figure 1) of x = 1.5.
# From the histogram this x value has a relatively high probability but is
# still far enough from the mean which is centered around 1.

#B.
# The question we want to ask is "what is the standard deviation (sigma)
# of the measurement value 1.5 for a lognormal distribution with parameter
# s = 0.340?".

#C.

sig = np.std(r1)
print(sig)
x = 1.5
num_std = x/sig
print(num_std)


