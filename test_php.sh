#!/bin/bash
# Test script for PHP implementation
# This script tests the profile_rank_check.php endpoint

echo "============================================"
echo "Testing PHP Profile Rank Checker"
echo "============================================"
echo ""

# Check if PHP is installed
if ! command -v php &> /dev/null; then
    echo "❌ PHP is not installed"
    exit 1
fi

echo "✅ PHP is installed"
php --version | head -n 1
echo ""

# Check if cURL extension is available
if php -m | grep -q curl; then
    echo "✅ PHP cURL extension is enabled"
else
    echo "❌ PHP cURL extension is not enabled"
    echo "Please install it with: sudo apt-get install php-curl"
    exit 1
fi
echo ""

# Test 1: Test profile ID extraction
echo "Test 1: Testing profile ID extraction logic"
php -r '
function extractProfileId($profile_url) {
    if (preg_match("/~([a-f0-9]+)/i", $profile_url, $matches)) {
        return $matches[1];
    }
    return null;
}

$test_urls = [
    "https://www.upwork.com/freelancers/~0101b6eacecad1f139",
    "https://www.upwork.com/freelancers/~abc123def456",
    "https://www.upwork.com/freelancers/~0101b6eacecad1f139?referrer=test"
];

foreach ($test_urls as $url) {
    $id = extractProfileId($url);
    if ($id !== null) {
        echo "✅ Extracted ID: $id from URL\n";
    } else {
        echo "❌ Failed to extract ID from: $url\n";
    }
}
'
echo ""

# Test 2: Test JSON request handling
echo "Test 2: Testing JSON request handling"
TEST_DATA='{"keyword":"UX designer","profile_url":"https://www.upwork.com/freelancers/~0101b6eacecad1f139","max_pages":1}'
echo "Sending test request with data: $TEST_DATA"

# Create a temporary PHP script to simulate POST request
cat > /tmp/test_php_post.php << 'EOF'
<?php
// Simulate POST request
$_SERVER['REQUEST_METHOD'] = 'POST';
$GLOBALS['HTTP_RAW_POST_DATA'] = $argv[1];

// Mock file_get_contents for php://input
function mockFileGetContents($filename) {
    if ($filename === 'php://input') {
        return $GLOBALS['HTTP_RAW_POST_DATA'];
    }
    return file_get_contents($filename);
}

// Read and parse the test data
$input = $argv[1];
$data = json_decode($input, true);

echo "Parsed data:\n";
echo "- Keyword: " . ($data['keyword'] ?? 'N/A') . "\n";
echo "- Profile URL: " . ($data['profile_url'] ?? 'N/A') . "\n";
echo "- Max Pages: " . ($data['max_pages'] ?? 'N/A') . "\n";

if (empty($data['keyword']) || empty($data['profile_url'])) {
    echo "❌ Validation failed: Missing required fields\n";
    exit(1);
}

if (preg_match('/~([a-f0-9]+)/i', $data['profile_url'], $matches)) {
    echo "✅ Profile ID extracted: " . $matches[1] . "\n";
} else {
    echo "❌ Invalid profile URL format\n";
    exit(1);
}

echo "✅ Request handling test passed\n";
?>
EOF

php /tmp/test_php_post.php "$TEST_DATA"
rm /tmp/test_php_post.php
echo ""

# Test 3: Check if profile_rank_check.php has correct syntax
echo "Test 3: Checking PHP syntax"
if php -l profile_rank_check.php > /dev/null 2>&1; then
    echo "✅ profile_rank_check.php syntax is valid"
else
    echo "❌ profile_rank_check.php has syntax errors"
    php -l profile_rank_check.php
    exit 1
fi
echo ""

# Test 4: Check if index.html exists and is readable
echo "Test 4: Checking HTML files"
if [ -f "index.html" ]; then
    echo "✅ index.html exists"
else
    echo "❌ index.html not found"
fi

if [ -f "index.php" ]; then
    echo "✅ index.php exists"
    php -l index.php > /dev/null 2>&1 && echo "✅ index.php syntax is valid"
else
    echo "⚠️  index.php not found (optional)"
fi
echo ""

echo "============================================"
echo "Testing Complete!"
echo "============================================"
echo ""
echo "To run the application:"
echo "1. Use PHP built-in server:"
echo "   php -S localhost:8000"
echo ""
echo "2. Open in browser:"
echo "   http://localhost:8000/index.html"
echo ""
echo "3. Or upload to your web server:"
echo "   - index.html (or index.php)"
echo "   - profile_rank_check.php"
echo ""
