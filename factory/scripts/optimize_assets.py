import os
import re
import subprocess

# Configuration
# Configuration
base_dir = "/Users/mediusa/NOVA/Repos/Cali-Bud"
images_dir = os.path.join(base_dir, "images")
extensions_to_convert = (".png", ".jpg", ".jpeg")

# Mapping of original names to kebab-case
# (Adding explicit mappings for complex names to avoid collision or confusion)
name_mapping = {
    "hero-home.png": "hero-home.webp",
    "service-flower.png": "service-flower.webp",
    "service-edibles.png": "service-edibles.webp",
    "service-vapes.png": "service-vapes.webp",
    "apple-touch-icon.png": "apple-touch-icon.png",
    "favicon-16x16.png": "favicon-16x16.png",
    "favicon-32x32.png": "favicon-32x32.png",
}

def convert_to_webp(src, dest):
    print(f"Converting {src} -> {dest}")
    subprocess.run(["cwebp", "-q", "80", src, "-o", dest], check=True)

def update_references(old_name, new_name):
    print(f"Updating references: {old_name} -> {new_name}")
    # Escape special characters for regex
    escaped_old = re.escape(old_name)
    # We want to match exactly the filename, possibly preceded by path separators
    # and possibly followed by quotes or other delimiters.
    pattern = f"(?i){escaped_old}"
    
    for root, dirs, files in os.walk(base_dir):
        if ".git" in root: continue
        for file in files:
            if file.endswith((".html", ".css", ".js")):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = re.sub(pattern, new_name, content)
                
                if content != new_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  Updated {filepath}")

def main():
    # 1. Convert and update mappings
    for old_name, new_name in name_mapping.items():
        old_path = os.path.join(images_dir, old_name)
        new_path = os.path.join(images_dir, new_name)
        
        if os.path.exists(old_path):
            if new_name.endswith(".webp"):
                convert_to_webp(old_path, new_path)
            # 2. Update references sitewide
            update_references(old_name, new_name)
        else:
            print(f"Skipping {old_name} (not found)")

    # Special case: catch any remaining .png, .jpg, .jpeg in js/html/css that we might have missed
    # (Optional, but let's stick to explicit mappings first for safety)

if __name__ == "__main__":
    main()
