import argparse
import requests
import sys

def main():
    parser = argparse.ArgumentParser(description='Tester client for vuln_app (single attempt).')
    parser.add_argument('--username', required=True)
    parser.add_argument('--password', required=True)
    parser.add_argument('--url', default='http://127.0.0.1:5000/login')
    args = parser.parse_args()

    payload = {'username': args.username, 'password': args.password}
    try:
        r = requests.post(args.url, json=payload, timeout=5)
        print('status_code:', r.status_code)
        print(r.json())
    except Exception as e:
        print('request failed:', e, file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
