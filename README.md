# Is Numerical Comparison Digital? #

This project will recreate the first experiment from Dehaene et al.'s 1990 paper 'Is Numerical Comparison Digital? Analogical and Symbolic effects in Two-Digit Number Comparison'. This experiment seeks to investigate whether number comparison is done holistically or digit by digit. It does so by examining the time it takes to determine whether a presented number is bigger or smaller than a reference number, in this case 55. A list compose of the numbers 11-99 (excluding 55) is presented participants in such a way that:
1. The numbers from 41-69 are presented four times and the numbers from 11-40 and 70-99 are presented twice.
2. Two identical numbers are not presented twice in a row.
3. Three numbers bigger than 55 or three numbers smaller than 55 are not presented in a row.
4. Half of the participants are presented the list in the order in which it was created, the other half in the reverse order.

The experiment hopes to show that there is a distance effect for both reaction time and error rate for these two-digit comparisons: reaction time for numbers further from 55 should be higher and the error rate for these numbers should also be lower.


# How to Run the Experiment #
To run this experiment, first clone the online repository to a local folder. Then open the numerical_experiment.py file in this local repository using Python 3. Expyriment, pandas and random must be installed. To determine whether the pseudo-random list of numbers is presented in the normal or reverse order, the 'ORDER' constant may be set to 1 or -1.

# Data Analysis #
In order to perform the data analysis, open the numerical_data_analysis.py file from the local repository using Python 3. The Expyriment, glob, pandas, statistics, matplotlib, scipy, numpy and os libraries must be installed. The code will perform the analysis on the latest xpd file to be added to the data folder; ie for the most recent participant.
The analysis follows the first steps of data analysis from the 
My graphs.

# Extending This Project #
In order to extend this project, the data analysis script might be ammended to concatenate data from many participants. This will allow stronger statistical effects to be found as well as average out participant idiosyncracies.
This project might also be furthered by completing the data analyses on this experiment desccribed in Deheane et al. paper, including the regression of log distance on reaction time and multiple regressions examining the slope of the distance effect.
Finally, all the experiments and data analyses from this paper might be coded to control for confounding factors in the first experiment and provide further support (or rebuttals) of the holistic hypothesis.

# My Coding Experience #
Previous coding experience

