import socket
import threading
import time
import os
from datetime import datetime


# ==========================================
# PYTHON NETWORK MONITOR
# ==========================================

print("=" * 55)
print("             PYTHON NETWORK MONITOR")
print("=" * 55)

target = input("Enter website/IP to scan: ")

print("\nStarting scanner...")
print("Target:", target)
print()


# ==========================================
# GET IP ADDRESS
# ==========================================

try:
    ip = socket.gethostbyname(target)

    print("IP Address:", ip)

except:

    print("Could not find the target.")

    exit()


# ==========================================
# PORT SCANNER
# ==========================================

open_ports = []

lock = threading.Lock()


def scan_port(port):

    s = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    s.settimeout(0.5)

    result = s.connect_ex(
        (ip, port)
    )

    if result == 0:

        with lock:

            open_ports.append(port)

            print(
                "[OPEN] Port:",
                port
            )

    s.close()


# ==========================================
# SCAN PORTS
# ==========================================

start_time = time.time()

threads = []


for port in range(1, 1025):

    thread = threading.Thread(
        target=scan_port,
        args=(port,)
    )

    thread.start()

    threads.append(thread)


# ==========================================
# WAIT FOR THREADS
# ==========================================

for thread in threads:

    thread.join()


# ==========================================
# RESULTS
# ==========================================

end_time = time.time()

print()
print("=" * 55)
print("                 SCAN COMPLETE")
print("=" * 55)

print(
    "Target:",
    target
)

print(
    "IP:",
    ip
)

print(
    "Open ports:",
    len(open_ports)
)

print(
    "Time:",
    round(
        end_time - start_time,
        2
    ),
    "seconds"
)

print()


# ==========================================
# SAVE REPORT
# ==========================================

filename = "scan_report.txt"

with open(filename, "w") as file:

    file.write(
        "PYTHON NETWORK SCAN REPORT\n"
    )

    file.write(
        "=" * 40 + "\n"
    )

    file.write(
        "Date: "
        + datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
        + "\n"
    )

    file.write(
        "Target: "
        + target
        + "\n"
    )

    file.write(
        "IP: "
        + ip
        + "\n\n"
    )

    file.write(
        "Open Ports:\n"
    )

    for port in sorted(open_ports):

        file.write(
            str(port)
            + "\n"
        )


print(
    "Report saved as:",
    filename
)

print()
print("Program finished.")
