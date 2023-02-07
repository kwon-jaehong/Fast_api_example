from prometheus_client import start_http_server, Summary
import random
import time
import sys
import json
import os
# Create a metric to track time spent and requests made.
line = sys.stdin.readline()


monitor_data = json.loads(line)
print(type(monitor_data),monitor_data)
# curl "http://localhost:32210"

# neuron-monitor | python monitorparsing.py