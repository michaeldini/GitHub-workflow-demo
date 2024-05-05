from import_design import main
from import_design.main import the_app

print('Hello from app.py')

the_app += f' -> {__name__}'
print(the_app)
