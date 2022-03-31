# messagebox
Simple python scripts to read text from a github gist, and then display this text on a 16x2 screen
* launcher.sh - simple shell script used to run *messagebox.py* at start-up
* messages.py - python code containing a continuous loop fetching from a github gist file that contains the text that you'd like to display.
* scrolling_text.py - the python code that displays the text on the 16x2 LCD screen. The text scrolls across the desired row and then displays the entire text.
* servo.py - python code used to contol the MicroServo. Used in *messagebox.py* when a new message is received.
