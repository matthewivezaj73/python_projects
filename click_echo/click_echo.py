#Importing libraries.
import click
#Adding a flag.
not_done = False
#Testing for user input.
while not not_done:
    #Asking the user to enter a choice.
    do_something = input("Please enter \'csv\' if you would like to create a csv file.\n\n")
    #Handling the case where the user enters csv.
    if do_something.lower() == "csv":
        #Asking the user to input text.
        content = input("Please enter the text that you would like to enter into the csv file for the first row: ")
        click.echo("processing your csv file...")