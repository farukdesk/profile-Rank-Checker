# Upwork Profile Rank Checker - PHP/JavaScript Version

## Quick Start for smartapplypro.com

This is the PHP/JavaScript version specifically designed for easy deployment on standard web hosting platforms.

### What You Need

1. PHP 7.4+ with cURL extension
2. Web server (Apache/Nginx)
3. Your domain (e.g., smartapplypro.com)

### Files to Upload

Upload these 2 files to your web server:

```
📁 public_html/
├── 📄 index.html          ← Main interface
└── 📄 profile_rank_check.php  ← Backend API
```

### Access URL Options

After uploading, you can access the rank checker at:

- **Option 1**: `https://smartapplypro.com/` (if index.html is in root)
- **Option 2**: `https://smartapplypro.com/index.html`
- **Option 3**: `https://smartapplypro.com/rank-checker/` (if in subdirectory)

## Installation Methods

### Method 1: FTP Upload (Easiest)

1. Open your FTP client (FileZilla, etc.)
2. Connect to your server
3. Navigate to `public_html/`
4. Upload:
   - `index.html`
   - `profile_rank_check.php`
5. Done! Visit your domain in a browser

### Method 2: cPanel File Manager

1. Log in to cPanel
2. Open "File Manager"
3. Go to `public_html/`
4. Click "Upload"
5. Select and upload:
   - `index.html`
   - `profile_rank_check.php`
6. Done! Visit your domain in a browser

### Method 3: Command Line (SSH)

```bash
# Connect to your server
ssh user@smartapplypro.com

# Go to web root
cd public_html

# Upload files (from local machine)
scp index.html user@smartapplypro.com:~/public_html/
scp profile_rank_check.php user@smartapplypro.com:~/public_html/

# Or clone from GitHub
git clone https://github.com/farukdesk/profile-Rank-Checker.git temp
cp temp/index.html .
cp temp/profile_rank_check.php .
rm -rf temp

# Set permissions
chmod 644 index.html profile_rank_check.php
```

## Verify Installation

### 1. Check PHP Version

Create a file `test.php`:
```php
<?php
echo "PHP Version: " . phpversion() . "\n";
echo "cURL: " . (function_exists('curl_init') ? 'Enabled' : 'Disabled');
?>
```

Visit: `https://smartapplypro.com/test.php`

You should see:
- PHP Version: 7.4 or higher ✅
- cURL: Enabled ✅

Delete `test.php` after checking.

### 2. Test the Application

1. Visit: `https://smartapplypro.com/index.html`
2. You should see the profile rank checker interface
3. Try a test search with:
   - Keyword: "test"
   - Profile URL: `https://www.upwork.com/freelancers/~0101b6eacecad1f139`
   - Max Pages: 1
4. It should return a result (found or not found)

## Directory Structure Examples

### Example 1: Root Directory
```
public_html/
├── index.html                 ← Main page
├── profile_rank_check.php     ← API endpoint
└── (your other site files...)
```
Access: `https://smartapplypro.com/`

### Example 2: Subdirectory (Recommended)
```
public_html/
├── index.html (your main site)
└── rank-checker/
    ├── index.html                ← Rank checker interface
    └── profile_rank_check.php    ← API endpoint
```
Access: `https://smartapplypro.com/rank-checker/`

### Example 3: As a Direct File
```
public_html/
├── profile_rank_check.html       ← Renamed index.html
└── profile_rank_check.php        ← API endpoint
```
Access: `https://smartapplypro.com/profile_rank_check.html`

## Features

✅ **No database required** - Everything runs server-side, no setup needed

✅ **No dependencies** - Pure PHP with built-in functions only

✅ **Mobile responsive** - Works on all devices

✅ **Fast and efficient** - Includes rate limiting to avoid server overload

✅ **Secure** - Input validation and error handling built-in

## How It Works

1. User enters keyword and Upwork profile URL
2. JavaScript sends request to `profile_rank_check.php`
3. PHP script searches Upwork pages for the profile
4. Results are returned and displayed
5. No data is stored - completely stateless

## Configuration (Optional)

### Change Rate Limiting

Edit `profile_rank_check.php`, line ~150:
```php
sleep(1); // Change to sleep(2) for 2 seconds between requests
```

### Customize Design

Edit `index.html` to change:
- Colors (search for `#667eea` and `#764ba2`)
- Text and labels
- Layout and styling

### Add to Existing Site

Add a link in your navigation:
```html
<a href="/rank-checker/">Check Your Rank</a>
```

Or embed in a page:
```html
<iframe src="/rank-checker/index.html" width="100%" height="800px"></iframe>
```

## Troubleshooting

### Problem: "500 Internal Server Error"

**Solution:**
```bash
# Check PHP error log
# Location varies by server, common locations:
tail -f /var/log/apache2/error.log
tail -f /var/log/nginx/error.log

# Or check in cPanel: Error Logs section
```

### Problem: "Call to undefined function curl_init"

**Solution:** Contact your hosting provider to enable PHP cURL extension.

For VPS/dedicated servers:
```bash
# Ubuntu/Debian
sudo apt-get install php-curl
sudo systemctl restart apache2

# CentOS/RHEL
sudo yum install php-curl
sudo systemctl restart httpd
```

### Problem: Page loads but search doesn't work

**Solutions:**
1. Check browser console for JavaScript errors (F12)
2. Ensure `profile_rank_check.php` is in the same directory as `index.html`
3. Check file permissions: `chmod 644 profile_rank_check.php`
4. Verify PHP is working: Create `test.php` with `<?php phpinfo(); ?>`

### Problem: "CORS policy" error

**Solution:** Already handled in `profile_rank_check.php`. If still occurring:
- Ensure both files are on the same domain
- Check server logs for additional errors

## Performance Notes

- Each search can take 1-10 minutes depending on max pages
- Uses 1-second delay between requests (required)
- Minimal server resources needed
- No database queries = fast and efficient

## Security

The application includes:
- ✅ Input validation
- ✅ SQL injection protection (no database used)
- ✅ XSS protection
- ✅ Rate limiting
- ✅ Error handling without exposing sensitive info

## Support

- **Documentation**: See `DEPLOYMENT.md` for detailed setup
- **Issues**: https://github.com/farukdesk/profile-Rank-Checker/issues
- **Python Version**: Available in `app.py` for local development

## Testing Locally

Want to test before deploying?

```bash
# 1. Make sure PHP is installed
php --version

# 2. Start PHP built-in server
cd /path/to/files
php -S localhost:8000

# 3. Open browser
# Visit: http://localhost:8000/index.html
```

## File Sizes

- `index.html`: ~10KB
- `profile_rank_check.php`: ~6KB
- **Total**: ~16KB (very lightweight!)

## Browser Compatibility

Works in all modern browsers:
- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Mobile browsers

## License

MIT License - Free to use for personal and commercial projects

## Credits

Original Python version by farukdesk
PHP/JavaScript version for web hosting deployment

---

**Ready to deploy?** Just upload the 2 files and you're done! 🚀

For detailed deployment instructions, see `DEPLOYMENT.md`
