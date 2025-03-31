"""Bitcoin Price Index"""

import sys
import requests


def main():
    """Main code"""
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin", timeout=10)
        content = response.json()
        price = float(content["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error due fetching coincap.io via API")
    except (KeyError, ValueError):
        sys.exit("Error due parsing coincap.io API response")

    print(f"${n*price:,.4f}")


if __name__ == "__main__":
    main()
