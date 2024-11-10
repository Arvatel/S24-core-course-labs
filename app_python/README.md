# Lab 1: Moscow time show

## Made by
Anastasiia Kuklina

## Installation
In order to run the project 'python' (v3 or higher), 'pip' are required 

### Run
1. Create virtual environment
```bash
python3 -m venv env
```

2. Activate virtual env
```bash
source env/bin/activate
```

3. Install nesessary modules
```bash
pip install -r requirements.txt
```

4. Run application
```bash
flask run
```

5. Open your web browser and go to `http://127.0.0.1:5000/` to view the Moscow time

## Project Structure

* `app_python/`: Main application folder
  * `app.py`: Flask application
  * `templates/`: HTML templates
  * `requirements.txt`: Python app requirements


## Docker

### Build the Docker Image

```bash
docker build -t lab2 .
```

### Pull the Docker Image

```bash
docker pull letavra/lab2:v1
```

### Run the Docker Image

```bash
docker run -p 5000:5000 letavra/lab2:v1
```


## Unit tests
Unit tests have been added to the project. 

Tests include testing of:
* Getting time
* Time formating
* Workflow

Tests use the unittest library