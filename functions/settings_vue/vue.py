from subprocess import CalledProcessError, run as runSubprocess;from os import getcwd
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
def npm_vue_router(project):
    try:runSubprocess(f'cd {project} && npm install vue-router@4', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def npm_install_pinia(project):
    try:runSubprocess(f'cd {project} && npm install pinia', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def vue_cli():
    try:runSubprocess('npm install -g @vue/cli', shell=True, check=True)
    except CalledProcessError as cp: print(f'An error occurred: {cp.stderr}')
def vue_create(project):
    try:runSubprocess(f'vue create {project}', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def npm_run_serve(project):
    try:runSubprocess(f'cd {project} && npm run serve', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def npm_run_build(project):
    try:runSubprocess(f'cd {project} && npm run build', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred:{cp.stderr}')
def npm_run_lint(project):
    try:runSubprocess(f'cd {project} && npm run lint', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def npm_vue_cli_init():
    try:runSubprocess(f'npm i -g @vue/cli-init', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def vue_init_webpack(project):
    try:runSubprocess(f'vue init webpack {project}', shell=True, check=True)
    except CalledProcessError as cp: print(f'An error occurred: {cp.stderr}')
def npm_audit(project):
    mode=input('any mode? ')
    try:runSubprocess(f'cd {project} && npm audit {mode}', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def npm_audit_fix(project):
    try:runSubprocess(f'cd {project} && npm audit fix', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def npm_audit_fix_force(project):
    try:runSubprocess(f'cd {project} && npm audit fix --force', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def npm_fund(project):
    try:runSubprocess(f'cd {project} && npm fund', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def npm_install_webpack(project):
    try:runSubprocess(f'cd {project} && npm install -D webpack-cli', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def vue_add_babel(project):
    try:runSubprocess(f'cd {project} && vue add babel', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stderr}')
def vue_add_eslint(project):
    try:runSubprocess(f'cd {project} && vue add eslint', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stdout}')
def npm_install_eslint(project):
    try:runSubprocess(f'cd {project} && npm install eslint --save-dev',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stdout}')
def eslint_fix(project):
    try:runSubprocess(f'cd {project} && npx eslint --fix src/App.vue', shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.stdout}')
def manage_vue():
    print('\n\n*************************** SETTINGS VUE ***************************************');options=['1','2','3','4','5','6','7','8','9','10','11','12','13', '14','15','16','17','18','19','20','21','22','23'];option='1'
    while option in options:
        option=input('\n1. npm install vue\n2. npm init vue@latest\n3. npm install -g @vue/cli\n4. npm i -g @vue/cli-init\n5. npm install\n6. npm run format\n7. npm run dev\n8. npm install vue-router@4\n9. npm install pinia\n10. vue create project\n11. npm run serve\n12. npm run build\n13. npm run lint\n14. vue init webpack "project"\n15. npm audit\n16. npm audit fix\n17. npm audit fix --force\n18. npm fund\n19. npm install -D webpack-cli\n20. vue add babel\n21. vue add eslint\n22. npm install eslint --save-dev\n23. eslint --fix src/App.vue\n\nInput a choice: ')
        if option == '1': vue_install()
        elif option == '2': vue_init()
        elif option == '3': vue_cli()
        elif option == '4': npm_vue_cli_init()
        elif option in options[4:]:
            project=input('Input the project name: '); #project=osJoin(getcwd(), project)
            if option == '5': npm_install(project)
            elif option == '6': run_format(project)
            elif option == '7': run_dev(project)
            elif option == '8': npm_vue_router(project)
            elif option == '9': npm_install_pinia(project)
            elif option == '19': vue_create(project)
            elif option== '11': npm_run_serve(project)
            elif option== '12': npm_run_build(project)
            elif option == '13': npm_run_lint(project)
            elif option == '14': vue_init_webpack(project)
            elif option == '15': npm_audit(project)
            elif option == '16': npm_audit_fix(project)
            elif option == '17': npm_audit_fix_force(project)
            elif option == '18': npm_fund(project)
            elif option == '19': npm_install_webpack(project)
            elif option == '20': vue_add_babel(project)
            elif option == '21': vue_add_eslint(project)
            elif option == '22': npm_install_eslint(project)
            elif option == '23': eslint_fix(project)
        else: print('************************************ END SETTINGS VUE *****************************************')