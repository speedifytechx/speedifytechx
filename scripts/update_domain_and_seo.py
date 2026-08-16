"""
Update Domain from speedifytechx.com to speedifytechx.in
and add comprehensive SEO improvements
"""

import os
import re

# Get the project root directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Domain mapping
OLD_DOMAIN = "speedifytechx.com"
NEW_DOMAIN = "speedifytechx.in"

def update_html_files():
    """Update all HTML files with new domain and enhanced SEO"""
    html_files = []
    
    # Find all HTML files in project root
    for file in os.listdir(project_root):
        if file.endswith('.html'):
            html_files.append(os.path.join(project_root, file))
    
    print(f"Found {len(html_files)} HTML files to update")
    
    for filepath in html_files:
        print(f"\nProcessing: {os.path.basename(filepath)}")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace old domain with new domain
            original_content = content
            content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
            
            # Check if <head> section exists and add verification meta tags if not present
            if '<head>' in content:
                # Add Google Search Console verification meta tag if not present
                if 'google-site-verification' not in content:
                    # Insert after charset
                    content = content.replace(
                        '<meta charset="UTF-8">',
                        '<meta charset="UTF-8">\n    <!-- Google Search Console Verification -->\n    <meta name="google-site-verification" content="YOUR_GOOGLE_VERIFICATION_CODE">'
                    )
                
                # Add Bing Webmaster verification if not present
                if 'msvalidate.01' not in content:
                    content = content.replace(
                        '<meta name="google-site-verification"',
                        '<!-- Bing Webmaster Verification -->\n    <meta name="msvalidate.01" content="YOUR_BING_VERIFICATION_CODE">\n    <meta name="google-site-verification"'
                    )
                
                # Ensure geo tags are present for local SEO
                if 'geo.region' not in content:
                    # Add after viewport meta tag
                    viewport_pattern = r'(<meta name="viewport"[^>]+>)'
                    geo_tags = r'\1\n    \n    <!-- Geographic & Local SEO Tags -->\n    <meta name="geo.region" content="IN-TN">\n    <meta name="geo.placename" content="Chennai">\n    <meta name="geo.position" content="13.1650;80.2707">\n    <meta name="ICBM" content="13.1650, 80.2707">'
                    content = re.sub(viewport_pattern, geo_tags, content)
            
            # Only write if changes were made
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Updated successfully")
            else:
                print(f"  - No changes needed")
                
        except Exception as e:
            print(f"  ✗ Error: {str(e)}")

def update_sitemap():
    """Update sitemap.xml with new domain"""
    sitemap_path = os.path.join(project_root, 'sitemap.xml')
    
    print(f"\nProcessing: sitemap.xml")
    
    try:
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace domain
        content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
        
        # Update lastmod dates to today
        import datetime
        today = datetime.date.today().strftime('%Y-%m-%d')
        content = re.sub(r'<lastmod>\d{4}-\d{2}-\d{2}</lastmod>', f'<lastmod>{today}</lastmod>', content)
        
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("  ✓ Sitemap updated successfully")
        
    except Exception as e:
        print(f"  ✗ Error updating sitemap: {str(e)}")

def update_robots_txt():
    """Update robots.txt with new domain"""
    robots_path = os.path.join(project_root, 'robots.txt')
    
    print(f"\nProcessing: robots.txt")
    
    try:
        with open(robots_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace domain
        content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
        
        # Update date
        import datetime
        today = datetime.date.today().strftime('%Y-%m-%d')
        content = re.sub(r'Last Updated: \d{4}-\d{2}-\d{2}', f'Last Updated: {today}', content)
        
        with open(robots_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("  ✓ robots.txt updated successfully")
        
    except Exception as e:
        print(f"  ✗ Error updating robots.txt: {str(e)}")

def main():
    print("=" * 60)
    print("SPEEDIFYTECHX DOMAIN UPDATE & SEO ENHANCEMENT")
    print("=" * 60)
    print(f"Updating from: {OLD_DOMAIN}")
    print(f"Updating to:   {NEW_DOMAIN}")
    print("=" * 60)
    
    update_html_files()
    update_sitemap()
    update_robots_txt()
    
    print("\n" + "=" * 60)
    print("UPDATE COMPLETE!")
    print("=" * 60)
    print("\nNEXT STEPS:")
    print("1. Update Google Search Console verification code in HTML files")
    print("2. Update Bing Webmaster verification code in HTML files")
    print("3. Submit updated sitemap to Google Search Console")
    print("4. Submit updated sitemap to Bing Webmaster Tools")
    print("5. Set up 301 redirects from old domain to new domain")
    print("6. Update Google My Business with new domain")
    print("7. Request re-indexing in Google Search Console")
    print("=" * 60)

if __name__ == "__main__":
    main()
