#!/usr/bin/python3

"""Creating the console for command line interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class for the command interpreter"""

    prompt = "(hbnb) "
    listClass = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                 'Review']

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Command for end-of-file and quit
        """
        return True

    def emptyline(self):
        """To cancel out repeating last command when empty command enter"""
        pass

    def do_create(self, arg):
        """Command to creates a new instance of the class
        """
        if arg != "":
            if arg in HBNBCommand.listClass:
                newInstance = eval(arg)()
                newInstance.save()
                print(newInstance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Show string representation of instance based on class name and id
        """
        response = arg.split(" ")

        if arg == "":
            print("** class name missing **")
        elif response[0] not in HBNBCommand.listClass:
            print("** class doesn't exist **")
        else:
            try:
                if response[1]:
                    objId = f"{response[0]}.{response[1]}"
                    savedInstance = storage.all()
                    if objId not in savedInstance.keys():
                        print("** no instance found **")
                    else:
                        print(savedInstance[objId])
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """Command to delete an instance based on the class name and id
        """
        response = arg.split(" ")

        if arg == "":
            print("** class name missing **")
        elif response[0] not in HBNBCommand.listClass:
            print("** class doesn't exist **")
        else:
            try:
                if response[1]:
                    objId = f"{response[0]}.{response[1]}"
                    savedInstance = storage.all()
                    if objId not in savedInstance.keys():
                        print("** no instance found **")
                    else:
                        del (savedInstance[objId])
                        storage.save()
            except IndexError:
                print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string repr of instances based or not on class name
        """
        instances = []
        savedInstance = storage.all()
        if arg == "":
            for inst in savedInstance.values():
                instances.append(str(inst))
            print(instances)
        else:
            if arg in HBNBCommand.listClass:
                for key, value in savedInstance.items():
                    clname = key.split(".")
                    if arg == clname[0]:
                        instances.append(str(value))
                print(instances)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updating or adding to an instance based on class name
        """
        response = arg.split(" ")
        savedInstance = storage.all()
        if arg == "":
            print("** class name missing **")
            return
        else:
            clname = response[0]
            #ids = response[1]
            #attr = response[2]
            #val = response[3].strip('"')
            #objId = f"{clname}.{ids}"
            if len(response) == 1:
                if clname not in HBNBCommand.listClass:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif len(response) == 2:
                ids = response[1]
                objId = f"{clname}.{ids}"
                if clname not in HBNBCommand.listClass:
                    print("** class doesn't exist **")
                elif objId not in savedInstance.keys():
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
            elif len(response) == 3:
                ids = response[1]
                objId = f"{clname}.{ids}"
                if clname not in HBNBCommand.listClass:
                    print("** class doesn't exist **")
                elif objId not in savedInstance.keys():
                    print("** no instance found **")
                else:
                    print("** value missing **")
            elif len(response) == 4:
                ids = response[1]
                attr = response[2]
                val = response[3].strip('"')
                objId = f"{clname}.{ids}"
                if clname not in HBNBCommand.listClass:
                    print("** class doesn't exist **")
                elif objId not in savedInstance.keys():
                    print("** no instance found **")
                else:
                    setattr(savedInstance[objId], attr, val)
                    savedInstance[objId].save()
        #except IndexError:
            #print("** no instance found **")

        '''
        try:
            if len(response) >= 4:
                objId = f"{response[0]}.{response[1]}"
                val = response[3]
                val = val.strip('"')
                setattr(savedInstance[objId], response[2], val)
                savedInstance[objId].save()
            elif arg == "":
                print("** class name missing **")
            elif response[0] not in HBNBCommand.listClass:
                print("** class doesn't exist **")
            elif (f"{response[0]}.{response[1]}") not in savedInstance.keys():
                print("** no instance found **")
            #elif len(response) == 1:
                #print("** instance id missing **")
            elif len(response) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
        except IndexError:
            print("** instance id missing **")
        '''

    def do_count(self, arg):
        """Command to count the number of instances of a class
        """
        savedInstance = storage.all()
        if arg == "":
            print("** class name missing **")
        else:
            if arg in HBNBCommand.listClass:
                num = 0
                for key in savedInstance.keys():
                    if arg in key:
                        num += 1
                print(num)
            else:
                print("** class doesn't exist **")

    def default(self, arg):
        """To command using class name followed by argument e.g User.all()
        """
        response = arg.split(".")
        clname = response[0]
        if len(response) == 1:
            print(f"*** Unknown syntax: {clname}")
            return
        try:
            args = response[1].split("(")
            command = args[0]
            if command == "all" and response[1] == "all()":
                HBNBCommand.do_all(self, clname)
            elif command == "count" and response[1] == "count()":
                HBNBCommand.do_count(self, clname)
            elif command == "show":
                cls_id = args[1].strip(')"')
                cls_id = cls_id.strip("'")
                objId = f"{clname} {cls_id}"
                HBNBCommand.do_show(self, objId)
            elif command == "destroy":
                cls_id = args[1].strip(')"')
                cls_id = cls_id.strip("'")
                objId = f"{clname} {cls_id}"
                HBNBCommand.do_destroy(self, objId)
            elif command == "update":
                entries = args[1].split(", ")
                clsId = entries[0].strip('"\'')
                attrName = entries[1].strip("'\"")
                attrVal = entries[2].strip("')")
                inputs = clname + " " + clsId + " " + attrName + " " + attrVal
                HBNBCommand.do_update(self, inputs)
            else:
                print(f"*** Unknown syntax: {clname}")
        except IndexError:
            print(f"*** Unknown syntax: {clname}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
