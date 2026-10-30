import glob
import re
from bs4 import BeautifulSoup

for file_path in glob.glob('*.html'):
    if file_path == 'index.html' or file_path == 'index0.html':
        continue # Skip home page because it already has a custom hero
    
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    
    # 1. Remove messy trailing breaks
    html = html.replace('<br><hr><br>', '')
    
    # 2. Check if it already has a hero section
    if 'class="hero-section"' in html:
        print(f"  Already has hero section. Skipping injection.")
    else:
        # 3. Find the first <h1> to use as the title
        match = re.search(r'<h1.*?>.*?</h1>', html, re.DOTALL | re.IGNORECASE)
        if match:
            h1_tag = match.group(0)
            
            # Extract plain text from the h1 tag (removing span etc)
            soup = BeautifulSoup(h1_tag, 'html.parser')
            title_text = soup.get_text(strip=True)
            
            # 4. Construct the hero section
            hero_html = f"""
    <!-- Premium Secondary Hero Section -->
    <div class="hero-section" style="margin-bottom: 40px; text-align: center; overflow: hidden;">
        <div class="hero-cover" style="height: 180px; background: linear-gradient(135deg, var(--dark-slate) 0%, var(--primary-blue) 100%); display: flex; align-items: center; justify-content: center;">
            <h1 style="color: #ffffff; border: none; margin: 0; padding: 0; font-size: 2.8rem !important; letter-spacing: 1px;">{title_text}</h1>
        </div>
    </div>
"""
            # Inject hero_html right before <div class="page-content-card">
            html = html.replace('<div class="page-content-card">', hero_html + '\n    <div class="page-content-card">')
            
            # Remove the original h1 tag so it isn't duplicated
            html = html.replace(h1_tag, '')
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
