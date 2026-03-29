# PhishGuard - Email Phishing Detector

![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Type](https://img.shields.io/badge/Type-Security%20Tool-red)
![Status](https://img.shields.io/badge/Status-Complete-success)

## Overview

A rule-based email phishing detection tool that scans email content for common phishing indicators and alerts the user to potential phishing attempts.

The tool checks three categories of phishing signals:
- **Suspicious links** - Raw IP addresses in URLs, uncommon TLDs (.xyz, .top, .info)
- **Spoofed sender hints** - Digits in domain, lookalike patterns (rn), excessive subdomains
- **Urgent language** - Words like "urgent", "immediately", "action required", "verify now"

## Live Demo

Open `phishing_ui.html` in any browser - no server required.

**Or view it live:** [GitHub Pages link will be here after deployment]

## Features

- **Score-based detection** - 0 to 10 phishing score with clear verdict thresholds
- **Visual score gauge** - Half-circle gauge with color gradient (green/yellow/red)
- **Email preview** - Formatted email display with highlighted suspicious elements
- **Scan animation** - Visual scanning effect across the email body
- **Compare mode** - Run all 3 sample emails side-by-side for comparison
- **VirusTotal integration** - One-click link to verify suspicious URLs externally
- **3 test emails included** - High risk, medium risk, and legitimate samples

## How It Works

### Scoring

| Category | Max Points | What It Checks |
|----------|-----------|----------------|
| Suspicious Links | 4 | Raw IP in URL, uncommon TLD, excessive dots |
| Spoofed Sender | 3 | Digits in domain, lookalike patterns, many subdomains |
| Urgent Language | 3 | Pressure words and phrases |

### Verdicts

| Score | Verdict |
|-------|---------|
| 7-10 | HIGH RISK PHISHING |
| 3-6 | LIKELY PHISHING |
| 0-2 | NOT LIKELY PHISHING |

## Usage

### Command Line

```bash
python phishing_detector.py phishing_high_risk.txt
python phishing_detector.py phishing_medium_risk.txt
python phishing_detector.py legit_email.txt
```

### Browser UI

Open `phishing_ui.html` in any modern browser. Upload a .txt file, paste email content, or click a sample card.

## Files

| File | Description |
|------|-------------|
| `phishing_detector.py` | Main Python detection script |
| `phishing_ui.html` | Browser-based UI (standalone, no server) |
| `phishing_high_risk.txt` | Test email - high risk phishing |
| `phishing_medium_risk.txt` | Test email - medium risk phishing |
| `legit_email.txt` | Test email - legitimate |

## Limitations

- Rule-based detection only (not ML)
- May miss advanced phishing techniques
- May produce false positives on legitimate urgent emails
- Does not verify domains against real trusted services
- Does not check email headers (SPF/DKIM/DMARC)

## Tech Stack

- Python 3.7+ (CLI script, no dependencies)
- HTML5 / CSS3 / JavaScript (browser UI)
- Canvas API (score gauge)

## Author

**Nevo Ben Ami** - Security Analyst
