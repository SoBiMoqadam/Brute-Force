# Brute-force Script — Pseudocode & Safety Guidelines

This file contains **pseudocode and safety guidance only**. **No executable attack code is included.**

## Purpose
Describe the architecture of an educational brute-force script intended to be run **only** in a controlled environment and with explicit authorization.

## Safety Principles
- Run only on **localhost** or within an isolated VM/container.
- Require an explicit manual safety check before running (e.g., setting `I_HAVE_PERMISSION = True` in the environment).
- Enforce request throttling, randomized delays, and comprehensive logging.
- Any unauthorized use is strictly prohibited.

## Pseudocode
1. Read configuration (only local file paths)
2. Explicit user confirmation:
   - Display a prominent warning
   - Require typing `I UNDERSTAND` to proceed
3. Build a list of credentials (from a local file)
4. For each credential in the list:
   - Perform a **single** login request
   - Log the result (no automatic exploitation)
   - Apply delay and backoff
5. Display a summary and exit

## Final note
If your goal is educational practice, prefer safe, purpose-built vulnerable applications and platforms such as **OWASP Juice Shop** or CTF-style environments.
