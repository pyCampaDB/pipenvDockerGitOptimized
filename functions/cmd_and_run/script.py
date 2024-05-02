from subprocess import  CalledProcessError, run as runSubprocess;from os import  getcwd
def run_script():
    try:runSubprocess(f'pipenv run python {input("Enter the file name: ")}.py',shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')  
def cmd():
    command = input(f'{getcwd()}: ')
    try:runSubprocess(command, shell=True, check=True)
    except CalledProcessError as cp:print(f'An error occurred: {cp.returncode}')
    finally:return command
def optimizer_html_css():
    filename = input('Input the file: ')
    with open(filename, 'r', encoding='utf-8') as fr:text = fr.read(); fr.close()
    if filename.endswith('.html') or filename.endswith('.css') or filename.endswith('.vue'):
        parts = filename.split('.');fw_final = f"{parts[0]}_optimized.{parts[1]}"
        if filename.endswith('.vue'):text = remove_comments(text, '//', '\n');optimized_text = text.replace('\n', ';')
        else:optimized_text = text.replace('\n', '');optimized_text = optimized_text.replace('  ', '')
        if filename.endswith('.html'):optimized_text = remove_comments(optimized_text, '<!--', '-->')
        if filename.endswith('.css'):optimized_text = remove_comments(optimized_text, '/*', '*/')
        with open(fw_final, 'w', encoding='utf-8') as fw:fw.write(optimized_text); fw.close();print('\nFile optimized!\n')
    else:print("Unsupported file type.")
def remove_comments(text, start_delim, end_delim):
    idx = 0
    while idx < len(text):
        start_idx = text.find(start_delim, idx)
        if start_idx == -1:break
        end_idx = text.find(end_delim, start_idx)
        if end_idx == -1:break
        text = text[:start_idx] + text[end_idx + len(end_delim):];idx = start_idx
    return text
def manage_cmd():
    print('\n*********************************** CMD ***********************************\n\n')
    try:
        while True:
            a = cmd()
            if a.lower() == 'exit':break                 
    except EOFError:pass
    finally:print('\n*********************************** EXIT CMD ***********************************\n\n')