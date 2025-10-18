# Usage Guide - Upwork Profile Rank Checker

## Quick Start

This application is now available in two versions: **PHP/JavaScript** (recommended for web hosting) and **Python** (for local development).

### Using the PHP/JavaScript Version (Web Hosting)

#### 1. Installation

```bash
# Clone the repository
git clone https://github.com/farukdesk/profile-Rank-Checker.git
cd profile-Rank-Checker

# Upload to your web server
# - Upload index.html (or index.php)
# - Upload profile_rank_check.php
```

#### 2. Access the Application

Simply navigate to your domain in a web browser:
```
https://smartapplypro.com/index.html
# or if using Apache with DirectoryIndex
https://smartapplypro.com/
```

#### 3. Use the Web Interface

1. Fill in the form:
   - **Search Keyword**: Your design/skill keyword (e.g., "UX designer", "Python Developer")
   - **Profile URL**: Your complete Upwork profile URL
   - **Max Pages**: How many pages to search (1-1000, default: 100)
2. Click "Search My Rank"
3. Wait for the results (may take a few minutes depending on the number of pages)

### Using the Python Version (Local Development)

#### 1. Installation

```bash
# Clone the repository
git clone https://github.com/farukdesk/profile-Rank-Checker.git
cd profile-Rank-Checker

# Install dependencies
pip install -r requirements.txt
```

#### 2. Run the Application

```bash
# Start the Flask server
python app.py
```

The application will start on `http://localhost:5000`

#### 3. Use the Web Interface

1. Open your browser and navigate to `http://localhost:5000`
2. Follow the same steps as the PHP version above

## Understanding Your Results

### Result Types

#### ✅ Profile Found
```
Your profile was found on Page 5
Approximate position: 41-50
```
This means your profile appears somewhere between position 41 and 50 in the search results.

#### ⚠️ Not Found
```
Profile not found in first 100 pages
```
Your profile might be ranked lower than the searched pages, or may not appear for that keyword.

#### ❌ Error
```
Invalid profile URL format
```
Check your profile URL and ensure it follows the correct format.

## Tips for Better Results

### 1. Choose Relevant Keywords
- Use keywords that match your profile skills
- Try variations of your main skill (e.g., "UI Designer" vs "UX Designer")
- Use specific keywords rather than generic ones

### 2. Optimize Search Settings
- Start with fewer pages (e.g., 50) for faster results
- Increase page count if not found initially
- Maximum 1000 pages to avoid excessive searching

### 3. Best Practices
- Don't run searches too frequently (wait at least a few minutes between searches)
- Use your exact profile URL from Upwork
- Be patient - searching 100 pages takes ~2-3 minutes

## Profile URL Format

Your Upwork profile URL should look like one of these:

✅ Correct formats:
```
https://www.upwork.com/freelancers/~0101b6eacecad1f139
https://www.upwork.com/freelancers/~abc123def456
https://www.upwork.com/freelancers/~0101b6eacecad1f139?referrer_url_path=/nx/search/talent/
```

❌ Incorrect formats:
```
upwork.com/freelancers/john-doe
www.upwork.com/fl/johndoe
/freelancers/~0101b6eacecad1f139
```

## How the Search Works

1. **Profile ID Extraction**: The app extracts your unique profile ID from the URL (e.g., `~0101b6eacecad1f139`)

2. **Page-by-Page Search**: Starting from page 1, the app:
   - Constructs the Upwork search URL with your keyword
   - Fetches the search results page
   - Looks for your profile ID in the HTML
   - Moves to the next page if not found

3. **Position Calculation**: When found, calculates your approximate position:
   - Each page has ~10 results
   - Page 1 = positions 1-10
   - Page 5 = positions 41-50
   - Page 100 = positions 991-1000

4. **Rate Limiting**: Includes a 1-second delay between requests to avoid overloading Upwork's servers

## Troubleshooting

### PHP Version Issues

### Issue: "Call to undefined function curl_init()"
**Solution**: Enable PHP cURL extension
```bash
# On Ubuntu/Debian
sudo apt-get install php-curl
sudo systemctl restart apache2

# On CentOS/RHEL
sudo yum install php-curl
sudo systemctl restart httpd
```

### Issue: 500 Internal Server Error
**Solution**: Check PHP error logs and ensure proper permissions
```bash
# Check PHP error log
tail -f /var/log/apache2/error.log
# or
tail -f /var/log/php-fpm/error.log

# Set proper permissions
chmod 644 profile_rank_check.php index.html
```

### Issue: CORS errors in browser console
**Solution**: The PHP script includes CORS headers. If still having issues, check server configuration.

### Python Version Issues

### Issue: "Module not found" error
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Search takes too long
**Solution**: 
- Reduce the maximum pages to search
- The 1-second delay is necessary to prevent rate limiting

### Issue: Profile not found but you know it should be there
**Solution**:
- Try different keyword variations
- Increase maximum pages
- Ensure your profile is public and active
- Check that the keyword actually matches your profile skills

### Issue: Connection errors
**Solution**:
- Check your internet connection
- Upwork may be blocking automated requests
- Wait a few minutes and try again
- Use a VPN if necessary

## Example Searches

### Example 1: UX Designer
```
Keyword: UX designer
Profile URL: https://www.upwork.com/freelancers/~0101b6eacecad1f139
Max Pages: 100

Result: Found on Page 5 (Position 41-50)
```

### Example 2: Python Developer
```
Keyword: Python developer
Profile URL: https://www.upwork.com/freelancers/~abc123def456
Max Pages: 50

Result: Found on Page 12 (Position 111-120)
```

### Example 3: Graphic Designer
```
Keyword: Graphic design
Profile URL: https://www.upwork.com/freelancers/~xyz789abc123
Max Pages: 200

Result: Not found in first 200 pages
```

## API Usage (Advanced)

If you want to use the API directly without the web interface:

```bash
curl -X POST http://localhost:5000/search \
  -H "Content-Type: application/json" \
  -d '{
    "keyword": "UX designer",
    "profile_url": "https://www.upwork.com/freelancers/~0101b6eacecad1f139",
    "max_pages": 100
  }'
```

Response:
```json
{
  "success": true,
  "found": true,
  "page": 5,
  "position_range": "41-50",
  "message": "Profile found on page 5 (approximate position 41-50)"
}
```

## Performance Notes

- **Search Speed**: ~1 second per page (due to rate limiting)
- **100 pages**: ~1-2 minutes
- **500 pages**: ~8-10 minutes
- **1000 pages**: ~16-20 minutes

## Privacy & Ethics

⚠️ **Important Notes**:
- This tool is for personal use only
- Respect Upwork's Terms of Service
- Don't abuse the search functionality
- Excessive automated requests may result in IP blocking
- Use responsibly and ethically

## Support

If you encounter issues:
1. Check this guide first
2. Review the README.md
3. Run the test script: `python test_app.py`
4. Open an issue on GitHub with details about your problem

## Contributing

Contributions are welcome! Please see CONTRIBUTING.md for guidelines.
