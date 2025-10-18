# Deployment Guide - PHP/JavaScript Version

This guide shows how to deploy the Upwork Profile Rank Checker on your domain (e.g., smartapplypro.com).

## Prerequisites

- A web hosting account with PHP support (version 7.4 or higher)
- PHP cURL extension enabled
- FTP/SFTP access or cPanel file manager
- Your domain configured to point to your hosting

## Files to Deploy

You need to upload these files to your web server:

1. **index.html** - The main HTML interface
2. **profile_rank_check.php** - The backend PHP script that handles search requests

Optional:
- **index.php** - Alternative to index.html (same content, can be used as DirectoryIndex)

## Deployment Steps

### Option 1: Deploy to Root Directory

If you want the rank checker to be your main application:

1. **Upload files to your web root** (typically `public_html/` or `www/`):
   ```
   public_html/
   ├── index.html
   └── profile_rank_check.php
   ```

2. **Access via your domain**:
   ```
   https://smartapplypro.com/
   ```

### Option 2: Deploy to Subdirectory (Recommended)

If you want the rank checker as an option on your site:

1. **Create a subdirectory** in your web root:
   ```bash
   mkdir public_html/rank-checker
   ```

2. **Upload files to the subdirectory**:
   ```
   public_html/
   └── rank-checker/
       ├── index.html
       └── profile_rank_check.php
   ```

3. **Access via subdirectory**:
   ```
   https://smartapplypro.com/rank-checker/
   ```

### Option 3: Deploy as a Direct PHP File

Based on your requirement to access it like `https://smartapplypro.com/profile_rank_check.php`:

1. **Create a standalone page** by copying `index.php` content into `profile_rank_check_page.php`:
   - Rename or create a file that includes both the interface and functionality

2. **Upload to web root**:
   ```
   public_html/
   ├── profile_rank_check.php (API endpoint)
   └── profile_rank_check_page.php (Full page with interface)
   ```

3. **Access directly**:
   ```
   https://smartapplypro.com/profile_rank_check_page.php
   ```

## Step-by-Step Deployment Instructions

### Using FTP/SFTP

1. **Connect to your server** using an FTP client (FileZilla, WinSCP, etc.):
   - Host: your-server.com
   - Username: your-username
   - Password: your-password

2. **Navigate to your web root** (usually `public_html/` or `www/`)

3. **Upload files**:
   - Upload `index.html`
   - Upload `profile_rank_check.php`

4. **Set permissions** (usually 644 is fine):
   ```bash
   chmod 644 index.html
   chmod 644 profile_rank_check.php
   ```

### Using cPanel File Manager

1. **Log in to cPanel**

2. **Open File Manager**

3. **Navigate to public_html/**

4. **Click Upload** and select your files:
   - index.html
   - profile_rank_check.php

5. **Files will automatically have correct permissions**

### Using Command Line (SSH)

If you have SSH access:

```bash
# Connect to your server
ssh username@smartapplypro.com

# Navigate to web root
cd public_html

# Upload files using scp from your local machine (run this on your local machine)
scp index.html username@smartapplypro.com:~/public_html/
scp profile_rank_check.php username@smartapplypro.com:~/public_html/

# Or clone directly on server
git clone https://github.com/farukdesk/profile-Rank-Checker.git
cp profile-Rank-Checker/index.html .
cp profile-Rank-Checker/profile_rank_check.php .

# Set permissions
chmod 644 index.html profile_rank_check.php
```

## Verification

After deployment, verify everything works:

1. **Check PHP version**:
   Create a file `phpinfo.php`:
   ```php
   <?php phpinfo(); ?>
   ```
   Visit: `https://smartapplypro.com/phpinfo.php`
   (Delete this file after checking!)

2. **Check cURL extension**:
   In the phpinfo page, search for "curl" - it should show "enabled"

3. **Test the application**:
   - Visit `https://smartapplypro.com/index.html`
   - Fill in a test search
   - Verify it works correctly

4. **Check for errors**:
   If something doesn't work, check error logs:
   - cPanel: Error Logs section
   - Command line: `/var/log/apache2/error.log` or `/var/log/nginx/error.log`

## Configuration Options

### Adjusting Rate Limiting

If you want to change the delay between requests, edit `profile_rank_check.php`:

```php
// Line ~150: Change from 1 second to your preferred delay
sleep(1); // Change to sleep(2) for 2 seconds, etc.
```

### Enabling Error Reporting (Development Only)

For debugging during setup, temporarily enable error display in `profile_rank_check.php`:

```php
// Line ~10: Change to:
ini_set('display_errors', 1);
```

**Important**: Disable this in production!

### CORS Configuration

If you need to restrict CORS, edit `profile_rank_check.php`:

```php
// Line ~15: Change from:
header('Access-Control-Allow-Origin: *');

// To specific domain:
header('Access-Control-Allow-Origin: https://smartapplypro.com');
```

## Common Issues and Solutions

### Issue: "500 Internal Server Error"

**Causes**:
- PHP syntax error
- Wrong file permissions
- Missing PHP cURL extension

**Solutions**:
```bash
# Check PHP syntax
php -l profile_rank_check.php

# Fix permissions
chmod 644 profile_rank_check.php

# Check if cURL is installed
php -m | grep curl
```

### Issue: "Call to undefined function curl_init()"

**Solution**: Install PHP cURL extension

```bash
# Ubuntu/Debian
sudo apt-get install php-curl
sudo systemctl restart apache2

# CentOS/RHEL
sudo yum install php-curl
sudo systemctl restart httpd

# Or contact your hosting provider to enable it
```

### Issue: "404 Not Found"

**Solution**: Ensure files are in the correct directory and web server is configured properly.

### Issue: CORS Errors

**Solution**: Check that `profile_rank_check.php` includes proper CORS headers (already included in the script).

## Security Best Practices

1. **Don't expose error details** in production:
   ```php
   ini_set('display_errors', 0);
   ```

2. **Use HTTPS** - Ensure your domain uses SSL certificate

3. **Rate limiting** - The script includes 1-second delays, don't reduce this

4. **Monitor usage** - Keep an eye on server logs for unusual activity

5. **Regular updates** - Keep PHP and server software updated

## Performance Optimization

1. **Enable PHP OPcache** (usually enabled by default)

2. **Use PHP 8.x** for better performance

3. **Consider caching** for repeated searches (advanced)

4. **Monitor resource usage** - Searching can be resource-intensive

## Integration with Your Website

### Adding to Existing Site

To integrate into an existing website:

1. **Create a menu link**:
   ```html
   <a href="/rank-checker/">Profile Rank Checker</a>
   ```

2. **Or embed in a page**:
   ```html
   <iframe src="/rank-checker/index.html" width="100%" height="800px"></iframe>
   ```

3. **Or use as a popup/modal** with JavaScript

## Support

If you encounter issues:

1. Check this deployment guide
2. Review error logs on your server
3. Test PHP functionality with phpinfo()
4. Ensure cURL is enabled
5. Open an issue on GitHub: https://github.com/farukdesk/profile-Rank-Checker/issues

## Next Steps

After successful deployment:

1. Test the application with real searches
2. Monitor performance and adjust rate limiting if needed
3. Consider adding analytics to track usage
4. Customize the design to match your website branding

## Backup

Always keep a backup of your files:

```bash
# Create backup
tar -czf rank-checker-backup-$(date +%Y%m%d).tar.gz index.html profile_rank_check.php
```

## License

This project is open source under the MIT License. Use it freely on your domain!
