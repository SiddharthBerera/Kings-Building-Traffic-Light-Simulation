# Kings-Building-Traffic-Light-Simulation
An ineractive traffic light simulation, of the TOUCAN traffic light system around the King's Building.
The program uses the python package Tkinter to produce a GUI in which it displays the the traffic lights.
The traffic lights then cycle through its finite states infinitely and the timings for each state are altered
by the interactive pedestrian wait button that can be pressed.
The program makes use of multithreading, the GUI window which constantly is detecting any movement in the GUI runs on one thread.
And the simulations infinite cycle on another thread - note there is a quit button to exit the program.
This was submitted as my coursework 1 project for one of my Univeristy Courses - Programming Skills for Engineers 2.
