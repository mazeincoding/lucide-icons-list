# This script will extract the icons from lucide-react and save them to a json and txt file
# Useful for when you know lucide-react added new icons and you need up-to-date icons

import json
import requests
from bs4 import BeautifulSoup

def extract_icons(html_content):
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all tooltip divs containing icon names
    tooltips = soup.find_all('div', class_='tooltip')
    icons = [tooltip.text for tooltip in tooltips]
    return icons

# Fetch content from the website
url = 'https://lucide.dev/icons/'
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
    content = response.text
except requests.RequestException as e:
    print(f"Error fetching content: {e}")
    exit(1)

# Extract icon names
icons = extract_icons(content)

if not icons:
    print("⚠️ No icons found! The website structure might have changed.")
    exit(1)

# Save as txt
with open('icons.txt', 'w', encoding='utf-8') as file:
    for icon in sorted(icons):
        file.write(f'{icon}\n')

# Save as JSON
icons_dict = {icon: {} for icon in sorted(icons)}
with open('icons.json', 'w', encoding='utf-8') as file:
    json.dump(icons_dict, file, indent=2)

print(f"✅ Found {len(icons)} icons!")