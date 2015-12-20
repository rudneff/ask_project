proc_name = "simple_wsgi_test_app"
bind = ['127.0.0.1:8081']
workers = 2
#The maximum number of pending connections.
backlog = 2048
threads = 2
timeout = 30
gracefu_timeout = 10
keepalive = 10
#max_requests = 1000
#logs
accesslog = "/home/rudi/projects/ask_project/ask_rudnev/logs/test_app_access.log"
errorlog = "/home/rudi/projects/ask_project/ask_rudnev/logs/test_app_error.log"
loglevel = "warning"

