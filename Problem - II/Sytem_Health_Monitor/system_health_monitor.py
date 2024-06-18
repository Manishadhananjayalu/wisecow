import psutil
import logging
from datetime import datetime

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Setup logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

def log_message(message):
    logging.info(f"{datetime.now()}: {message}")

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_message(f"High Memory usage detected: {memory_usage}%")

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        log_message(f"High Disk usage detected: {disk_usage}%")

def log_running_processes():
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]
    log_message(f"Running processes: {processes}")

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    log_running_processes()

if __name__ == "__main__":
    main()
