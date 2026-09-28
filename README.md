# Anti-Phishing API

A REST API designed to analyze and identify URLs suspected of phishing and social engineering tactics. The tool performs multi-layer checks to determine the risk level of a link before a user interacts with it.

## Key Features

* Heuristic Analysis: Identifies suspicious domain patterns, including typosquatting, excessive subdomains, and direct IP usage.
* Protocol & Security Verification: Checks for valid HTTPS usage and safe navigation parameters.
* Risk Score: Returns a numeric and categorical indicator reflecting the probability of a link being malicious.
* External Integration: Queries threat intelligence databases to validate domain reputation.
