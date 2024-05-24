from subprocess import run as runSubprocess, CalledProcessError;from functions.settings_pipenv.settings_pipenv import check_package_installed
def startproject():
    option = input('Enter your project name: ')
    try:runSubprocess(f'pipenv run django-admin startproject {option} .',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def startapp():
    option = input('Enter your app name: ')
    try:runSubprocess(f'pipenv run python manage.py startapp {option}', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def runserver():
    try:runSubprocess(f'pipenv run python manage.py runserver',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def migrate():
    try:runSubprocess(f'pipenv run python manage.py migrate',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def migrateapp():
    name = input('Enter your app name: ')
    try:runSubprocess(f'pipenv run python manage.py migrate {name}',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def makemigrations(): 
    try:runSubprocess(f'pipenv run python manage.py makemigrations',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def makemigrationsapp():
    option = input('Enter your app name: ')
    try:runSubprocess(f'pipenv run python manage.py makemigrations {option}',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def reversemigrateproject():
    option = input('Enter your project name: ')
    try:runSubprocess(f'pipenv run python manage.py migrate {option} zero',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def reversemigrateapp():
    option = input('Enter your app name: ')
    try:runSubprocess(f'pipenv run python manage.py migrate {option} zero',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def show_migrations():
    try:runSubprocess(f'pipenv run python manage.py showmigrations',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def showmigrationsapp():
    option = input('Enter your app name: ')
    try:runSubprocess(f'pipenv run python manage.py showmigrations {option}',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def create_superuser():
    try:runSubprocess(f'pipenv run python manage.py createsuperuser',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def djangohelp():
    try:runSubprocess(f'pipenv run python manage.py help',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def sqlmigrate():
    try:appname = input('Enter your app name: ');mn = input('Enter the migration number: ');runSubprocess(f'pipenv run python manage.py sqlmigrate {appname} {mn}',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def djangoflush():
    try:runSubprocess(f'pipenv run python manage.py flush',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def collect_static_files():
    try:runSubprocess(f'pipenv run python manage.py collectstatic',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def find_static_file():
    try:runSubprocess(f'pipenv run python manage.py findstatic staticfile',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def clearsessions():
    try:runSubprocess(f'pipenv run python manage.py clearsessions',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def check_errors():
    try:runSubprocess(f'pipenv run python manage.py check',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def changepassword():
    try:runSubprocess(f'pipenv run python manage.py changepassword',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def compilemessages():
    try:runSubprocess(f'pipenv run python manage.py compilemessages',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def makemessages():
    try:runSubprocess(f'pipenv run python manage.py makemessages',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def pythonshell():
    try:runSubprocess(f'pipenv run python manage.py shell',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def dbshell():
    try:runSubprocess(f'pipenv run python manage.py dbshell',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def inspectdb():
    try:runSubprocess(f'pipenv run python manage.py inspectdb',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def load_fixture():
    name = input('Enter your fixture name: ')
    try:runSubprocess(f'pipenv run python manage.py loaddata {name}',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def testapp():
    name = input('Enter your app name: ')
    try:runSubprocess(f'pipenv run python manage.py test {name}',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def dumpapp():
    name = input('Enter your app name: ')
    try:runSubprocess(f'pipenv run python manage.py dumpdata {name}',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def manage_django(check=True):
    if not check:
        if not check_package_installed('Django'):
            try:runSubprocess('pipenv install Django')
            except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}') 
    option = '1'
    while option in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']:
        option = input('\n************************** DJANGO SETTINGS **************************\n\n1. Start project\n2. Start app\n3. Run server\n4. Migrate\n5. Migrate app\n6. Reverse migration project\n7. Reverse migration app\n8. Make migrations\n9. Make migrations app\n10. Show migrations\n11. Show app migrations\n12. Show the SQL app migration\n13. Create a superuser\n14. Collect static files\n15. Find the absolute path of a static file\n16. Compile messages\n17. Make messages\n18. Check errors\n19. Run app test\n20. Delete all data of DB\n21. Clear the table from expired sessions\n22. Inspect the DB\n23. Load data from a fixture\n24. Create a fixture data app\n25. Enter in the Python shell\n26. Enter in the DB shell\n27. Help\n28. Change your password\n(Other) Exit Django Settings\n\nEnter your choice: ')
        if option == '1': startproject()
        elif option == '2': startapp()
        elif option == '3': runserver()
        elif option == '4': migrate()
        elif option == '5': migrateapp()
        elif option == '6': reversemigrateproject()
        elif option == '7': reversemigrateapp()
        elif option == '8': makemigrations()
        elif option == '9': makemigrationsapp()
        elif option == '10': show_migrations()
        elif option == '11': showmigrationsapp()
        elif option == '12': sqlmigrate()
        elif option == '13': create_superuser()
        elif option == '14': collect_static_files()
        elif option == '15': find_static_file()
        elif option == '16': compilemessages()
        elif option == '17': makemessages()
        elif option == '18': check_errors()
        elif option == '19': testapp()
        elif option == '20': djangoflush()
        elif option == '21': clearsessions()
        elif option == '22': inspectdb()
        elif option == '23': load_fixture()
        elif option == '24': dumpapp()
        elif option == '25': pythonshell()
        elif option == '26': dbshell()
        elif option == '27': djangohelp()
        elif option == '28': changepassword()
    print('\n***************************************** EXIT DJANGO SETTINGS *****************************************\n')

