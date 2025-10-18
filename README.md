# Brute‑Force Login Simulator — Educational Repository

> **Educational demo** for authentication faults, rate‑limiting concepts, and safe testing workflows.  
> This repository **does not** contain automated attack tools — only a small, local test server and helper client for learning purposes.

---

## Important Legal & Ethical Notice

This project is for **educational** and **safe testing** only. Do **not** use or adapt any attacking scripts against targets that you do not own or do not have **explicit written permission** to test. Unauthorized testing can be illegal and harmful.

You are responsible for how you use the code and examples contained in this repository.

---

## Overview

The Brute‑Force Login Simulator is a lightweight demonstration that helps you understand:

- how simple authentication endpoints behave,
- common pitfalls (weak passwords, no rate limits, predictable responses),
- how to design mitigations (rate limiting, IP blocking, account lockout, progressive delays),
- how to safely test client behavior against a controlled target.

This repo is intentionally minimal and safe-by-design — it provides a test server (Flask) and a one-shot test client. It **does not** provide mass‑attack or automation tooling.

---

## What’s in this repository

- `vuln_app.py` — a minimal Flask test server exposing `/login` and `/status` endpoints.  
- `tester_client.py` — a simple example client that performs a single login attempt (one request).  
- `bruteforce_stub.md` — documentation and pseudo-code describing how a brute‑force script would work **for learning only** (no runnable attack code included).  
- `requirements.txt` — Python dependencies.  
- `Dockerfile` — containerized environment for isolated local testing (binds to localhost).  
- `.gitignore` — recommended ignores.

---

## Features & Learning Goals

- Understand how authentication endpoints return success/failure states.  
- Observe the difference between verbose vs. minimal error messages.  
- Explore simple defenses: rate limiting, exponential backoff, account lockouts.  
- Practice responsible testing patterns in a safe, local environment.

---

## Quickstart (Local)

> These instructions run everything on your machine or inside a local container. Do **not** expose the test server to the public internet.

```bash
# 1) Create & activate a virtual environment
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the vulnerable test server (default: localhost:5000)
python vuln_app.py
# Server will print a URL like: http://127.0.0.1:5000

# 4) Run the example client (one login attempt)
python tester_client.py --username alice --password alice123
```

---

## Docker (Isolated run)

Build the image and run entirely in a container:

```bash
# build
docker build -t brute-sim:latest .

# run container (binds to localhost inside container)
# NOTE: this container is for local testing only.
docker run --rm -p 127.0.0.1:5000:5000 brute-sim:latest
```

Then use the `tester_client.py` from host or another container to hit `http://127.0.0.1:5000`.

---

## Example API

- `POST /login` — JSON body: `{"username":"alice","password":"..."}`  
  - Returns `200` on success with `{"status":"ok","user":"alice"}`  
  - Returns `401` on failure with `{"status":"fail"}` or a minimal error message.  
- `GET /status` — returns server health & basic metrics (attempt counters).

(Exact behavior implemented in `vuln_app.py` — read it to see response structure.)

---

## Safe Testing Patterns

When you move from experiments to more advanced tooling, follow these rules:

1. **Authorization**: test only systems you own or have explicit permission for.  
2. **Throttling**: always limit request rates and concurrency.  
3. **Logging & Privacy**: redact sensitive data in shared reports.  
4. **Disclosure**: follow coordinated disclosure if you find real issues.  
5. **CI Safety**: never run attack-style tests in CI against external targets.

---

## Contributing

Contributions are welcome but must follow safety guidelines:

- Keep any examples offline or in `examples/`—never include live targets.  
- Add tests and examples that use the local server or canned fixture data.  
- When in doubt, prefer documentation and simulation over automation.

Suggested branch/commit patterns:
- `feat: add xyz`
- `fix: correct abc`
- `docs: update README or comments`

---

## Suggested first commit message

```
chore: initial import — vuln demo server, example client, docs
```

---

## License

**MIT License** (recommended). See `LICENSE` for full text.  
If you’d like, I can generate a `LICENSE` file pre-filled with your name and the current year.

---

## Contact & Attribution

Author: `SoBiMoqadam` (or replace with your real name)  
Repo: https://github.com/SoBiMoqadam/Brute-Force

---

Thank you for keeping security testing responsible — if you want,
I can:
- generate the `LICENSE` file with your name and year,
- create a polished `README.md` file in the repo and provide a downloadable file,
- or craft the exact `git commit` command to add and push these files.

Tell me which of those you want me to do now and I’ll produce it.
