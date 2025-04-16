# Lucide Icons List

A script that gets all the icons from [Lucide](https://lucide.dev/) and saves them to files. Lucide has a nice collection of consistent, well-designed icons.

## What it does

Pulls from Lucide's website to create:
- A text file listing all icons (`icons.txt`) 
- The same list in JSON format (`icons.json`)

Made this so you can reference all Lucide's icons to any LLM so it knows all the available icons it can use.

## Usage

Grab everything in `icons.txt` or `icons.json` file.

## Check for new icons

Want to see what new icons Lucide's added without updating your files? Just run:

```bash
python check_new_icons.py
```

It'll compare the icons list with all Lucide's icons and tell you if there's anything new.

## Updating the icons

Want to update the icon list yourself? You'll need:

### Requirements
- Python 3.x
- These packages:
  ```
  requests>=2.31.0
  beautifulsoup4>=4.12.2
  ```

### Setup
1. Get the code:
   ```bash
   git clone https://github.com/mazeincoding/lucide-icons-list.git
   cd lucide-icons-list
   ```

2. Install what you need:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the update:
   ```bash
   python extract_icons.py
   ```

This'll grab all the latest icons and update both files.
