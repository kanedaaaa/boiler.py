#!/usr/bin/env python3

from boiler import Boiler
import inquirer
import time
from halo import Halo

def main():
  boiler = Boiler()

  questions = [
    inquirer.List('type',
                  message="Pick your boilerplate",
                  choices=["Node.js", "JavaScript", "TypeScript", "Exit"])
  ]

  answers = inquirer.prompt(questions)

  if answers['type'] == "Node.js":
    questions = [
      inquirer.Text('name', message="Name of your project"),
      inquirer.List('type',
                    message="Pick your boilerplate",
                    choices=["Express Server", "React App", "Exit"])
    ]

    answers = inquirer.prompt(questions)

    if answers['type'] == "Express Server":
      print("Creating Node.js Express Server")
      spinner = Halo(text='Loading', spinner='dots')
      spinner.start()
      boiler.node(answers['name'], "express-server")
      time.sleep(0.5)
      spinner.stop()
      print("Done! (Yes, i do have time.sleep() right above this for aesthetics. Anyways, good luck)")

    elif answers['type'] == "React App":
      print("Not implemented yet")
      return

    elif answers['type'] == "Exit":
      print("Bye!")
      return

    else:
      print("Error: Unknown type")
      return
  
  elif answers['type'] == "JavaScript":
    print("Not implemented yet")
    return

  elif answers['type'] == "TypeScript":
    print("Not implemented yet")
    return

  elif answers['type'] == "Exit":
    print("Bye!")
    return
  
  else: 
    print("Error: Unknown choice")  

main()