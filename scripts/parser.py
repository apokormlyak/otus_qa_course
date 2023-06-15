from functools import reduce
from subprocess import PIPE, Popen


def parser():
    with open('parsed_data.txt', 'w') as f:
        user_list = Popen(
            ['ps aux | tr -s " " | cut -d " " -f1'], shell=True, stdout=PIPE)
        user_list = set(user_list.stdout.read().decode('ascii').split())

        pid_list = Popen(
            ['ps aux | tr -s " " | cut -d " " -f2'], shell=True, stdout=PIPE)
        pid_list = set(pid_list.stdout.read().decode('ascii').split())

        cpu_list = Popen(
            ['ps aux | tr -s " " | cut -d " " -f3'], shell=True, stdout=PIPE)
        cpu_list = list(cpu_list.stdout.read().decode('ascii').split())
        cpu_list2 = [float(x) for x in cpu_list[1:]]
        sum_cpu = reduce((lambda x, y: x + y), cpu_list2)

        mem_list = Popen(
            ['ps aux | tr -s " " | cut -d " " -f4'], shell=True, stdout=PIPE)
        mem_list = list(mem_list.stdout.read().decode('ascii').split())
        mem_list2 = [float(x) for x in mem_list[1:]]
        mem_sum = reduce((lambda x, y: x + y), mem_list2)

        process_mem_list = Popen(
            ['ps aux --sort=-%mem | tr -s " " | cut -d " " -f11'], shell=True, stdout=PIPE)
        process_mem_list = list(process_mem_list.stdout.read().decode('ascii').split())[1:]
        process_mem = process_mem_list[0]

        process_cpu_list = Popen(
            ['ps aux --sort=-%cpu | tr -s " " | cut -d " " -f11'], shell=True, stdout=PIPE)
        process_cpu_list = list(process_cpu_list.stdout.read().decode('ascii').split())[1:]
        process_cpu = process_cpu_list[0]

        f.write("Отчёт о состоянии системы: \n")
        f.write(f'Пользователи системы: {", ".join(user_list)}\n')
        f.write(f'Процессов запущено: : {len(pid_list)}\n')
        f.write(f'Процессов  CPU используется: {sum_cpu} %\n')
        f.write(f'Всего памяти используется: {mem_sum} mb\n')
        f.write(f'Больше всего памяти использует: {process_mem}\n')
        f.write(f'Больше всего CPU использует: {process_cpu}\n')


if __name__ == '__main__':
    parser()
