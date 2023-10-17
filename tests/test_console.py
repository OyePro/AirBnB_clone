#!/usr/bin/python3
"""
Unittest for console command interpreter
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
from console import HBNBCommand
import tests
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):

    """Unittest for command interpreter
    Run with python3 -m unittest -v tests/test_console.py
    """

    @classmethod
    def setUpClass(self):
        """Set up test"""
        self.console = HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    """Check for docstring existance"""
    def test_if_doc(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(HBNBCommand().__doc__) >= 1)

    def test_doc_in_test(self):
        """Test docstrings exist in test_console.py"""
        self.assertTrue(len(self.__doc__) >= 1)

    """Testing the command interpreter outputs"""
    def test_prompt(self):
        """Test prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """Test no user input"""
        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("\n")
            self.assertEqual(f_out.getvalue(), '')

    def test_create(self):
        """Test the command output: create"""
        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("User.all()")
            self.assertEqual('["[User]', f_out.getvalue()[:8])

    def test_all(self):
        """Test the command output: all"""
        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("all NonExistantModel")
            self.assertEqual("** class doesn't exist **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("all Place")
            self.assertEqual('["[Place]', f_out.getvalue()[:9])

    def test_destroy(self):
        """Test the command output: destroy"""
        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("City.destroy('123')")
            self.assertEqual("** no instance found **\n", f_out.getvalue())

    def test_update(self):
        """Test the command output: update"""
        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("update You")
            self.assertEqual("** class doesn't exist **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("update User")
            self.assertEqual("** instance id missing **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("User.update(12345, name, 'Betty')")
            self.assertEqual("** no instance found **\n", f_out.getvalue())

    def test_show(self):
        """Test the command output: show"""
        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("SomeClass.show()")
            self.assertEqual("** class doesn't exist **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("show Review")
            self.assertEqual("** instance id missing **\n", f_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("User.show('123')")
            self.assertEqual("** no instance found **\n", f_out.getvalue())

    def test_count(self):
        """Test the command output: count"""
        with patch('sys.stdout', new=StringIO()) as f_out:
            self.console.onecmd("User.count()")
            self.assertEqual(int, type(eval(f_out.getvalue())))


if __name__ == "__main__":
    unittest.main()
