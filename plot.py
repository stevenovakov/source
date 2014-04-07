#!/usr/bin/env python3
from pylab import *
from scipy import *

# CFRI machine, 100,000 particles, two reducers, varying steplengths.
steplengths = (10,100,1000,10000,100000)
sl_times = ((15.2,13.6,14.5),
            (15.0,13.8,14.8),
            (14.3,14.7,15.2),
            (11.3,12.5,12.0),
            (69.9))

sl_avg = [average(time) for time in sl_times]
sl_std = [std(time) for time in sl_times]

# CFRI machine, 100,000 particles, 10,000 steps, varying reducers.
reducers = (1,2,3,4,5,6)
red_times = ((12.7,12.3,13.3),
             (12.0,12.7,11.8),
             (11.3,12.0,11.5),
             (11.9,11.1,11.9),
             (12.3,12.5,11.8),
             (11.4,10.7,11.2))

red_avg = [average(time) for time in red_times]
red_std = [std(time) for time in red_times]

# Plot SL vs. time
errorbar(steplengths, sl_avg, yerr=sl_std)
semilogx()
xlim((1e0,1e6))
ylim((10,75))
xlabel("Number of steps per interpolation kernel")
ylabel("Runtime")
savefig('images/collatz_stepsper.pdf')

# Plot RedCount vs. time
clf()
errorbar(reducers, red_avg, yerr=red_std)
xlabel("Number of reduction threads")
xlim((.5,6.5))
ylabel("Runtime")
savefig('images/collatz_workpool.pdf')
