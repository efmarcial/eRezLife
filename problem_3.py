#!/usr/bin/env python3


text = ['a','b','c','d','e','f']

def recursive(array, left_counter, right_counter):



	# init by checking if we need to move left to right or in reverse in the array
	# if left_counter is less then the lenght of the array then we move to the right
	if left_counter < right_counter:

		# "  " * left_counter , multiples the spaces nessacary for that element
		# format the string element to add <> around that element
		print("  "* left_counter, f"<{array[left_counter]}>")

		# Restart the function and increment the left_counter by 1 to travers the array to right by 1
		recursive(array , left_counter+1, right_counter)


	# if left_counter reaches the end of the array we restart to travers the array in reverses unilt it reaches 0
	elif right_counter == left_counter or right_counter != 0:

		print("  " * (right_counter-1), f"</{array[right_counter-1]}>")

		recursive(array, left_counter, right_counter-1)


# Run recursive() function
if __name__ == "__main__":

	# Initalize funciton by stating at left of the array with left_counter and
	# set the right_counter to length of the array

	recursive(text, left_counter = 0, right_counter = len(text))
