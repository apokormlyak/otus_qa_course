from functools import reduce
from subprocess import PIPE, Popen


def collect_system_info(cmd):
    info = Popen([cmd], shell=True, stdout=PIPE)
    return list(info.stdout.read().decode('ascii').split())[1:]


def get_max(process_list, data_list):
    list_zipped = list(zip(process_list, data_list))
    list_zipped.sort(key=lambda x: x[1], reverse=True)
    return list_zipped[0][0]


def parser():
    user_list = set(collect_system_info('ps aux | tr -s " " | cut -d " " -f1'))
    pid_list = set(collect_system_info('ps aux | tr -s " " | cut -d " " -f2'))
    cpu_list = list(collect_system_info('ps aux | tr -s " " | cut -d " " -f3'))
    mem_list = list(collect_system_info('ps aux | tr -s " " | cut -d " " -f4'))
    process_list = list(collect_system_info('ps aux | tr -s " " | cut -d " " -f11'))

    cpu_list2 = [float(x) for x in cpu_list[1:]]
    sum_cpu = reduce((lambda x, y: x + y), cpu_list2)
    mem_list2 = [float(x) for x in mem_list[1:]]
    mem_sum = reduce((lambda x, y: x + y), mem_list2)

    process_mem = get_max(process_list, mem_list)
    process_cpu = get_max(process_list, cpu_list)

    with open('parsed_data.txt', 'w') as f:
        f.write("Отчёт о состоянии системы: \n")
        f.write(f'Пользователи системы: {", ".join(user_list)}\n')
        f.write(f'Процессов запущено: : {len(pid_list)}\n')
        f.write(f'Процессов  CPU используется: {sum_cpu} %\n')
        f.write(f'Всего памяти используется: {mem_sum} mb\n')
        f.write(f'Больше всего памяти использует: {process_mem}\n')
        f.write(f'Больше всего CPU использует: {process_cpu}\n')


if __name__ == '__main__':
    parser()
