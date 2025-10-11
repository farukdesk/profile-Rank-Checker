# Upwork Profile Rank Checker

A web application that helps freelancers find their profile ranking on Upwork search results for specific keywords.

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

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/farukdesk/profile-Rank-Checker.git
cd profile-Rank-Checker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to:
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

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Web Scraping**: BeautifulSoup4, Requests
- **Parsing**: lxml

### How It Works

1. The app extracts your profile ID from the URL
2. It constructs Upwork search URLs with the provided keyword
3. It iterates through search result pages (starting from page 1)
4. For each page, it parses the HTML and looks for links containing your profile ID
5. When found, it calculates and returns your approximate position

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
