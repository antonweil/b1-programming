import re
from datetime import datetime
import os

def reformat_to_web_style(input_file):
    if not os.path.exists(input_file):
        print(f"Critial Error: The file '{input_file}' does not exist. Is this the right directory?")
        return
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3} - (WARNING|ERROR) - (.*)')
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    try:
        with open(input_file, 'r') as infile, \
             open('errors.txt', 'w') as err_file, \
             open('warnings.txt', 'w') as warn_file, \
             open('corrupt_lines.log', 'w') as junk_file:
            for line_num, line in enumerate(infile, 1):
                line = line.strip()
                if not line: 
                    continue
                match = log_pattern.match(line)
                if not match:
                    junk_file.write(f"Line {line_num} (MALFORMED): {line}\n")
                    continue 
                raw_ts, level, message = match.groups()
                try:
                    dt = datetime.strptime(raw_ts, '%Y-%m-%d %H:%M:%S')
                    formatted_ts = dt.strftime('%d/%b/%Y:%H:%M:%S -0000')
                except ValueError:
                    formatted_ts = datetime.now().strftime('%d/%b/%Y:%H:%M:%S -0000')
                ip_match = ip_pattern.search(message)
                ip = ip_match.group(1) if ip_match else "127.0.0.1"
                status = "403" if level == "WARNING" else "500"
                web_style_log = f'{ip} - - [{formatted_ts}] "{level} {message} HTTP/1.1" {status} 0 "-" "Python-Logger/1.0"'
                if level == 'ERROR':
                    err_file.write(web_style_log + '\n')
                else:
                    warn_file.write(web_style_log + '\n')
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

reformat_to_web_style('logs.txt')