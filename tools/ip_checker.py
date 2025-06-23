import requests
import sys
import socket

def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception:
        return None

def is_ip(string):
    try:
        socket.inet_aton(string)
        return True
    except:
        return False

def format_coords(lat, lon):
    lat_dir = 'N' if lat >= 0 else 'S'
    lon_dir = 'E' if lon >= 0 else 'W'
    return f"{abs(lat)}° {lat_dir}", f"{abs(lon)}° {lon_dir}"

def get_ip_info(target):
    ip = resolve_domain(target) if not is_ip(target) else target
    if not ip:
        print(f"❌ Cannot resolve: {target}")
        return

    try:
        url = f"https://ipwho.is/{ip}"
        res = requests.get(url).json()

        if not res.get("success", False):
            print("❌ Failed to get data.")
            return

        lat_formatted, lon_formatted = format_coords(res.get('latitude'), res.get('longitude'))

        print(f"\n📍 IP Checker Result for: {target}")
        print("-" * 60)
        print(f"🔹 IP Address : {res.get('ip')}")
        print(f"🌐 Hostname   : {res.get('connection', {}).get('domain', 'N/A')}")
        print(f"🏙️  City       : {res.get('city')}")
        print(f"🏞️  Region     : {res.get('region')}")
        print(f"📮 ZIP Code   : {res.get('postal')}")
        print(f"🌎 Country    : {res.get('country')} ({res.get('country_code')})")
        print(f"📍 Latitude   : {lat_formatted}")
        print(f"📍 Longitude  : {lon_formatted}")
        print(f"🕐 Timezone   : {res.get('timezone', {}).get('id')}")
        print(f"🏢 ISP        : {res.get('connection', {}).get('isp')}")
        print(f"🔢 ASN        : {res.get('connection', {}).get('asn')}")
        print(f"📡 Type       : {res.get('type')}")
        print("-" * 60)

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ip_checker.py <ip_or_domain>")
    else:
        get_ip_info(sys.argv[1])
