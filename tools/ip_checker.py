import requests
import sys
import socket

def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception:
        return None

def get_ip_info(target):
    ip = resolve_domain(target) if not is_ip(target) else target
    if not ip:
        print(f"❌ Cannot resolve domain: {target}")
        return

    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url)
        data = response.json()

        print(f"\n📍 IP Checker Result for: {target}")
        print("-" * 50)
        print(f"🔹 IP Address  : {ip}")
        print(f"🌐 Hostname    : {data.get('hostname', 'N/A')}")
        print(f"🏙️  City        : {data.get('city', 'N/A')}")
        print(f"🌎 Country     : {data.get('country', 'N/A')}")
        print(f"📍 Location    : {data.get('loc', 'N/A')}")
        print(f"🏢 ISP         : {data.get('org', 'N/A')}")
        print(f"🔢 ASN         : {data.get('asn', {}).get('asn', 'N/A')}")
        print("-" * 50)

    except Exception as e:
        print(f"❌ Error: {e}")

def is_ip(string):
    try:
        socket.inet_aton(string)
        return True
    except:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ip_checker.py <ip_or_domain>")
    else:
        get_ip_info(sys.argv[1])
