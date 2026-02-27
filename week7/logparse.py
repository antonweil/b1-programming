import re
from datetime import datetime

def reformat_to_web_style(input_file):
    # Regex for your specific log format
    # Group 1: Timestamp | Group 2: Level | Group 3: Message
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),\d{3} - (WARNING|ERROR) - (.*)')
    
    # Regex to pull an IP if it exists in the message (for the Warning logs)
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    with open(input_file, 'r') as infile, \
         open('errors.txt', 'w') as err_file, \
         open('warnings.txt', 'w') as warn_file:
        
        for line in infile:
            match = log_pattern.match(line)
            if not match:
                continue
                
            raw_ts, level, message = match.groups()
            
            # 1. Convert Timestamp: 2025-11-20 12:01:06 -> 20/Nov/2025:12:01:06 -0000
            dt = datetime.strptime(raw_ts, '%Y-%m-%d %H:%M:%S')
            formatted_ts = dt.strftime('%d/%b/%Y:%H:%M:%S -0000')
            
            # 2. Extract IP or use placeholder
            ip_match = ip_pattern.search(message)
            ip = ip_match.group(1) if ip_match else "127.0.0.1"
            
            # 3. Create the NCSA String
            # Format: IP - - [Time] "LEVEL Message" STATUS BYTES "REFERER" "USER_AGENT"
            status = "403" if level == "WARNING" else "500"
            web_style_log = f'{ip} - - [{formatted_ts}] "{level} {message} HTTP/1.1" {status} 0 "-" "Python-Logger/1.0"'
            
            # 4. Save to respective files
            if level == 'ERROR':
                err_file.write(web_style_log + '\n')
            else:
                warn_file.write(web_style_log + '\n')

reformat_to_web_style('logs.txt')