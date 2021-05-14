import glob
import expyriment
import pandas as pd
from statistics import mean
import matplotlib.pyplot as plt
from scipy.stats import sem
import numpy as np
from scipy import stats




# experiment_data=expyriment.misc.data_preprocessing.read_datafile("data/numerical_experiment_10_202105111736.xpd", only_header_and_variable_names=False, encoding=None, read_variables=None)
# print(experiment_data)
# for datafile in glob.glob('data/*.xpd'):
#      data = pd.read_csv(datafile, comment='#')
#      print(data)
# expyriment.misc.data_preprocessing.write_concatenated_data()


data,variables,subject_info,comments=expyriment.misc.data_preprocessing.read_datafile('C:/Users/maxim/OneDrive/Desktop/Numerical-Comparison_git/data/numerical_experiment_20_202105141706.xpd',\
 only_header_and_variable_names=False, encoding=None, read_variables=None)
print(data)
print(variables)

def extract_numbers_and_associated_reaction_times_discounting_errors(data):
	number_list=[]
	rt_list=[]
	for i in range(len(data)):
		if data[i][3]== 'True':
			number_list.append(int(data[i][1]))
			rt_list.append(int(data[i][2]))
	return [number_list,rt_list]

def extract_numbers_from_data_in_order_of_presentation(data):
	all_numbers_list=[]
	for i in range(len(data)):
		all_numbers_list.append(int(data[i][1]))
	return all_numbers_list


def create_and_get_mean_and_standard_error_of_list_from_list_of_indices(indices,list):
	list_from_indices=[]
	for index in indices:
		list_from_indices.append(list[index])
	return [mean(list_from_indices),sem(list_from_indices)]


def get_mean_rt_and_standard_error(number_list,rt_list,range_list):
	mean_reaction_times_list=[]
	standard_error_list=[]
	for number in range_list:
		if number in number_list:
			indices = [i for i, x in enumerate(number_list) if x == number]
			mean_reaction_times_list.append(create_and_get_mean_and_standard_error_of_list_from_list_of_indices\
				(indices,rt_list)[0])
			standard_error_list.append(create_and_get_mean_and_standard_error_of_list_from_list_of_indices\
				(indices,rt_list)[1])
	return [mean_reaction_times_list,standard_error_list]

range_list=list(range(11,100))
range_list.remove(55)

number_and_rt_list=extract_numbers_and_associated_reaction_times_discounting_errors(data)
mean_rt_and_standard_error_list=get_mean_rt_and_standard_error(number_and_rt_list[0],number_and_rt_list[1],range_list)
print(mean_rt_and_standard_error_list)

plt.figure()
plt.errorbar(range_list,mean_rt_and_standard_error_list[0], yerr=mean_rt_and_standard_error_list[1],linestyle=':')
plt.plot(np.full((20,1),55),np.linspace(400,1400,20), '--')
plt.xlabel('number')
plt.ylabel('mean reaction time(ms)')


def count_correct_reponses_for_a_given_number(number,number_list,data):
	true_counter=0
	false_counter=0
	indices = [i for i, x in enumerate(number_list) if x == number]
	for i in indices:
		if data[i][3]=='True':
			true_counter+=1
		else:
			false_counter+=1
	return true_counter,false_counter


def get_error_rate_by_number(range_list,number_list,data):
	error_rate_list=[]
	for number in range_list:
		if number in number_list:
			true_counter,false_counter=\
			count_correct_reponses_for_a_given_number(number,number_list,data)
			if true_counter==0:
				error_rate_list.append(1)
			elif false_counter==0:
				error_rate_list.append(0)
			else:
				error_rate_list.append(false_counter/(true_counter+false_counter))
	return error_rate_list

all_numbers_list=extract_numbers_from_data_in_order_of_presentation(data)
error_rate_by_number_list=get_error_rate_by_number(range_list,all_numbers_list,data)

def distance_from_55(range_list):
	distance_from_55_list=[]
	for i in range_list:
		distance_from_55_list.append(np.log(np.absolute(55-i)))
	return distance_from_55_list

distance_from_55_list=distance_from_55(range_list)
print(distance_from_55_list)
print(error_rate_by_number_list)


gradient, intercept, r_value, p_value, std_err = stats.linregress(distance_from_55_list,error_rate_by_number_list)
x=np.linspace(np.min(distance_from_55_list),np.max(distance_from_55_list),500)
y=gradient*x+intercept

plt.figure()
plt.plot(distance_from_55_list,error_rate_by_number_list,'ob')
plt.plot(x,y,'-r',label='p='+str(p_value))
plt.legend()
plt.xlabel('logarithm of absolute distance from 55')
plt.ylabel('error rate')
plt.show()






