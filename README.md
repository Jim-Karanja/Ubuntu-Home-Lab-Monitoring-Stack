# Ubuntu Home-Lab Monitoring Stack
A lightweight, containerized monitoring solution for Ubuntu Server 24.04. This project uses Prometheus to collect system metrics via Node Exporter and visualizes them through a Grafana dashboard
# Tech Stack
OS: Ubuntu Server 24.04 (Noble Numbat)

Runtime: Docker & Docker Compose

Metrics: Prometheus & Node Exporter

Visualization: Grafana

Networking: Cloudflare Tunnels (for remote SSH access)
# Features
Real-time Monitoring: Track CPU, Memory, and Disk usage with 15s refresh rates.

Network Analysis: Monitor inbound and outbound traffic spikes.

Auto-Start: Configured with Docker restart policies to launch on system boot.

Remote Access: Securely accessible via Cloudflare Tunnels without opening router ports
Infrastructure as Code:** Entire monitoring stack deployed via Docker Compose with automated restart policies.
Automated Diagnostics:** Includes a Python-based health check script that queries the Prometheus API for instant CLI-based status reports.
Alerting ready:** Configured to support Webhook integrations for external notifications.
# dashboards
<img width="1351" height="682" alt="image" src="https://github.com/user-attachments/assets/a811f8fb-2a78-439e-81f8-0190f7ed22fb" />
<img width="556" height="151" alt="image" src="https://github.com/user-attachments/assets/67033a8f-87f2-4273-b63f-18f356a14270" />
