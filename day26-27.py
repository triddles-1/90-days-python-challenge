# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 10:46:26 2025

@author: Triddles lamar
"""

import requests

def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

        # Check for common security headers
        security_headers = {
            "Strict-Transport-Security": "Missing (HSTS not enabled)",
            "X-Content-Type-Options": "Missing (MIME sniffing not prevented)",
            "X-Frame-Options": "Missing (Clickjacking protection not enabled)",
            "Content-Security-Policy": "Missing (CSP not configured)",
        }

        for header, message in security_headers.items():
            if header in headers:
                print(f"{header}: {headers[header]}")
            else:
                print(f"{header}: {message}")

    except requests.RequestException as e:
        print(f"Error fetching headers: {e}")

if __name__ == "__main__":
    target_url = input("Enter the target URL: ")
    check_security_headers(target_url)