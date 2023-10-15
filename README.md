# AirBnB_clone
![HBnB Logo](./image/hbnb_img.png)


### Contents

- [Description](#Description)
- [Environment](#Environment)
- [Further Information](#Furtherinformation)
- [Requirements](#Requirements)
- [Repository Contents](#FileContents)
- [Installation](#Installation)
- [Usage](#Usage)
- [Built with](#Built-with)

## Description 📃

AirBnB Clone Project; The goal of the project is to deploy a simple copy of the AirBnB website on my server. It's one of the project done while learning Software Engineering at Alx School. This repository consists of one of the four projects that will be done to clone the AirBnB website. In this phase, a basic `console` was created using the Python module, Cmd, to manage the objects of the whole project through implementation of the methods `create`, `show`, `update`, `all`, and `destroy` to the existing classes and subclasses.

## Environment 💻

The console was developed in Ubuntu 20.04LTS using python3 (version 3.8.5).

## Further Information 📑

For further information on python version, and documentation visit [python.org](https://www.python.org/).

## Requirements 📝

- Basic knowledge in python3 and usage of a command line interpreter.
- A computer with Ubuntu 20.04LTS, may be Subsystem for Linux.
- Code must follow the Python Coding Style, pycodestyle (2.8 version)
- All modules, classes and function must have a documentation.

## Repository Contents 📋

This repository contains the following files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about the doer of the project |
|[base_model.py](./models/base_model.py) | Defines class BaseModel (parent class), and its methods |
|[user.py](./models/user.py) | Defines subclass User |
|[state.py](./models/state.py) | Defines subclass State |
|[city.py](./models/city.py)| Defines subclass City |
|[place.py](./models/place.py)| Defines subclass Place |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[review.py](./models/review.py) | Defines subclass Review |
|[file_storage.py](./models/engine/file_storage.py) | Creates new instance of class, saves, reloads, serializes and deserializes data |
|[console.py](./console.py) | creates object, retrieves object from file, list instances of objects, updates attributes of object and destroys object |
|[test_base_model.py](./tests/test_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/test_models/test_user.py) | unittests for user |
|[test_amenity.py](./tests/test_models/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_models/test_city.py) | unittests for city |
|[test_place.py](./tests/test_models/test_place.py) | unittests for place |
|[test_review.py](./tests/test_models/test_review.py) | unittests for review |
|[test_state.py](./tests/test_models/test_state.py) | unittests for state |
|[test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |


## Installation 🛠️

Clone the repository and run the console.py
```
$ git clone https://github.com/OyePro/AirBnB_clone.git
```

## Usage 🔧

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of given class and display the id |
|[show](./console.py) | Prints the string representation of an instance based on the class name and id |
|[all](./console.py) | Prints all string representation of all instances based or not on the class name |
|[update](./console.py) | Updates an instance based on the class name and id by adding or updating attribute and the changes will be saved to the JSON file) |
|[destroy](./console.py)| Deletes an instance based on the class name and id and the changes will be to the JSON file) |
|[count](./console.py)| Retrieve the number of instances of a class |
|[help](./console.py)| Prints information about specific command |
|[quit/ EOF](./console.py)| Exit the program

###### Console Execution

```
OyePro@proboscis:~AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
(hbnb)
(hbnb) quit
OyePro@proboscis:~AirBnB_clone$

```


###### Testing 1

```
OyePro@proboscis:~AirBnB_clone$ ./console.py
(hbnb) create User
bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) show User bb4f4b81-7757-460b-9263-743c9ea6fef6
[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) update User bb4f4b81-7757-460b-9263-743c9ea6fef6 name Betty
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name': 'Betty', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) destroy User bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb)

```

###### Testing 2

```
OyePro@proboscis:~AirBnB_clone$ ./console.py
(hbnb) User.count
*** Unknown syntax: User.count
(hbnb) User.count()
1
(hbnb) User.all()
["[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc613f1b4', 'updated_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), 'created_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}"]
(hbnb) User.show()
** instance id missing **
(hbnb) User.show(e6ee5344-04ef-454d-84e4-ba6fc613f1b4)
[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc613f1b4', 'updated_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), 'created_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}
(hbnb) User.update("e6ee5344-04ef-454d-84e4-ba6fc613f1b4", "name", "Betty")
(hbnb) User.all()
['[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {\'"name"\': \'"Betty"\', \'id\': \'e6ee5344-04ef-454d-84e4-ba6fc613f1b4\', \'updated_at\': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), \'created_at\': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}']
(hbnb) User.destroy(e6ee5344-04ef-454d-84e4-ba6fc613f1b4)
(hbnb) User.all()
[]
(hbnb) quit
OyePro@proboscis:~AirBnB_clone$

```

## Built with ⚙️

python3 (3.8.5)

### Authors 🖋️

* Olalekan Okewale - @OyePro
