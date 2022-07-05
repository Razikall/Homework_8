import subprocess
from ProcessParser import ParserProcess
from datetime import datetime


def process_data():
    process = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE, encoding='utf-8').stdout.readlines()
    process_fields = len(process[0].split()) - 1
    result = []
    for row in process[1:]:
        result.append(row.split(None, process_fields))
    return result


pars = ParserProcess()
data = process_data()

process_count = pars.process_count(data)
users = pars.get_users(data)
user_process = pars.user_process_count(data)
cpu_and_memory = pars.calculate_memory_and_cpu(data)
highest_cpu_memory = pars.high_cpu_process(data)

report = [
    f"Пользователи системы: {users}\n",
    f"Процессов запущено: {process_count}\n",
    f"Пользовательских процессов: {dict(user_process)}\n",
    f"Всего памяти используется: {cpu_and_memory[0]}\n",
    f"Всего CPU используется: {cpu_and_memory[1]}\n",
    f"Больше всего памяти использует: {highest_cpu_memory[0]}\n",
    f"Больше всего CPU использует: {highest_cpu_memory[1]}\n"
]

with open(f"{datetime.today():%d-%m-%Y-%H-%M}-scan.txt", 'w') as parsfile:
    parsfile.writelines(report)
