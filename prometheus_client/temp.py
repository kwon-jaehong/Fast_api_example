from prometheus_client import start_http_server, Summary
import random
import time

# https://velog.io/@seokbin/%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81-%EC%8B%9C%EC%8A%A4%ED%85%9C-%EA%B5%AC%EC%B6%952-Custom-Exporter-%EA%B0%9C%EB%B0%9C

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(32210)
    # Generate some requests.
    while True:
        process_request(random.random())
        
# curl "http://localhost:32210"