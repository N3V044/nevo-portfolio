# Falcon X SIEM - Interactive Security Dashboard Demo

![Project](https://img.shields.io/badge/Type-B.Sc.%20Final%20Project-blue)
![Grade](https://img.shields.io/badge/Grade-98%2F100-brightgreen)
![Status](https://img.shields.io/badge/Status-Complete-success)

## Overview

Falcon X SIEM is a next-generation Security Information and Event Management system designed as a B.Sc. final project at Ramat Gan Academic College (Information Systems Engineering, Cyber Security specialization).

The project designed a comprehensive upgrade to **Harel Insurance's** existing Falcon monitoring system - transforming it from a passive NOC tool into a full SIEM platform with SOC capabilities.

**This repository contains an interactive demo** that showcases the system's core capabilities.

## Live Demo

Open `index.html` in any modern browser - no server required.

**Or view it live:** [GitHub Pages link will be here after deployment]

## Features

### SOC Command Center
- Real-time alert feed with severity classification (Critical / High / Medium / Low)
- Alerts update automatically every 6 seconds with new incoming events
- Status transitions (Open -> In Progress -> Resolved) happen in real-time
- Click any alert row to view full details and recommended actions
- Severity distribution donut chart updates dynamically
- Sparkline trend charts on each metric card

### Correlation Engine
- Interactive demo showing how 3 independent events (Firewall, IDS, Server Monitor) are correlated into a single DDoS attack detection
- Step-by-step animation with visual feedback

### Automated Playbooks
- **DDoS Response** - Network attack containment in < 30 seconds
- **Malware Containment** - Endpoint threat isolation in < 45 seconds
- **IAM Anomaly** - Identity threat response in < 20 seconds
- Each playbook includes a full timeline with detect/correlate/respond/resolve phases

### UEBA (User & Entity Behavior Analytics)
- Baseline user profiling vs. real-time anomaly detection
- Demo scenario: CFO account compromise with 6 triggered anomalies
- Risk score visualization with automated response

## Key Contributions

- **Correlation engine** linking events across firewalls, IDS, EDR, and server monitors
- **UEBA behavioral profiling** for insider threat detection
- **Automated playbooks** for DDoS, malware, and IAM anomalies
- **Severity classification system** that reduced false positives by 25%
- Several concepts were implemented in the production environment

## Project Info

| Field | Details |
|-------|---------|
| Project | Falcon X SIEM |
| Type | B.Sc. Final Project |
| Grade | **98 / 100** |
| Institution | Ramat Gan Academic College |
| Organization | Harel Insurance |
| Team | Nevo Ben Ami, Itai Assis |
| Advisor | Shlomo Katz |
| Standards | ISO 27001, GDPR |
| Key Tech | SIEM, UEBA, IAM, EDR |

## Tech Stack

- HTML5 / CSS3 / Vanilla JavaScript
- Canvas API (charts and gauges)
- Intersection Observer (scroll animations)
- No external dependencies

## Author

**Nevo Ben Ami** - Security Analyst
