import requests

# 1. Update with your actual IP and Discord Webhook URL
PROMETHEUS_URL = "http://192.168.100.241:9090/api/v1/query"
DISCORD_WEBHOOK ="https://discord.com/api/webhooks/1456213980308832297/viB8jOhZQsVNm5wvKn993X4KPwR6J48uN3Zjy5M51wC3oaDUZoP-8MnGFk9hTwssqXTy"

# Queries for Prometheus
QUERIES = {
    "CPU Usage": '100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[2m])) * 100)',
    "RAM Usage": '(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100',
    "Disk Usage": '100 - ((node_filesystem_avail_bytes{mountpoint="/"} * 100) / node_filesystem_size_bytes{mountpoint="/"})'
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

# Build the message for Discord
report_text = "--- 🖥️ **SERVER HEALTH REPORT** ---\n"
print("--- 🖥️ SERVER HEALTH REPORT ---")

for name, query in QUERIES.items():
    value = get_metric(query)
    status = "⚠️ WARNING" if isinstance(value, float) and value > 80 else "✅ OK"
    line = f"{name}: {value}% {status}"
    print(line)
    report_text += f"{line}\n"

# Send to Discord
if "http" in DISCORD_WEBHOOK:
    requests.post(DISCORD_WEBHOOK, json={"content": report_text})
    print("🚀 Report sent to Discord!")
