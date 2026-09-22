import random
from datetime import datetime

users = ["sid", "alex", "rahul", "john", "admin"]
ips = [
    "192.168.1.10",
    "192.168.1.15",
    "10.0.0.24",
    "172.16.0.8",
    "45.67.23.91"
]

print("=" * 55)
print("             CYBER LOG ANALYZER")
print("=" * 55)

logs = []

for i in range(25):

    user = random.choice(users)
    ip = random.choice(ips)

    if random.randint(1, 10) <= 3:
        status = "FAILED"
    else:
        status = "SUCCESS"

    time = datetime.now().strftime("%H:%M:%S")

    logs.append({
        "user": user,
        "ip": ip,
        "status": status,
        "time": time
    })

print("\nGENERATED LOGIN LOGS")
print("-" * 55)

for log in logs:
    print(
        f"[{log['time']}] "
        f"USER: {log['user']:<6} "
        f"IP: {log['ip']:<15} "
        f"STATUS: {log['status']}"
    )

# Count failed attempts
failed_users = {}

for log in logs:

    if log["status"] == "FAILED":

        user = log["user"]

        if user not in failed_users:
            failed_users[user] = 0

        failed_users[user] += 1

print("\n" + "=" * 55)
print("             SECURITY ANALYSIS")
print("=" * 55)

print("\nFailed Login Attempts:")

for user, attempts in failed_users.items():
    print(f"{user}: {attempts}")

print("\nSuspicious Users:")

found = False

for user, attempts in failed_users.items():

    if attempts >= 3:
        print(f"[WARNING] {user} has {attempts} failed attempts!")
        found = True

if not found:
    print("No suspicious users detected.")

print("\n" + "=" * 55)
print("             ANALYSIS COMPLETE")
print("=" * 55)
