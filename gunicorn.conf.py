# gunicorn.conf.py
import multiprocessing

# Server socket - use a different socket name
bind = "unix:/run/gunicorn-impressions.sock"

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Restart workers after this many requests
max_requests = 1000
max_requests_jitter = 50

# Logging
loglevel = "info"
# accesslog = "/var/log/gunicorn-access.log"  # Update this path
# errorlog = "/var/log/gunicorn-error.log"    # Update this path
accesslog = "-"  # stdout
errorlog = "-"   # stderr

# Process naming
proc_name = "secondapp"

# Server mechanics
daemon = False
pidfile = None
user = None
group = None
tmp_upload_dir = None