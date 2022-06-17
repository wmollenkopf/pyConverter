import PySimpleGUI as sg

# Rows->Columns layout
layout = [
	[sg.Input(key='-INPUT-'), sg.Spin(['km to mile','kg to pound','sec to min'],key='-UNITS-'), sg.Button('Convert', key='-CONVERT-')],
	[sg.Text('', key='-OUTPUT-')]
]

# Assign the sg.Window to a window variable
window = sg.Window('Converter',layout)

# Keep the window alive while awaiting input from user
while True:

	# Deconstruct events and values from the window read event
	# upon an event trigger, 
	# the event itself and all values will be deconstructed into variables.
	event, values = window.read()

	# Close the window if the Window close button is pressed
	if event == sg.WIN_CLOSED:
		break #break will stop the read loop, and trigger a final window close event in the code

	# If the convert button event is triggered,
	# Obtain the value of the value input into the text box
	# Place the units value into a variable for faster referrence
	# Branch into what should be done based on the unit conversion selected
	# Place output into the -OUTPUT- text feild
	if event == '-CONVERT-':
		input_value = values['-INPUT-']
		units_value = values['-UNITS-']
		if input_value.isnumeric():
			if units_value == 'km to mile':
				output = round(float(input_value) * 0.6214,2)
				output_string = f'{input_value} km are {output} miles.'
				window['-OUTPUT-'].update(output_string)
			if units_value == 'kg to pound':
				output = round(float(input_value) * 2.20462,2)
				output_string = f'{input_value} kg are {output} pounds.'
				window['-OUTPUT-'].update(output_string)
			if units_value == 'sec to min':
				output = round(float(input_value) / 60,2)
				output_string = f'{input_value} seconds are {output} minutes.'
				window['-OUTPUT-'].update(output_string)
				
# After looping is over, close the window
window.close()
