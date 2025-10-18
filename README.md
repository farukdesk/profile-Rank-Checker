# Upwork Profile Rank Checker

A web application that helps freelancers find their profile ranking on Upwork search results for specific keywords.

**New PHP/JavaScript Version**: This project now includes a PHP/JavaScript implementation alongside the original Python version, making it easy to deploy on standard web hosting platforms like Apache/Nginx with PHP support.

## Screenshots

### User Interface
![Upwork Profile Rank Checker Interface](https://github.com/user-attachments/assets/e3d4e73c-ef75-4d19-bd34-b8cbf1619529)

### Search Results
![Search Result Example](https://github.com/user-attachments/assets/9d4ea82f-5b3b-4b4e-9577-5787c2590068)

## Features

- 🔍 Search for your Upwork profile across search result pages
- 📊 Get your approximate ranking position for any keyword
- 🎯 Support for searching up to 1000 pages
- 💫 User-friendly web interface
- ⚡ Real-time search progress

## How It Works

1. **Enter Your Keyword**: Type in the skill or keyword you want to search for (e.g., "UX designer")
2. **Provide Your Profile URL**: Paste your Upwork profile URL (e.g., `https://www.upwork.com/freelancers/~0101b6eacecad1f139`)
3. **Set Search Limit**: Choose how many pages to search (default: 100, max: 1000)
4. **Get Results**: The app will search through Upwork pages and tell you exactly where your profile appears

## Installation

You can use either the **PHP/JavaScript version** (recommended for web hosting) or the **Python version** (for local development).

### Option 1: PHP/JavaScript Version (Recommended for Web Hosting)

#### Prerequisites
- PHP 7.4 or higher with cURL extension enabled
- Web server (Apache, Nginx, or any PHP-compatible server)

#### Setup

1. Clone the repository:
```bash
git clone https://github.com/farukdesk/profile-Rank-Checker.git
cd profile-Rank-Checker
```

2. Upload files to your web server:
   - Upload `index.html` (or `index.php`) to your web root
   - Upload `profile_rank_check.php` to the same directory

3. Ensure PHP cURL extension is enabled:
```bash
# Check if cURL is enabled
php -m | grep curl
```

4. Set proper permissions:
```bash
chmod 644 index.html profile_rank_check.php
```

5. Access via your domain:
```
https://smartapplypro.com/profile_rank_check.php
# or
https://smartapplypro.com/index.html
```

### Option 2: Python Version (For Local Development)

#### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

#### Setup

1. Clone the repository:
```bash
git clone https://github.com/farukdesk/profile-Rank-Checker.git
cd profile-Rank-Checker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

3. Fill in the form:
   - **Search Keyword**: Enter the keyword/skill (e.g., "Web Developer", "UX Designer")
   - **Profile URL**: Paste your full Upwork profile URL
   - **Max Pages**: Set the maximum number of pages to search (1-1000)

4. Click "Search My Rank" and wait for the results

## Example

**Keyword**: UX designer  
**Profile URL**: https://www.upwork.com/freelancers/~0101b6eacecad1f139  
**Max Pages**: 100

**Result**: Profile found on Page 5 (approximate position 41-50)

## Understanding the Results

- **Page Number**: The search results page where your profile was found
- **Position Range**: Approximate position in the overall search results
  - Each page typically contains ~10 results
  - Position range is calculated as: (page - 1) × 10 + 1 to page × 10

## Important Notes

⚠️ **Rate Limiting**: The app includes a 1-second delay between page requests to avoid overwhelming Upwork's servers and prevent rate limiting.

⚠️ **Search Accuracy**: Results are approximate because:
- Upwork's search results may vary based on location, time, and other factors
- The exact position within a page isn't determined

⚠️ **Performance**: Searching through many pages can take time. For 100 pages, expect ~2-3 minutes.

## Technical Details

### Built With

**PHP/JavaScript Version**:
- **Backend**: PHP with cURL
- **Frontend**: HTML, CSS, JavaScript (Vanilla JS)
- **Web Scraping**: PHP cURL and string search

**Python Version** (Legacy):
- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Web Scraping**: BeautifulSoup4, Requests
- **Parsing**: lxml

### How It Works

1. The app extracts your profile ID from the URL using regex
2. It constructs Upwork search URLs with the provided keyword
3. It iterates through search result pages (starting from page 1)
4. For each page, it fetches the HTML and looks for your profile ID
5. When found, it calculates and returns your approximate position

### Key Features of PHP Version

- **No dependencies**: Pure PHP with built-in cURL
- **Easy deployment**: Works on any PHP hosting (Apache, Nginx, etc.)
- **Cross-origin compatible**: Includes CORS headers for flexibility
- **Rate limiting**: Built-in 1-second delay between requests
- **Error handling**: Comprehensive error logging and user feedback

## Troubleshooting

**Problem**: Profile not found even though it exists  
**Solution**: Try these steps:
- Increase the maximum pages to search
- Try different keyword variations
- Ensure your profile URL is correct
- Check if your profile is public

**Problem**: Search is too slow  
**Solution**: 
- Reduce the maximum pages to search
- The 1-second delay is necessary to avoid rate limiting

**Problem**: Connection errors  
**Solution**:
- Check your internet connection
- Upwork may be temporarily blocking requests
- Try again after a few minutes

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for educational and personal use only. Please use responsibly and in accordance with Upwork's Terms of Service. Excessive automated requests may result in IP blocking or other restrictions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
