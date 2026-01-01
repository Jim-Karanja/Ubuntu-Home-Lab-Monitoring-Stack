import requests
import time

# Configuration
PROMETHEUS_URL = "http://localhost:9090/api/v1/query"

# Queries for Prometheus
QUERIES = {
    "CPU Usage (%)": '100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[2m])) * 100)',
    "RAM Usage (%)": '(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100',
    "Disk Usage (%)": '100 - ((node_filesystem_avail_bytes{mountpoint="/"} * 100) / node_filesystem_size_bytes{mountpoint="/"})'
}

def get_metric(query):
    try:
        response = requests.get(PROMETHEUS_URL, params={'query': query})
        result = response.json()['data']['result']
        if result:
            return round(float(result[0]['value'][1]), 2)
        return "N/A"
    except Exception as e:
        return f"Error: {e}"

print("--- 🖥️ SERVER HEALTH REPORT ---")
for name, query in QUERIES.items():
    value = get_metric(query)
    status = "⚠️ WARNING" if isinstance(value, float) and value > 80 else "✅ OK"
    print(f"{name}: {value}% {status}")
