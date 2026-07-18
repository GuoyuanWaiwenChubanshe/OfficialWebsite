import os
import glob
from datetime import datetime
from pathlib import Path

def generate_sitemap():
    # Get all HTML files (excluding sitemap itself)
    html_files = []
    for file in glob.glob('**/*.html', recursive=True):
        if file != 'sitemap.html' and not file.startswith('.'):
            html_files.append(file)
    
    # Sort files alphabetically
    html_files.sort()
    
    # Get current date for the timestamp
    current_date = datetime.now().strftime("%Y-%m-%d at %H:%M UTC")
    
    # Generate the sitemap HTML content
    html_content = '''<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="UTF-8">
  <meta name="description" content="The sitemap.html page of the Boomgaard Foreign Languages Publishing Company. This page serves as the global navigation page to find every page on our website.">
  <meta name="keywords" content="Boomgaard Foreign Languages Publishing Company, Boomgaard, Publishing Company, Boomgaard Publishing Company">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="copyright"content="All Rights Reserved © 2026 Organiser：Boomgaard Foreign Languages Publishing Company">
  <meta http-equiv="Content-Language" content="en-GB">
  <meta name="language" content="en-GB">
  <meta name="geo.position" content="51.5074; -0.1278">
  <meta name="geo.region" content="GB-LND">
  <meta name="geo.placename" content="London, United Kingdom">
  <meta name="ICBM" content="51.5074, -0.1278">
  <meta name="author" content="Köhn-van den Boomgaard Institute for the Theoretical Study of Scientific Socialism and Communism">
  <meta name="application-name" content="果园外文出版社">
  <meta property="og:title" content="Sitemap - Boomgaard Foreign Languages Publishing Company"/>
  <meta property="og:url" content="https://www.boomgaard.org/sitemap.html">
  <meta property="og:image" content="https://www.boomgaard.org/images/banner.jpg"/>
  <meta property="og:site_name" content="Boomgaard Foreign Languages Publishing Company"/>
  <meta property="og:locale" content="en-GB">
  <meta property="og:description" content="The Boomgaard Foreign Languages Publishing Company is a nonprofit specialised in the research and dissemination of Communist/Socialist works and materials."/>
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <title>Sitemap - Boomgaard Foreign Languages Publishing Company</title>
  <link rel="dns-prefetch" href="//www.boomgaard.org">
  <link rel="preconnect" href="https://www.boomgaard.org">
  <link rel="stylesheet" href="https://www.boomgaard.org/styles.css">
  <link rel="icon" type="image/x-icon" href="https://www.boomgaard.org/images/favicon.ico">
  <link rel="icon" type="image/png" sizes="512x512" href="https://www.boomgaard.org/images/favicon512.png">
  <link rel="icon" type="image/png" sizes="256x256" href="https://www.boomgaard.org/images/favicon256.png">
  <link rel="icon" type="image/png" sizes="192x192" href="https://www.boomgaard.org/images/favicon192.png">
  <link rel="icon" type="image/png" sizes="128x128" href="https://www.boomgaard.org/images/favicon128.png">
  <link rel="icon" type="image/png" sizes="64x64" href="https://www.boomgaard.org/images/favicon64.png">
  <link rel="icon" type="image/png" sizes="48x48" href="https://www.boomgaard.org/images/favicon48.png">
  <link rel="icon" type="image/svg+xml" href="https://www.boomgaard.org/images/favicon.svg">
  <link rel="apple-touch-icon" sizes="180x180" href="https://www.boomgaard.org/images/favicon180.png">
  <link rel="apple-touch-icon" sizes="120x120" href="https://www.boomgaard.org/images/favicon120.png">
  <link rel="manifest" href="https://www.boomgaard.org/site.webmanifest">
  <link rel="canonical" href="https://www.boomgaard.org/sitemap.html">
  <link rel="alternate" hreflang="x-default" href="https://www.boomgaard.org/sitemap.html">
</head>

<body>

<header class="top-header">
   <div class="container">
    <a href="https://www.boomgaard.org">
     <img src="https://www.boomgaard.org/images/%E6%9E%9C%E5%9B%AD%E5%A4%96%E6%96%87%E5%87%BA%E7%89%88%E7%A4%BE.webp" alt="Company Logo - All Rights Reserved © 2026 Organiser：Boomgaard Foreign Languages Publishing Company" class="logo" as="image" width="330.64" height="80" fetchpriority="high">
    </a>
   </div>
</header>

 <nav class="nav-bar">
  <div class="container nav-links">
   <a href="https://www.boomgaard.org">Frontpage</a>
 	 <a href="https://www.boomgaard.org/library/">Library</a>
 	 <a href="https://www.boomgaard.org/about">About</a>
 	 <a href="https://www.boomgaard.org/library/recommendation/">Recommendations</a>
 	 <a href="https://www.boomgaard.org/contact">Contact</a>
  </div>
      <div class="boomgaard-language-selector">
        <button class="boomgaard-language-button">中文 ▾</button>
          <div class="boomgaard-language-dropdown">
            <a href="https://www.boomgaard.org/ar-SA/" lang="ar-SA">العربية</a>
            <a href="https://www.boomgaard.org/de-DE/" lang="de-DE">Deutsch</a>
            <a href="https://www.boomgaard.org/en-GB/" lang="en-GB">English</a>
            <a href="https://www.boomgaard.org/eo/" lang="eo">Esperanto</a>
            <a href="https://www.boomgaard.org/es-CU/" lang="es-CU">Español</a>
            <a href="https://www.boomgaard.org/fil-PH/" lang="fil-PH">Filipino</a>
            <a href="https://www.boomgaard.org/fr-FR/" lang="fr-FR">Français</a>
            <a href="https://www.boomgaard.org/hi-IN/" lang="hi-IN">हिंदी</a>
            <a href="https://www.boomgaard.org/id-ID/" lang="id-ID">Bahasa Indonesia</a>
            <a href="https://www.boomgaard.org/it-IT/" lang="it-IT">Italiano</a>
            <a href="https://www.boomgaard.org/ja-JP/" lang="ja-JP">日本語</a>
            <a href="https://www.boomgaard.org/ko-KP/" lang="ko-KP">조선어</a>
            <a href="https://www.boomgaard.org/lo-LA/" lang="lo-LA">ລາວ</a>
            <a href="https://www.boomgaard.org/ms-MY/" lang="ms-MY">Bahasa Melayu</a>
            <a href="https://www.boomgaard.org/nl-NL/" lang="nl-NL">Nederlands</a>
            <a href="https://www.boomgaard.org/pt-BR/" lang="pt-BR">Português</a>
            <a href="https://www.boomgaard.org/ru-RU/" lang="ru-RU">Русский</a>
            <a href="https://www.boomgaard.org/ug-CN/" lang="ug-CN">ئۇيغۇر تىلى</a>
            <a href="https://www.boomgaard.org/vi-VN/" lang="vi-VN">Tiếng Việt</a>
            <a href="https://www.boomgaard.org" lang="zh-CN">中文</a>
          </div>
      </div>
   <div class="divider-top"></div>
<div class="breadcrumb">
  <a href="https://www.boomgaard.org">Frontpage</a>
  <span>/</span>
  <a href="https://www.boomgaard.org/sitemap.html">Sitemap.html</a>
</div>
 </nav>

<main>
  <div class="container sitemap-container">
    <h1>Site Map</h1>
    <p>Complete index of all pages on the Boomgaard Foreign Languages Publishing Company website.</p>
    <div class="divider"></div>
    <ul class="sitemap-list">
'''

    # Add all pages as list items
    for file in html_files:
        # Clean up the path for display
        display_name = file.replace('index.html', '').replace('.html', '')
        if display_name.endswith('/'):
            display_name = display_name[:-1]
        if display_name == '':
            display_name = 'Home'
        elif display_name == 'index':
            display_name = 'Home'
        
        # Clean up the display name
        display_name = display_name.replace('-', ' ').replace('_', ' ')
        # Capitalize first letter of each word
        display_name = ' '.join(word.capitalize() for word in display_name.split())
        
        # Convert file path to URL
        url = file.replace('index.html', '').replace('\\', '/')
        if url == '':
            url = '/'
        elif not url.startswith('/'):
            url = '/' + url
        
        html_content += f'      <li><a href="{url}">{display_name}</a></li>\n'
    
    # Close the HTML with your existing footer
    html_content += f'''    </ul>
    <div class="divider"></div>
    <p class="sitemap-timestamp">Last updated: {current_date}</p>
  </div>
</main>

<footer>
  <div class="footer-top">
    <p lang="en">All Rights Reserved © 2026 Organiser：Boomgaard Foreign Languages Publishing Company</p>
    <div class="footer-links">
      <a href="https://www.boomgaard.org/legal/terms">Terms of Service</a>
      <span>|</span>
      <a href="https://www.boomgaard.org/legal/privacy">Privacy Policy</a>
      <span>|</span>
      <a href="https://www.boomgaard.org/legal/conduct">Code of Conduct</a>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="left-text">
      <a href="https://www.boomgaard.org/legal/registration">Future content reserved</a>
    </div>
    <div class="right-text">
      <a href="https://www.boomgaard.org/sitemap.xml">sitemap.xml</a> / <a href="https://www.boomgaard.org/sitemap.html">sitemap.html</a>
    </div>
  </div>
</footer>
</body>
</html>'''
    
    # Write sitemap
    with open('sitemap.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Sitemap generated successfully with {len(html_files)} pages")
    print(f"📅 Last updated: {current_date}")

if __name__ == "__main__":
    generate_sitemap()
