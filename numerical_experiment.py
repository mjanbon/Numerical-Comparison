import expyriment
import random

exp = expyriment.design.Experiment(name="Numerical Comparison Experiment 1 Normal Order")
expyriment.control.initialize(exp)
exp.data_variable_names = ["Block", "Trial", "Key", "RT"]



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
pseudo_random_list=fill_pseudo_random_list(list_to_draw_from)
	


for number in pseudo_random_list[0:20]:
    trial=expyriment.design.Trial()
    trial.set_factor('number',number)

    blankscreen.present()
    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    exp.clock.wait(waiting_time)
    target.present()
    key, rt = exp.keyboard.wait(duration=MAX_RESPONSE_DELAY)
    exp.data.add([i_trial, waiting_time, key, rt])



block_one = expyriment.design.Block(name="Training Block")
trial_one = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="45", text_size=80)
stim.preload()
trial_one.add_stimulus(stim)
trial_two = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="I am a stimulus in Block 1, Trial 2")
trial_two.add_stimulus(stim)
block_one.add_trial(trial_one)
block_one.add_trial(trial_two)
exp.add_block(block_one)






# expyriment.control.start()

# for block in exp.blocks:
#     for trial in block.trials:
#         trial.stimuli[0].present()
#         key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
#                                      expyriment.misc.constants.K_RIGHT])
#         exp.data.add([block.name, trial.id, key, rt])


# expyriment.control.end()