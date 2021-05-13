import expyriment
import random
import pandas as pd

exp = expyriment.design.Experiment(name="Numerical Comparison Experiment 1 Normal Order")
expyriment.control.initialize(exp)
exp.data_variable_names = ["digit", "RT","correct"]


random.seed(42)


def fill_list_to_draw_from():
	list_to_draw_from=[]
	for i in range(41,55):
		list_to_draw_from.append(i)
		list_to_draw_from.append(i)
		list_to_draw_from.append(i)
		list_to_draw_from.append(i)
	for i in range(56,70):
		list_to_draw_from.append(i)
		list_to_draw_from.append(i)
		list_to_draw_from.append(i)
		list_to_draw_from.append(i)
	for i in range(11,41):
		list_to_draw_from.append(i)
		list_to_draw_from.append(i)
	for i in range(70,100):
		list_to_draw_from.append(i)
		list_to_draw_from.append(i)
	return list_to_draw_from

def add_first_element_to_pseudo_random_list(pseudo_random_list,index_list,list_to_draw_from):
	potential_index=random.choice(index_list)
	pseudo_random_list.append(list_to_draw_from[potential_index])
	index_list.remove(potential_index)

def add_second_element_to_pseudo_random_list(pseudo_random_list,index_list,list_to_draw_from):
	potential_index=random.choice(index_list)
	if pseudo_random_list[0]!=list_to_draw_from[potential_index]:
		pseudo_random_list.append(list_to_draw_from[potential_index])
		index_list.remove(potential_index)
	else:
		add_second_element_to_pseudo_random_list(pseudo_random_list,index_list,list_to_draw_from)

def three_elements_not_all_above_or_all_below_55_checker(pseudo_random_list,index_list,list_to_draw_from,potential_index):
	if (pseudo_random_list[-1]>55 and pseudo_random_list[-2]>55 and list_to_draw_from[potential_index]>55)\
	or (pseudo_random_list[-1]<55 and pseudo_random_list[-2]<55 and list_to_draw_from[potential_index]<55):
		return False
	else:
		return True



def add_another_element_to_pseudo_random_list(pseudo_random_list,index_list,list_to_draw_from):
	potential_index=random.choice(index_list)
	if pseudo_random_list[-1]!=list_to_draw_from[potential_index] and \
	three_elements_not_all_above_or_all_below_55_checker(pseudo_random_list,index_list,list_to_draw_from,potential_index):
		pseudo_random_list.append(list_to_draw_from[potential_index])
		index_list.remove(potential_index)
	else:
		add_another_element_to_pseudo_random_list(pseudo_random_list,index_list,list_to_draw_from)


def fill_pseudo_random_list(list_to_draw_from):
    pseudo_random_list=[]
    index_list=list(range(232))
    add_first_element_to_pseudo_random_list(pseudo_random_list,index_list,list_to_draw_from)
    add_second_element_to_pseudo_random_list(pseudo_random_list,index_list,list_to_draw_from)
    for i in range(2,230):
        add_another_element_to_pseudo_random_list(pseudo_random_list,index_list,list_to_draw_from)
    pseudo_random_list.append(list_to_draw_from[index_list[0]])
    pseudo_random_list.append(list_to_draw_from[index_list[1]]) #to avoid a recursion error
    return pseudo_random_list,index_list

list_to_draw_from=fill_list_to_draw_from()
pseudo_random_list=fill_pseudo_random_list(list_to_draw_from)[0]
training_list=[34,56,78,45,12,32,67,87,90,42]

	
instructions_initial = expyriment.stimuli.TextScreen("Instructions",
    f"""Two digit numbers, distributed around 55, will appear on the screen.
    Press the right-hand response key if the number is
	larger than 55, or the left-hand key if the number is smaller than
	55. Please respond as fast as possible whilst keeping errors to a minimum.
	You will be presented with 10 numbers to practice with before the 
	experiment starts. 

    Press the space bar to start.""")

instructions_experiment_start = expyriment.stimuli.TextScreen("Instructions",
    f"""The training set is over. The experiment will start when you press
    the space bar. It will last approximately 30 minutes""")


blankscreen=expyriment.stimuli.BlankScreen()
training_block = expyriment.design.Block(name="Training Block")
experiment_block = expyriment.design.Block(name="Experiment Block")


for number in training_list:
    trial=expyriment.design.Trial()
    trial.set_factor('number',number)
    training_block.add_trial(trial)

for number in pseudo_random_list[0:5]:
    trial=expyriment.design.Trial()
    trial.set_factor('number',number)
    experiment_block.add_trial(trial)

expyriment.control.start(skip_ready_screen=True)
instructions_initial.present()
exp.keyboard.wait()

for trial in training_block.trials:
	digit = trial.get_factor("number")
	target = expyriment.stimuli.TextLine(text=str(digit), text_size=60)
	target.present()
	key, rt=exp.keyboard.wait([expyriment.misc.constants.K_LEFT, expyriment.misc.constants.K_RIGHT])
	exp.clock.wait(2000-rt)
	blankscreen.present()
	exp.clock.wait(2000)

instructions_experiment_start.present()
exp.keyboard.wait()
exp.clock.wait(500)


for trial in experiment_block.trials:
	digit = trial.get_factor("number")
	target = expyriment.stimuli.TextLine(text=str(digit), text_size=60)
	target.present()
	key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT, expyriment.misc.constants.K_RIGHT])
	correct=True
	if digit<55:
		if key==expyriment.misc.constants.K_RIGHT:
			correct=False
	if digit>55:
		if key==expyriment.misc.constants.K_LEFT:
			correct=False
	exp.clock.wait(2000-rt)
	blankscreen.present()
	exp.clock.wait(2000)
	exp.data.add([digit, rt,correct])

expyriment.control.end()
# experiment_data=expyriment.misc.data_preprocessing.read_datafile("data/numerical_experiment_10_202105111736.xpd", only_header_and_variable_names=False, encoding=None, read_variables=None)
# print(experiment_data)
# import glob
# for datafile in glob.glob('data/*.xpd'):
#      data = pd.read_csv(datafile, comment='#')
#      print(data)


# block_one = expyriment.design.Block(name="Training Block")
# trial_one = expyriment.design.Trial()
# stim = expyriment.stimuli.TextLine(text="45", text_size=80)
# stim.preload()
# trial_one.add_stimulus(stim)
# trial_two = expyriment.design.Trial()
# stim = expyriment.stimuli.TextLine(text="I am a stimulus in Block 1, Trial 2")
# trial_two.add_stimulus(stim)
# block_one.add_trial(trial_one)
# block_one.add_trial(trial_two)
# exp.add_block(block_one)






# expyriment.control.start()

# for block in exp.blocks:
#     for trial in block.trials:
#         trial.stimuli[0].present()
#         key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
#                                      expyriment.misc.constants.K_RIGHT])
#         exp.data.add([block.name, trial.id, key, rt])


# expyriment.control.end()