# Welcome to the AirBnB clone project!

The Airbnb clone project for which we are creating a copy of the [Airbnb](https://www.airbnb.com/).


## Features

### Command Interpreter

#### Description

The Command Interpreter is used to manage the whole application's functionality from the command line, such as:
+ Create a new object.
+ Retrieve an object from a file.
+ Execute operation on objects. e.g. Count, compute statistics, etc.
+ Update the object's attributes.
+ Destroy an object.

#### Usage

The console application works in interactive mode:
 
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
or The non-interactive mode run:

```
 echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

```

#### Commands

Commands | Description | Usage
-------- | ----------- |-------- |
**help**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program.| N/A
**create**  | Creates a new instance of the \<class_name\>. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

## Bugs

+ No known bugs at this time.

## Contributors

#### [Moussaddak Meddeb](https://www.linkedin.com/in/moussaddak-meddeb-a64246b6/)