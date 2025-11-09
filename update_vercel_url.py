"""
Script to update README.md with Vercel deployment URL
Run this after deploying to Vercel with your live URL
"""

import re
import sys

def update_readme_url(vercel_url):
    """Update README.md with the actual Vercel URL."""
    
    readme_path = 'README.md'
    
    try:
        # Read README
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace placeholder URL with actual URL
        content = content.replace('https://your-app.vercel.app', vercel_url)
        content = content.replace('YOUR_VERCEL_URL_HERE', vercel_url)
        
        # Write back
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ README.md updated successfully!")
        print(f"   Live URL: {vercel_url}")
        print("\nNext steps:")
        print("1. Add screenshots to screenshots/ folder")
        print("2. Run: git add README.md screenshots/")
        print("3. Run: git commit -m 'Update live URL and add screenshots'")
        print("4. Run: git push")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🔐 EmotionCipher - Update Vercel URL")
    print("="*70 + "\n")
    
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter your Vercel deployment URL: ").strip()
    
    # Clean up URL
    if not url.startswith('http'):
        url = 'https://' + url
    
    print(f"\nUpdating README.md with: {url}\n")
    update_readme_url(url)
