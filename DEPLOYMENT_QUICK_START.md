# Quick Start Guide - Deploy to smartapplypro.com

## 🚀 For Your Domain: smartapplypro.com

This is a **5-minute deployment guide** to get the Profile Rank Checker running on your domain.

## What You're Getting

A fully functional Upwork Profile Rank Checker that:
- ✅ Works on any PHP hosting (no Python needed)
- ✅ Uses JavaScript and PHP (as requested)
- ✅ Can be accessed at: `https://smartapplypro.com/profile_rank_check.html`
- ✅ No database required
- ✅ No dependencies to install

## The 2 Files You Need

```
📄 index.html           (11KB) - The user interface
📄 profile_rank_check.php (6KB)  - The backend API
```

That's it! Just 2 files, 17KB total.

## Upload Methods

### Method A: cPanel (Easiest)

1. **Log in to cPanel**
2. **Click "File Manager"**
3. **Go to `public_html/`**
4. **Click "Upload"**
5. **Select these 2 files:**
   - `index.html`
   - `profile_rank_check.php`
6. **Done!** Visit: `https://smartapplypro.com/index.html`

### Method B: FTP (FileZilla)

1. **Connect to your server** with FileZilla
2. **Navigate to `public_html/`**
3. **Drag and drop:**
   - `index.html`
   - `profile_rank_check.php`
4. **Done!** Visit: `https://smartapplypro.com/index.html`

### Method C: Command Line (SSH)

```bash
# 1. Connect to your server
ssh user@smartapplypro.com

# 2. Go to web root
cd public_html

# 3. Download files from GitHub
wget https://raw.githubusercontent.com/farukdesk/profile-Rank-Checker/main/index.html
wget https://raw.githubusercontent.com/farukdesk/profile-Rank-Checker/main/profile_rank_check.php

# 4. Set permissions
chmod 644 index.html profile_rank_check.php

# Done!
```

## Access URLs

After uploading, you can access the rank checker at:

- **Option 1**: `https://smartapplypro.com/index.html`
- **Option 2**: Rename `index.html` to `profile_rank_check.html`
  - Then access: `https://smartapplypro.com/profile_rank_check.html`

## Verify It's Working

### Quick Test

1. Visit: `https://smartapplypro.com/index.html`
2. Fill in the form:
   - **Keyword**: "test"
   - **Profile URL**: `https://www.upwork.com/freelancers/~0101b6eacecad1f139`
   - **Max Pages**: 1
3. Click "Search My Rank"
4. Should see result: "Not Found" (expected for test data)

If you see the result, **it's working! ✅**

## Customization (Optional)

### Rename for Your Preferred URL

Want to access it as `profile_rank_check.php`? Here's how:

1. **Rename `index.html` to `profile_rank_check.html`**
2. Access: `https://smartapplypro.com/profile_rank_check.html`

Or, create a subdirectory:

```
public_html/
└── rank-checker/
    ├── index.html
    └── profile_rank_check.php
```

Access: `https://smartapplypro.com/rank-checker/`

### Add to Your Website Menu

Add a link in your navigation:

```html
<a href="/index.html">Check Profile Rank</a>
```

Or:

```html
<a href="/profile_rank_check.html">Rank Checker</a>
```

## Troubleshooting

### Problem: Can't access the page

**Check:**
1. Files are in `public_html/` (or your web root)
2. Files have correct permissions: `chmod 644 *.html *.php`
3. Your domain is properly configured

### Problem: Page loads but search doesn't work

**Solution:**
1. Check if PHP cURL is enabled:
   - Create `test.php`: `<?php phpinfo(); ?>`
   - Search for "curl" → should show "enabled"
2. Ensure both files are in the same directory
3. Check browser console (F12) for JavaScript errors

### Problem: "500 Internal Server Error"

**Solution:**
1. Check PHP version: Must be 7.4+
2. Check error logs in cPanel
3. Verify PHP syntax: `php -l profile_rank_check.php`

## Requirements

Your hosting must have:
- ✅ PHP 7.4 or higher (most hosting has 8.x)
- ✅ PHP cURL extension (usually enabled by default)
- ✅ Web server (Apache/Nginx)

**99% of web hosting providers meet these requirements.**

## What It Does

1. User enters their Upwork profile URL and keyword
2. JavaScript sends request to PHP script
3. PHP searches Upwork pages for the profile
4. Results displayed to user
5. No data stored - completely stateless

## Features

- 🔍 Search up to 1000 pages
- 📊 Get approximate ranking position
- 💫 Beautiful, responsive interface
- ⚡ Fast and efficient
- 🔒 Secure with input validation
- 📱 Works on mobile and desktop

## Tech Stack (As Requested)

- **Frontend**: HTML, CSS, JavaScript (Vanilla JS)
- **Backend**: PHP with cURL
- **No Python** - Pure PHP/JavaScript implementation

## File Structure

```
smartapplypro.com/
├── index.html                 ← User interface
├── profile_rank_check.php     ← Backend API
└── (your other files...)
```

## Support

- **Full Documentation**: See `DEPLOYMENT.md`
- **PHP Guide**: See `README_PHP.md`
- **Usage Guide**: See `USAGE.md`
- **GitHub Issues**: https://github.com/farukdesk/profile-Rank-Checker/issues

## Screenshots

### Interface
![Rank Checker Interface](https://github.com/user-attachments/assets/8303032a-533d-40c8-b201-efe669b1262a)

### Search Results
![Search Results](https://github.com/user-attachments/assets/e8079ef8-67cd-4c28-9704-b79c3799a05d)

## That's It! 🎉

Just upload 2 files and you're done. No complex setup, no dependencies, no configuration files.

**Ready to deploy?** Grab the files and upload them now!

---

**Questions?** Open an issue on GitHub or check the detailed guides:
- `DEPLOYMENT.md` - Complete deployment instructions
- `README_PHP.md` - PHP version documentation
- `USAGE.md` - How to use the application
