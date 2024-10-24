from collections import defaultdict
import sys


def load_logs(path):
    try:
        with open(path, 'r') as file:
            return [parse_log_line(line) for line in file.readlines()]
    except FileNotFoundError:
        print(f'File {path} not found.')
        return []
    

def parse_log_line(line):
    parts = line.split(' ', 3)
    if len(parts) < 4:
        return {'date': '', 'time': '', 'level': '', 'message': 'Invalid log format'}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3],
    }


def filter_logs_by_level(logs, level):
    level = level[0].upper()
    filtered_logs = []
    for log in logs:
        if level in log['level']:
            filtered_logs.append(f"{log['date']} {log['time']} - {log['message']}")

    return filtered_logs

    
def count_logs_by_level(logs):
    log_counts = defaultdict(int)

    for log in logs:
        log_counts[log['level']] += 1

    return log_counts


def display_log_counts(log_counts, level, filtered_logs=None):

    print(f"{'\nРівень логування':<17} | {'Кількість':<8}")
    print('-' * 18 + "|" + '-' * 9)

    for lvl, count in log_counts.items():
        print(f"{lvl:<17} | {count:<8}")
    
    if filtered_logs:
        print(f"\nДеталі логів для рівня '{level[0].upper()}':\n\n{filtered_logs}")
    

def main():
    if len(sys.argv) < 2:
        print("Необхідно вказати шлях до файлу логу.")
        return

    path = sys.argv[1]
    level = sys.argv[2:]

    logs = load_logs(path=path)

    if logs:
        log_counts = count_logs_by_level(logs)
        if level:
            filtered_logs = filter_logs_by_level(logs, level)
            if filtered_logs:
                display_log_counts(log_counts, level, filtered_logs = '\n'.join(filtered_logs))
            else:
                print(f"Немає логів рівня {level[0].upper()}")
        else:
            display_log_counts(log_counts, level)
        


    
if __name__ == '__main__':
    main()