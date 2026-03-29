import re
import sys

SUSPICIOUS_TLDS = [".xyz", ".top", ".info", ".club", ".tk"]
URGENT_PHRASES = ["urgent", "immediately", "action required", "verify now", "today", "expire"]


def extract_sender(text: str) -> str:
    match = re.search(r"^from:\s*(?:.*<)?([^\s<>]+@[^\s<>]+)>?", text, re.IGNORECASE | re.MULTILINE)
    return match.group(1).strip().lower() if match else "Unknown"


def analyze_email(filepath: str) -> None:
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            raw_text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return

    text = raw_text.lower()
    scores = []
    indicators = []
    categories_found = {"links": False, "sender": False, "language": False}

    # 1. Suspicious links (max 4 points)
    suspicious_urls = []
    urls = re.findall(r"https?://[^\s<>\"']+", text)

    for url in urls:
        if re.search(r"https?://\d{1,3}(?:\.\d{1,3}){3}", url):
            suspicious_urls.append(f"{url} (raw IP)")
        elif any(tld in url for tld in SUSPICIOUS_TLDS) or url.count(".") > 3:
            suspicious_urls.append(f"{url} (uncommon domain)")

    if suspicious_urls:
        scores.append(4)
        indicators.append(f"Suspicious links: URL found including {', '.join(suspicious_urls)}")
        categories_found["links"] = True

    # 2. Spoofed sender hints (max 3 points)
    sender = extract_sender(raw_text)

    if sender != "Unknown":
        domain = sender.split("@")[-1]
        hints = []

        if any(c.isdigit() for c in domain):
            hints.append("digits in domain")
        if "rn" in domain:
            hints.append("lookalike pattern 'rn'")
        if domain.count(".") > 2:
            hints.append("many subdomains")

        if hints:
            scores.append(3)
            indicators.append(f"Spoofed sender hints: {', '.join(hints)} ({domain})")
            categories_found["sender"] = True

    # 3. Urgent language (max 3 points)
    found_phrases = [f'"{phrase}"' for phrase in URGENT_PHRASES if phrase in text]

    if found_phrases:
        scores.append(min(len(found_phrases), 3))
        indicators.append(f'Urgent language: matched {", ".join(found_phrases)}')
        categories_found["language"] = True

    # 4. Verdict
    total_score = sum(scores)
    breakdown = "+".join(str(score) for score in scores) if scores else "0"

    if total_score >= 7:
        verdict = "HIGH RISK PHISHING"
    elif total_score >= 3:
        verdict = "LIKELY PHISHING"
    else:
        verdict = "NOT LIKELY PHISHING"

    print("\n--- Phishing Detector Summary ---")
    print(f"Verdict: {verdict}")
    print(f"Phishing score (1-10): {total_score} ({breakdown})")
    print(f"Source address: {sender}")
    print("Detected indicators:")

    if indicators:
        for indicator in indicators:
            print(f" * {indicator}")
    if not categories_found["links"]:
        print(" * No suspicious links found")
    if not categories_found["sender"]:
        print(" * No spoofed sender hints found")
    if not categories_found["language"]:
        print(" * No urgent language found")

    print("---------------------------------\n")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        analyze_email(sys.argv[1])
    else:
        print("Usage: python phishing_detector.py <email.txt>")
