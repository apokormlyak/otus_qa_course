import argparse
import re
import json
from collections import defaultdict

parser = argparse.ArgumentParser(description='Log file')
parser.add_argument('-f', dest='file', action='store', help='Path to lod file',
                    default='/home/alisapokormlyak/Desktop/'
                            'otus_automation/otus_qa_course/logs/'
                            'access.log')
args = parser.parse_args()


def log_parser():
    ip_data = defaultdict(
        lambda: {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "HEAD": 0}
    )
    request_data = defaultdict(str)
    top_longest_list = []
    total_requests = 0
    with open(args.file, 'r') as f:
        for line in f:
            ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
            if ip_match is not None:
                ip = ip_match.group()
                method = re.search(r"(POST|GET|PUT|DELETE|HEAD)", line)
                req_time = re.search(r"\d{3,4}$", line)
                req_date = re.search(r"(\[(.*)\])", line)
                url = re.search(r"(\ \"http:(.*)\" \")", line)
                if method is not None:
                    ip_data[ip][method.group()] += 1
                    request_data['ip'] = ip
                    request_data['method'] = method.group()
                    total_requests += 1
                if req_time is not None:
                    request_data['duration'] = req_time.group()
                else:
                    request_data['duration'] = '0'
                if req_date is not None:
                    request_data['date'] = req_date.group()
                if url is not None:
                    request_data['url'] = url.group().strip('\" ')
                else:
                    request_data['url'] = '-'
                top_longest_list.append(dict(request_data))

        total_stat = {
            'total_stat': get_total_stat(ip_data)
        }
        top_ips = {
            'top_ips': get_top_ips(ip_data)
        }
        total_requests = {
            'total_requests': total_requests
        }
        top_longest = {
            'top_longest': get_top_longest(top_longest_list)
        }
        data = [top_ips, top_longest, total_stat, total_requests]

        print("Результат анализа файла логов: \n")
        print(json.dumps(data, indent=4))


def get_total_stat(request_data: defaultdict) -> defaultdict:
    """
    Собирается информация по кол-ву каждого из выполненных запросов
    """
    total_stat_data = defaultdict(int)
    for el in request_data.values():
        for k2, v2 in el.items():
            total_stat_data[k2] += v2
    total_stat = total_stat_data
    return total_stat


def get_top_ips(request_data: defaultdict) -> dict:
    """
    Собирается информация по топ 3 IP адресов, с которых были сделаны запросы
    """
    top_ips = defaultdict(int)
    for k, v in request_data.items():
        request_count = 0
        for k2, v2 in v.items():
            request_count += v2
        top_ips[k] = request_count
    sorted_ips = sorted(top_ips.items(), key=lambda item: item[1], reverse=True)
    result_top_ips = sorted_ips[:3]
    result_top_ips = {k: v for k, v in result_top_ips}
    return result_top_ips


def get_top_longest(top_longest_list: list) -> list[dict]:
    """
    Собирается информация по топ 3 самых долгих запросов
    """
    sorted_top_longest_list = sorted(top_longest_list, key=lambda item: item['duration'], reverse=True)
    result_top_longest = sorted_top_longest_list[:3]
    return result_top_longest


if __name__ == '__main__':
    log_parser()
