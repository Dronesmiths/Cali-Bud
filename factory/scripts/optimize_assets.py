import os
import re
import subprocess

# Configuration
base_dir = "/Users/mediusa/NOVA/Repos/Cali-Bud"
images_dir = os.path.join(base_dir, "images")
# We only want to convert content images, not branding/technical ones
extensions_to_convert = (".png", ".jpg", ".jpeg")

# Files to ABSOLUTELY EXCLUDE from conversion and reference updates to webp
# These must remain PNG for compatibility (social/ios/favicons)
branding_files = [
    "favicon-16x16.png",
    "favicon-32x32.png",
    "apple-touch-icon.png",
    "android-chrome-192x192.png",
    "android-chrome-512x512.png",
    "logo-og.png",
    "favicon.ico",
    "logo.png" # Safe to have logo.png for fallback
]

def convert_to_webp(src, dest):
    print(f"Converting {src} -> {dest}")
    try:
        # Use -lossless for logos if they are small/transparent, or high quality
        subprocess.run(["cwebp", "-q", "85", src, "-o", dest], check=True)
        return True
    except Exception as e:
        print(f"Error converting {src}: {e}")
        return False

def update_references(old_name, new_name):
    print(f"Updating references: {old_name} -> {new_name}")
    escaped_old = re.escape(old_name)
    pattern = f"(?i){escaped_old}"
    
    updated_count = 0
    for root, dirs, files in os.walk(base_dir):
        if any(ignored in root for ignored in [".git", "node_modules", "factory"]): 
            continue
        for file in files:
            if file.endswith((".html", ".css", ".js", ".json")):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Special Case: Do NOT update og:image content to webp
                    # We will handle og:image in a separate pass
                    if 'property="og:image"' in content:
                        # Find the og:image content and preserve it if it matches old_name
                        pass

                    new_content = re.sub(pattern, new_name, content)
                    
                    if content != new_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        # print(f"  Updated {filepath}")
                        updated_count += 1
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
    return updated_count

def fix_branding():
    print("Standardizing Branding (Favicons & OG Images)...")
    og_image_url = "https://calibud.club/images/logo-og.png"
    
    for root, dirs, files in os.walk(base_dir):
        if any(ignored in root for ignored in [".git", "node_modules", "factory"]): 
            continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Fix og:image
                # Regex to find meta property="og:image" content="..."
                new_content = re.sub(r'<meta property="og:image" content="[^"]+">', 
                                    f'<meta property="og:image" content="{og_image_url}">', 
                                    content)
                
                # 2. Ensure Favicons use site-root paths for consistency
                # (Optional but recommended)
                # new_content = new_content.replace('href="/images/', 'href="/images/')
                
                if content != new_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  Fixed branding in {filepath}")

def main():
    print("Starting Site-Wide Optimization & Branding Alignment...")
    
    # 1. Branding pass first (Fixes OG Images)
    fix_branding()

    # 2. Conversion pass
    all_files = os.listdir(images_dir)
    conversion_map = {}
    
    for filename in all_files:
        if filename.lower().endswith(extensions_to_convert) and filename not in branding_files:
            name_part = os.path.splitext(filename)[0]
            new_filename = f"{name_part}.webp"
            
            src_path = os.path.join(images_dir, filename)
            dest_path = os.path.join(images_dir, new_filename)
            
            if convert_to_webp(src_path, dest_path):
                conversion_map[filename] = new_filename

    # 3. Update non-branding references
    for old_img, new_img in conversion_map.items():
        update_references(old_img, new_img)

    print("\nOptimization Complete.")
    print(f"Total content images converted: {len(conversion_map)}")

if __name__ == "__main__":
    main()
