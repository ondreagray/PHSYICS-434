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
z = 3.5
table = stats.norm.cdf(z)
print(stats.norm.ppf(0.84))
print(stats.norm.ppf(0.99))
# For z = 1, python outputed the value 0.841 which matches the z-table
# found on wikipedia at https://en.wikipedia.org/wiki/Standard_normal_table.

#C.
# In this example we calculate the inverse function of above. Instead of
# entering a sigma value we enter a probability and want the associated
# sigma. To show this, I saved the value given by th cdf function and entere
# it into the ppf function and received the original val;ue (z = 1) back.
percentage = stats.norm.ppf(table)

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
plt.xlim([0, 3.5])
plt.hist(r1, 50, density=True)
x1 = np.linspace(0,3.5,100000)
plt.plot(x1,stats.lognorm.pdf(x1,s1), label='s = 0.340')

figure(2)
plt.hist(r2, 50, density=True)
plt.xlim([0, 7])
x2 = np.linspace(0,7,100000)
plt.plot(x2,stats.lognorm.pdf(x2,s2), label='s = 0.626')
plt.legend()

figure(3)
plt.xlim([0, 12])
plt.hist(r3, 50, density=True)
x3 = np.linspace(0,12,100000)
plt.plot(x3,stats.lognorm.pdf(x3,s3), label='s=0.954')
plt.legend()

#SECTION 1.3

#A.
# I have selected a value relevant to my first graph (Figure 1) of x = 1.5.
# From the histogram this x value has a relatively high probability.

#B.
# The question we want to ask is "if we have a signal-free, lognormal background
# distribution, what is the probability of a chosen measurement being from our
# background and what value of the standard deviation (sigma) does this probability
# correspond to in a normal distribution?"

#C.

#D./E.

measurement = 1.5
prob = stats.lognorm.cdf(measurement,s1)
sigma = stats.norm.ppf(prob)
print(prob)

#A. I chose the Binomial distribution. The binomial distribution
figure(4)
a = np.random.binomial(100000, 0.5)
b = np.random.binomial(100000, 0.25)
c = np.random.binomial(100000, 0.75)

x = np.arange(-20,20,1)
plt.step(x,stats.binom.pmf(x,10,0.5),label = 'k = x : n = 10 : p = 0.5')
plt.step(x,stats.binom.pmf(x,10,0.1),label = 'k = x : n = 10 : p = 0.1')
plt.step(x,stats.binom.pmf(x,10,0.7),label = 'k = x : n = 10 : p = 0.7')
plt.legend()

k = 10
n = 100
p = 0.25
probBinom = stats.binom.cdf(k,n,p)
sigBinom =stats.norm.ppf(probBinom)
print(sigBinom)
print(probBinom)


