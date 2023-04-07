import json
import socket
import time
import urllib.request
import os
import httpagentparser
from accept_language import parse_accept_language

def get_browser_name():
    user_agent = os.environ.get('HTTP_USER_AGENT', '')
    parsed_ua = httpagentparser.detect(user_agent)
    browser_name = parsed_ua.get('browser', {}).get('name', 'Unknown')
    return browser_name

def get_ip_info():
    url = "http://www.geoplugin.net/json.gp?ip="
    try:
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            data = json.loads(response.read())
            return data
        else:
            print(f"Error: API returned status code {response.getcode()}")
            return None
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
        return None

def get_time():
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S')
    return time_stamp

def get_language():
    accept_language = os.environ.get('HTTP_ACCEPT_LANGUAGE', '')
    parsed_languages = parse_accept_language(accept_language)
    if parsed_languages:
        preferred_language = parsed_languages[0].language
        return preferred_language
    else:
        return 'Unknown'

def get_client_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ipaddress = s.getsockname()[0]
        s.close()
        return ipaddress
    except socket.error as e:
        print(f"Error: {e}")
        return None

def get_server_info():
    server_info = {}
    for k, v in os.environ.items():
        if k.startswith("HTTP_"):
            server_info[k] = v
    return server_info

browser_name = get_browser_name()
print(f"Browser Name: {browser_name}")

ip_info = get_ip_info()
print(f"IP Info: {ip_info}")

time_stamp = get_time()
print(f"Time: {time_stamp}")

language = get_language()
print(f"Language: {language}")

client_ip = get_client_ip()
print(f"Client IP: {client_ip}")

server_info = get_server_info()
print(f"Server Info: {server_info}")