import glob
from bs4 import BeautifulSoup
import re

google_fonts = """
    <!-- Masterpiece Modern Redesign -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Inter:wght@400;500;600&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
"""

for file_path in glob.glob('*.html'):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Fix the double html tags which is common in this repo
    content = content.replace('<html lang="en">\n<html>', '<html lang="en">')
    content = content.replace('<html>\n<head>', '<html lang="en">\n<head>')
    
    # 2. Parse with BS4 to easily strip out inline <style> tags 
    # (wait, BS4 will modify the entire layout, maybe just regex is safer to preserve exact original indentation of body)
    # Let's use regex to remove <style>...</style> blocks
    content = re.sub(r'<style.*?>.*?</style>', '', content, flags=re.DOTALL)
    
    # 3. Add Google fonts before </head> if not already there
    if 'fonts.googleapis.com' not in content:
        content = content.replace('</head>', google_fonts + '</head>')
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
