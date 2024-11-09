# Lab 1


### Framework: Flask
#### Justification:

* Simplicity: Flask is minimalistic and easy to set up, which makes it great for small applications.
* Flexibility: It provides the essentials, allowing for easy scaling and integration of other libraries as needed.
* Community and Documentation: Flask has strong community support and excellent documentation, making it easier to find solutions and get help.

### Best practices

* Use proper naming conventions for variables and functions
* Organize your code using functions to improve readability
* Write a description of the project and installation process in the README file
* Use virtual environment for isolated development
* Use .gitignore to avoid uploading unnecessary files that can be retrieved from
* Include a requirements.txt file for dependencies

## Unit tests
Unit tests have been added to the project. 

Tests include testing of:
* Getting time
* Time formating
* Workflow

Tests use the unittest library

## Best practices implemented
* Flask HTML templating - allows dynamic content rendering and helps separate frontend and backend
* Separation of the main sections of the app - backend logic in the 'main.py', while templates used for frontend in the separate folder