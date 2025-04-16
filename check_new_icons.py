import json
import requests
from bs4 import BeautifulSoup
import os

def extract_icons_from_html(html_content):
    """Parses HTML and extracts icon names from tooltip divs."""
    soup = BeautifulSoup(html_content, 'html.parser')
    tooltips = soup.find_all('div', class_='tooltip')
    # Use a set for faster lookups later
    return {tooltip.text for tooltip in tooltips}

def fetch_lucide_icons(url='https://lucide.dev/icons/'):
    """Fetches icon names from the lucide website."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return extract_icons_from_html(response.text)
    except requests.RequestException as e:
        print(f"❌ Error fetching content from {url}: {e}")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred during fetching/parsing: {e}")
        return None

# --- Main script logic ---

def load_existing_icons(filename='icons.json'):
    """Loads existing icon names from a JSON file."""
    if not os.path.exists(filename):
        print(f"⚠️ Existing icons file '{filename}' not found. Assuming no icons exist locally.")
        return set()
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # The keys of the dictionary are the icon names
            return set(json.load(file).keys())
    except json.JSONDecodeError:
        print(f"❌ Error decoding JSON from '{filename}'. Is the file valid?")
        return None
    except Exception as e:
        print(f"❌ Error reading '{filename}': {e}")
        return None

def main():
    print("🔎 Checking for new Lucide icons...")

    # Load existing icons
    existing_icons = load_existing_icons()
    if existing_icons is None:
        print("Aborting due to error loading existing icons.")
        exit(1)
    print(f"ℹ️ Found {len(existing_icons)} icons in local 'icons.json'.")

    # Fetch current icons from website
    print("🌍 Fetching latest icons from lucide.dev...")
    latest_icons = fetch_lucide_icons()

    if latest_icons is None:
        print("Aborting due to error fetching latest icons.")
        exit(1)
    print(f"ℹ️ Found {len(latest_icons)} icons on the website.")

    if not latest_icons:
        print("⚠️ No icons found on the website! The structure might have changed or the site is down.")
        exit(1)

    # Compare and find new icons
    new_icons = latest_icons - existing_icons

    if not new_icons:
        print("✅ No new icons found. Your list is up-to-date!")
    else:
        print(f"✨ Found {len(new_icons)} new icon(s):")
        for icon in sorted(list(new_icons)):
            print(f"  - {icon}")
        print("💡 You might want to run 'extract_icons.py' to update your local files.")

if __name__ == "__main__":
    main() 