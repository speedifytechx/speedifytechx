"""
Update Bing Verification Code in all HTML files
"""

import os
import re

# Get the project root directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Your Bing verification code
BING_CODE = "C4A1403A1298B99CB45A13CCBBC551ED"

def update_bing_verification():
    """Update Bing verification code in all HTML files"""
    html_files = []
    
    # Find all HTML files in project root
    for file in os.listdir(project_root):
        if file.endswith('.html'):
            html_files.append(os.path.join(project_root, file))
    
    print(f"Found {len(html_files)} HTML files to update")
    print(f"Bing Verification Code: {BING_CODE}")
    print("=" * 60)
    
    updated_count = 0
    
    for filepath in html_files:
        filename = os.path.basename(filepath)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if placeholder exists
            if 'YOUR_BING_VERIFICATION_CODE' in content:
                # Replace placeholder with actual code
                content = content.replace('YOUR_BING_VERIFICATION_CODE', BING_CODE)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"✓ {filename} - Updated")
                updated_count += 1
            elif BING_CODE in content:
                print(f"- {filename} - Already has correct code")
            else:
                print(f"? {filename} - No placeholder found")
                
        except Exception as e:
            print(f"✗ {filename} - Error: {str(e)}")
    
    print("=" * 60)
    print(f"Update Complete! {updated_count} files updated.")
    print("\nNext Steps:")
    print("1. Upload updated HTML files to your server")
    print("2. Go to Bing Webmaster Tools: https://www.bing.com/webmasters")
    print("3. Click 'Verify' button")
    print("4. Submit sitemap: https://speedifytechx.in/sitemap.xml")

if __name__ == "__main__":
    update_bing_verification()
