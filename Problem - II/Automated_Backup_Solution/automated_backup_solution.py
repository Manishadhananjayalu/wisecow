import os
import subprocess
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='backup_report.log', level=logging.INFO)

def log_message(message):
    logging.info(f"{datetime.now()}: {message}")

def backup_directory(local_dir, remote_user, remote_host, remote_dir):
    try:
        # Create a compressed archive of the local directory
        archive_name = f"{local_dir.strip('/').replace('/', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.tar.gz"
        subprocess.check_call(['tar', 'czf', archive_name, local_dir])
        
        # Transfer the archive to the remote server
        scp_command = ['scp', archive_name, f"{remote_user}@{remote_host}:{remote_dir}"]
        subprocess.check_call(scp_command)

        # Remove the local archive after successful transfer
        os.remove(archive_name)

        log_message(f"Backup of {local_dir} to {remote_host}:{remote_dir} succeeded.")
    except subprocess.CalledProcessError as e:
        log_message(f"Backup of {local_dir} to {remote_host}:{remote_dir} failed. Error: {e}")
    except Exception as e:
        log_message(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Configuration
    LOCAL_DIR = '/path/to/local/directory'
    REMOTE_USER = 'username'
    REMOTE_HOST = 'remote.server.com'
    REMOTE_DIR = '/path/to/remote/directory'

    backup_directory(LOCAL_DIR, REMOTE_USER, REMOTE_HOST, REMOTE_DIR)
