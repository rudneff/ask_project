proc_name = "ask_app"
bind = ['127.0.0.1:8082']
workers = 2
#The maximum number of pending connections.
backlog = 2048
threads = 2
timeout = 30
gracefu_timeout = 10
keepalive = 10
#max_requests = 500
#logs
accesslog = "/home/rudi/projects/ask_project/ask_rudnev/logs/ask_app_access.log"
errorlog = "/home/rudi/projects/ask_project/ask_rudnev/logs/ask_app_error.log"
loglevel = "warning"

