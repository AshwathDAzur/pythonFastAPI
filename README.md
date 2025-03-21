# pythonFastAPI
A codebase with the python FastAPI 

## Setting up the venv and activate it
`python -m venv venv`
`venv\Scripts\Activate`

## Installing the fast API 
`pip install "fastapi[standard]"`

## To freeze the package and to maintain version control
`pip freeze > requirements.txt`

## To run the application
`fastapi dev main.py` - to run in develop mode
`fastapi run main.py` - to run in proiduction mode
The application will run in port 8080 and we can see the api documentation in the swagger api doc
