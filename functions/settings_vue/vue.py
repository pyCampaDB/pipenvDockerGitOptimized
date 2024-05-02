from subprocess import CalledProcessError, run as runSubprocess;from os import getcwd; from os.path import join as osJoin
def vue_install():
    try:runSubprocess('npm install vue', shell=True, check=True)
    except CalledProcessError as cp: print(f'An error occurred: {cp.stderr}')
def vue_init():
    try:runSubprocess('npm init vue@latest', shell=True, check=True)
    except CalledProcessError as cp: print(f'An error occurred: {cp.stderr}')
def npm_install(project):
    try:runSubprocess(f'cd {project} && npm install', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def run_format(project):
    try:runSubprocess(f'cd {project} && npm run format', shell=True, check=True)
    except CalledProcessError as cp: print(f'An error occurred: {cp.stderr}')
def run_dev(project):
    try:runSubprocess(f'cd {project} && npm run dev',shell=True, check=True)
    except CalledProcessError as cp: print(f'An error occurred: {cp.stderr}')
def manage_vue():
    print('\n\n*************************** SETTINGS VUE ***************************************');options=['1','2','3','4'];option='1'
    while option in options:
        option=input('\n1. npm install vue\n2. npm init vue@latest\n3. npm install\n4. npm run format\n5. npm run dev\n\nInput a choice: ')
        if option == '1': vue_install()
        elif option == '2': vue_init()
        elif option in ['3', '4','5']:
            project=input('Input the project name: '); project=osJoin(getcwd(), project)
            if option == '3': npm_install(project)
            elif option == '4': run_format(project)
            elif option == '5': run_dev()
        elif option not in options: print('************************************ END SETTINGS VUE *****************************************')