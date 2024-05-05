from datetime import datetime

date = datetime.now()
print('Hello from base.py')

the_app = f"Starting -> {__name__}"
print(the_app)


def modify_the_app(modifier):
    global the_app
    the_app += modifier
    print(the_app)
