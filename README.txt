Task has 3 components
-Title
-Description
-Deadline

Store task/user information in a json file
-list of dicts

Menu system using tkinter
authentication/user system


PROJECT CRITERIA
In this assignment, you will create a command line todo list application that allows users to add, remove, and list tasks. The application should store tasks in a text file, and should read from and write to the file whenever tasks are added, removed, or listed.

Tasks
A task contains three "elements":

the title of the task: for example "Take out the trash"
the description of the task: additional information about the task (optional). For example: "Don't forget to put a new bag in the trash bin". The task description can span several lines.
the deadline for the task (as a date)
File format
Your application should use a single text file to store and read the tasks. It is up to you to choose the format of the file.

Requirements
When started, the application displays a menu that allows the user to perform the following actions:

view all tasks (sorted by deadline ascending)
view pending tasks (= tasks with a deadline in the future), sorted by deadline ascending
create a new task
View tasks
When viewing tasks, the program should display a list of their titles. Each task has a "number" associated to it. It is up to you to make up this number as required.

From the task list, a user can:

select a task and view it
select a task and delete it
go back to the previous screen
It is up to you to decide on the menu system to make the features work.

View a single task
When viewing a single task, you should display the task title, description and deadline on the screen. Make sure the user can go back to the previous screen or to the main menu.

Create a task
When creating a task, the user is prompted for the task title. It cannot be empty!
The deadline is also mandatory - make sure that the user provided a valid date.
The task description is optional (can be empty). To support multiple line input, you can either use input() in a loop, or use "sys.stdin.read()". This function returns a string. It will stop reading from user input once the "EOF" character is generated - you can generate it with Control-Z on Windows, or Control-D on Mac / Linux.

Persistence in the file
Whenever changes are made to a task, they should be immediately reflected in the file. The application should read from the file whenever it needs to access todo data (no local persistence / caching).

Code quality and hints
You should divide your code into separate, independent logic units - and implement them in functions. Make sure that your functions are concise (20-25 lines long maximum). You should write generic functions that can handle many situations.

Your code should also be split into separate modules, and use import statements.

You must follow the software development best practices - write comments, docstrings as necessary, and follow the PEP8 recommendations.

Your program must be safe and not crash regardless of user input (you must handle all exceptions and error validation).

This assignment is very open ended - on purpose. Use your best judgement in deciding how to structure your code. The most important is to have a stable application with no bugs or crashes - your first priority should be implementation rather than features.