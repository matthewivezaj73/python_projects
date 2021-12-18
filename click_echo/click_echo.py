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
        click.echo("processing your csv file")