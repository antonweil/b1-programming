devices = [ ("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23,
80, 3389])]
risky_ports = [21, 23, 3389]

risky_port_number = 0

for ip, ports in devices:
    for open in ports:
        for risky_port in risky_ports:
            if open == risky_port:
                risky_port_number += 1
                print(f"risky port found: {open} in {ip}")

print(f"scan complete: {risky_port_number} risky ports found")