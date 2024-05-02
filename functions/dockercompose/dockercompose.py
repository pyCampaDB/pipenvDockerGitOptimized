from subprocess import CalledProcessError, run as runSubprocess
def compose_up():
    try:runSubprocess(f'pipenv run docker-compose up',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def compose_down():
    try:runSubprocess('pipenv run docker-compose down',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def compose_build():
    try:runSubprocess('pipenv run docker-compose build',check=True,shell=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def compose_logs():
    try:runSubprocess('pipenv run docker-compose logs',shell=True,check=True)
    except CalledProcessError as cp:print (f'An error occurred: {cp.returncode}')
def compose_ps():
    try:runSubprocess('pipenv run docker-compose ps',shell=True,check=True)
    except CalledProcessError as cp:print (f'An error occurred: {cp.returncode}')
def compose_restart():
    try:
        services = []
        while True:
            out = input('Enter the amount of containers you want to restart: ')
            if out.isdigit():break
        for i in range(int(out)):s = input(f'{i} - Enter the name of the container: ');services.append(s)
        runSubprocess(f'pipenv run docker-compose restart {services}',shell=True,check=True)
    except CalledProcessError as cp:print (f'An error occurred: {cp.returncode}')
def compose_stop():
    try:runSubprocess('pipenv run docker-compose stop',shell=True,check=True)
    except CalledProcessError as cp:print (f'An error occurred: {cp.returncode}')
def compose_start():
    try:runSubprocess('pipenv run docker-compose start',shell=True,check=True)
    except CalledProcessError as cp:print (f'An error occurred: {cp.returncode}')
def compose_exec():
    service = input('Enter the name of the container: ')
    try:runSubprocess(f'pipenv run docker-compose exec {service} bash',check=True,shell=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def compose_pull():
    try:runSubprocess('pipenv run docker-compose pull',shell=True,check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
def manage_compose():
    print('\n******************************** DOCKER COMPOSE ********************************\n')
    opt = '1'
    while opt in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        opt = input('\n1. Up docker compose\n2. Down docker compose\n3. Build docker compose\n4. Show the logs of the docker compose\n5. Show the containers related with docker compose.yml\n6. Restart docker compose\n7. Stop docker compose\n8. Start docker compose\n9. Exec a command in the running container\n10. Download the images of the services defined in docker compose.yml\n(Other) Exit Docker Compose\n\nEnter your choice: ')
        if opt == '1': compose_up()
        elif opt == '2': compose_down()
        elif opt == '3': compose_build()
        elif opt == '4': compose_logs()
        elif opt == '5': compose_ps()
        elif opt == '6': compose_restart()
        elif opt == '7': compose_stop()
        elif opt == '8': compose_start()
        elif opt == '9': compose_exec()
        elif opt == '10': compose_pull()
        else:print('\n******************************** END DOCKER COMPOSE ********************************\n')
