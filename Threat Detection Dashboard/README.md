# SentinelView - Threat Detection Dashboard

A professional, interactive threat detection and response dashboard built as a portfolio project for cybersecurity analyst and SOC/MDR roles.

Live Demo: `https://<your-username>.github.io/threat-detection-dashboard/`

---

## Overview

SentinelView simulates a realistic Security Operations Center (SOC) dashboard used in Managed Detection and Response (MDR) environments. It displays 25 hardcoded security alerts across three severity levels and allows analysts to search, filter, and investigate each event with detailed context, threat rationale, and recommended actions.

This project demonstrates practical understanding of:
- Security alert triage and prioritization
- Incident investigation workflows
- Threat detection event types commonly seen in enterprise environments
- SOC/MDR analyst decision-making processes

---

## Key Features

- **Summary Cards** - Real-time counts for total, high, medium, and low severity alerts
- **Alerts Table** - Professional sortable table with severity badges, status indicators, and timestamps
- **Search** - Live text search across event types, users, IPs, assets, and descriptions
- **Severity Filters** - One-click filtering by High, Medium, or Low severity
- **Investigation Modal** - Detailed investigation panel for each alert showing event details, threat rationale, and recommended analyst actions
- **Alert Actions** - Dismiss or Escalate to Tier 2 with confirmation toast notifications
- **Responsive Layout** - Works on desktop, tablet, and mobile screens
- **Dark Theme** - Professional SOC-style dark interface

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Structure | HTML5 (semantic) |
| Styling | CSS3 (custom properties, grid, flexbox) |
| Logic | Vanilla JavaScript (ES6+) |
| Fonts | Google Fonts (DM Sans, JetBrains Mono) |
| Hosting | GitHub Pages (static files only) |

No frameworks, no build tools, no backend, no dependencies to install.

---

## Project Structure

```
threat-detection-dashboard/
  index.html    - Main dashboard page (HTML structure)
  styles.css    - All styling (dark theme, layout, components)
  script.js     - Alert data, rendering, search, filter, modal logic
  README.md     - Project documentation
```

---

## How It Works

1. **Data Layer** - 25 realistic security alerts are hardcoded in `script.js` as a JavaScript array. Each alert includes ID, event type, user, IP, timestamp, severity, status, asset, description, threat rationale, and recommended action.

2. **Rendering** - On page load, the dashboard renders all alerts into an HTML table. Summary cards update to reflect current counts.

3. **Search** - As the user types in the search box, alerts are filtered in real time by matching against event type, user, IP, asset, and description fields.

4. **Filter** - Clicking a severity filter button (All / High / Medium / Low) shows only alerts matching that severity level. Filters combine with search.

5. **Investigation** - Clicking "Investigate" on any alert opens a modal panel with full event details, an explanation of why the event is suspicious, and specific recommended analyst actions.

6. **Actions** - The modal includes "Dismiss Alert" and "Escalate to Tier 2" buttons that close the modal and show a confirmation toast.

---

## Relevance for Security Analyst / SOC / MDR Roles

This project demonstrates skills directly relevant to security operations:

- **Alert Triage** - Understanding severity levels and how to prioritize investigation
- **Threat Analysis** - Each alert includes realistic threat context explaining why the behavior is suspicious
- **Incident Response** - Recommended actions follow real-world SOC playbook patterns (isolate, investigate, escalate, remediate)
- **Event Types** - Covers common detection categories including brute force, phishing, privilege escalation, data exfiltration, malware, DDoS, and insider threats
- **Analyst Workflow** - The investigate-assess-act flow mirrors how real SOC analysts process alerts in SIEM and SOAR platforms

---

## How to Run Locally

1. Download or clone the repository
2. Open `index.html` in any modern web browser

That is all. No installation, no build step, no server required.

---

## GitHub Pages Deployment

This project is fully compatible with GitHub Pages. After uploading the files to a GitHub repository:

1. Go to the repository Settings
2. Navigate to Pages (under "Code and automation")
3. Set Source to "Deploy from a branch"
4. Select the `main` branch and `/ (root)` folder
5. Click Save

The dashboard will be live at `https://<your-username>.github.io/<repository-name>/` within a few minutes.

---

## License

This project is open source and available for portfolio and educational use.
