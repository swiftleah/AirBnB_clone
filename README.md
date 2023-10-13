The tasks throughout this project create the first step to cloning AirBnb.
We are writing a command interpreter to manage our AirBnB objects.
During this project, we:
- create a parent class called BaseModel which will take care of initialization, serialization & deserialization of our future instances.
- create a simple flow of serialization & deserialization from creating an instance -> Dictionary -> JSON string -> file.
- create classes necessary for AirBnb like 'place', 'city', 'user', etc.. that will inherit from our parent class BaseModel.
- create storage engine for the project: 'File Storage' where serialization & deserialization will take place.
- create unittests to validate all our classes & storage engine.
- create the console which will be the entry point for our command interpreter.


The command interpreter works as a shell. It displays a prompt, waits for input from the user and executes a command.
- we start the command interpreter by saying './console.py'
- 'quit' to exit
- 'EOF' to exit
- 'help' to display different commands available and how to use them
- different actions you can perform include:
	- creating an instance with 'create BaseModel' which will save it to JSON file and print the id.
	- 'show {instance}' which will print the string representation of an instance based on the class name and id.
	- 'destroy {instance}' will destroy instance based on class name and id.
	- 'all {instance}' will print all string representation of instances based or not on the class name.
	- 'update {instance}' will update specified instance based on the class name and id by adding (appending) or updating attribute and save the changes to JSON file.
