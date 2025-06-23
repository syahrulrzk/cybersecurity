import requests
import sys

def get_ip_info(ip_or_domain):
    try:
        url = f"https://ipinfo.io/{ip_or_domain}/json"
        response = requests.get(url)
        data = response.json()

        print(f"\n📍 IP Checker Result for: {ip_or_domain}")
        print("-" * 50)
        print(f"🔹 IP Address  : {data.get('ip', 'N/A')}")
        print(f"🌐 Hostname    : {data.get('hostname', 'N/A')}")
        print(f"🏙️  City        : {data.get('city', 'N/A')}")
        print(f"🌎 Country     : {data.get('country', 'N/A')}")
        print(f"📍 Location    : {data.get('loc', 'N/A')}")
        print(f"🏢 ISP         : {data.get('org', 'N/A')}")
        print(f"🔢 ASN         : {data.get('asn', {}).get('asn', 'N/A')}")
        print("-" * 50)

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ip_checker.py <ip_or_domain>")
    else:
        get_ip_info(sys.argv[1])

