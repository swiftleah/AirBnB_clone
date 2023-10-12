#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    allowed_classes = {"BaseModel"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Creates a new line and doesnt preint anything before it"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it"""
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = arg.split()[0]
            if class_name not in self.allowed_classes:
                print("** class doesn't exist **")
                return
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            if len(args) < 2:
                print("** instance id missing **")
                return

            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)

            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in [cls.__name__ for cls in BaseModel.__subclasses__()]:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        instances = []
        if not arg:
            for key, value in storage.all().items():
                instances.append(str(value))
            print(instances)
            return
        try:
            class_name = args[0]
            class_names = [cls.__name__.lower() for cls in BaseModel.__subclasses__()]
            if class_name.lower() not in class_names:
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if class_name.lower() in key.lower():
                    instances.append(str(value))
            print(instances)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attributes"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            if class_name not in [cls.__name__ for cls in BaseModel.__subclasses__()]:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key in storage.all():
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                if len(args) < 4:
                    print("** value missing **")
                    return
                attribute_name = args[2]
                attribute_value = args[3]
                instance = storage.all()[key]
                setattr(instance, attribute_name, attribute_value)
                instance.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
