from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import re
import time

app = Flask(__name__)

def extract_profile_id(profile_url):
    """Extract the profile ID from Upwork profile URL"""
    # Profile URL format: https://www.upwork.com/freelancers/~0101b6eacecad1f139
    match = re.search(r'~([a-f0-9]+)', profile_url)
    if match:
        return match.group(1)
    return None

def search_profile_on_page(keyword, profile_id, page_num, max_pages=1000):
    """Search for profile on Upwork search results"""
    try:
        # Construct search URL
        search_url = f"https://www.upwork.com/nx/search/talent/?nbs=1&q={keyword}&page={page_num}"
        
        # Set headers to mimic browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Make request
        response = requests.get(search_url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return None
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Search for profile links in the page
        # Profile links typically contain the profile ID
        links = soup.find_all('a', href=True)
        
        for link in links:
            href = link.get('href', '')
            if profile_id in href:
                return True
        
        return False
        
    except Exception as e:
        print(f"Error searching page {page_num}: {str(e)}")
        return None

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """Handle search request"""
    try:
        data = request.get_json()
        keyword = data.get('keyword', '').strip()
        profile_url = data.get('profile_url', '').strip()
        max_pages = int(data.get('max_pages', 100))
        
        if not keyword or not profile_url:
            return jsonify({'error': 'Keyword and profile URL are required'}), 400
        
        # Extract profile ID from URL
        profile_id = extract_profile_id(profile_url)
        if not profile_id:
            return jsonify({'error': 'Invalid profile URL format'}), 400
        
        # Limit max pages to 1000
        max_pages = min(max_pages, 1000)
        
        # Search through pages
        for page_num in range(1, max_pages + 1):
            # Add delay to avoid rate limiting
            if page_num > 1:
                time.sleep(1)  # 1 second delay between requests
            
            found = search_profile_on_page(keyword, profile_id, page_num, max_pages)
            
            if found:
                # Calculate approximate position
                # Assuming ~10 results per page
                min_position = (page_num - 1) * 10 + 1
                max_position = page_num * 10
                
                return jsonify({
                    'success': True,
                    'found': True,
                    'page': page_num,
                    'position_range': f"{min_position}-{max_position}",
                    'message': f'Profile found on page {page_num} (approximate position {min_position}-{max_position})'
                })
            
            # Return progress update
            if page_num % 10 == 0:
                print(f"Searched {page_num} pages...")
        
        return jsonify({
            'success': True,
            'found': False,
            'message': f'Profile not found in first {max_pages} pages'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
