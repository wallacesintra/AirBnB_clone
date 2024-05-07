#!/usr/bin/python3
"""
Test module for the console (command interpreter).
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Defines test cases for the HBNBCommand class (the console)."""

    def create(self, line):
        """Helper method to create an object using the console."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(line)
            return fake_out.getvalue().strip()

    def show(self, line):
        """Helper method to show an object using the console."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(line)
            return fake_out.getvalue().strip()

    def setUp(self):
        """Set up the tests."""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test quit command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("quit")
            self.assertEqual('', fake_out.getvalue().strip())

    def test_EOF(self):
        """Test EOF command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("EOF")
            self.assertEqual('', fake_out.getvalue().strip())

    def test_empty_line(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("")
            self.assertEqual('', fake_out.getvalue().strip())

    def test_create_missing_class(self):
        """Test create command with missing class."""
        result = self.create("create")
        self.assertEqual("** class name missing **", result)

    def test_create_invalid_class(self):
        """Test create command with invalid class."""
        result = self.create("create MyClass")
        self.assertEqual("** class doesn't exist **", result)

    def test_show_missing_class(self):
        """Test show command with missing class."""
        result = self.show("show")
        self.assertEqual("** class name missing **", result)

    def test_show_missing_id(self):
        """Test show command with missing id."""
        result = self.show("show BaseModel")
        self.assertEqual("** instance id missing **", result)

    def test_all(self):
        """Test all command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            self.assertIn('[]', fake_out.getvalue().strip())  # assuming no instances

    def test_update_missing_class(self):
        """Test update command with missing class."""
        result = self.create("update")
        self.assertEqual("** class name missing **", result)


if __name__ == "__main__":
    unittest.main()
