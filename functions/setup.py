from signal import signal, SIGINT;from functions.cmd_and_run.script import  run_script, manage_cmd, optimizer_html_css;from functions.settings_pipenv.settings_pipenv import manage_pipenv, ensure_pipenv_installed, manage_and_use_env;from functions.dockercompose.dockercompose import manage_compose;from functions.git.git import manage_git;from functions.settings_docker.settings_docker import manage_docker;from functions.settings_vue.vue import manage_vue
def signal_handler(sign, frame):print('Ctrl+C pressed')
def run():
    signal(SIGINT, signal_handler);ensure_pipenv_installed();manage_and_use_env();option = '1'
    while option in ['1', '2', '3', '4', '5', '6', '7', '8']:
        option = input( '\n*********************************** SETUP ***********************************\n\n\n1. CMD\n2. Run Script\n3. Settings pipenv\n4. Docker\n5. Docker Compose\n6. GIT\n7. Optimizer the file of your app\n8. Settings vue\n(Other). Exit\n\nEnter your choice: ')
        if option == '1':manage_cmd()
        elif option == '2':run_script()
        elif option == '3': manage_pipenv()
        elif option in ['4', '5', '6']:from dotenv import load_dotenv;load_dotenv()
        elif option == '7': optimizer_html_css()
        elif option == '8': manage_vue()
        if option == '4': manage_docker()         
        elif option == '5': manage_compose()
        elif option == '6': manage_git()
    print('\n*********************************** EXIT SETUP ***********************************\n\n')