import requests

failed_codes = [
    "100016", "100025", "118635",
    "102886", "102887", "148568"
]

for code in failed_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url, timeout=30)
        print(
            code,
            "Status:", response.status_code,
            "Response:", response.text[:200]
        )
    except requests.RequestException as e:
        print(code, "Error:", e)