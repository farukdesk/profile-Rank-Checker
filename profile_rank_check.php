<?php
/**
 * Upwork Profile Rank Checker - PHP Version
 * 
 * This script checks the ranking of an Upwork profile for a given keyword search.
 * It replaces the Python Flask implementation with a pure PHP solution.
 */

// Enable error reporting for debugging (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 0);

// Set content type for JSON responses
header('Content-Type: application/json');

// Allow CORS if needed (adjust for production)
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Handle preflight requests
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit();
}

/**
 * Extract profile ID from Upwork profile URL
 * 
 * @param string $profile_url The full Upwork profile URL
 * @return string|null The extracted profile ID or null if not found
 */
function extractProfileId($profile_url) {
    // Profile URL format: https://www.upwork.com/freelancers/~0101b6eacecad1f139
    if (preg_match('/~([a-f0-9]+)/i', $profile_url, $matches)) {
        return $matches[1];
    }
    return null;
}

/**
 * Search for profile on a specific Upwork search results page
 * 
 * @param string $keyword The search keyword
 * @param string $profile_id The profile ID to search for
 * @param int $page_num The page number to search
 * @return bool|null True if found, false if not found, null on error
 */
function searchProfileOnPage($keyword, $profile_id, $page_num) {
    try {
        // Construct search URL
        $search_url = "https://www.upwork.com/nx/search/talent/?nbs=1&q=" . urlencode($keyword) . "&page=" . $page_num;
        
        // Initialize cURL
        $ch = curl_init();
        
        // Set cURL options
        curl_setopt($ch, CURLOPT_URL, $search_url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, 10);
        curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36');
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
        curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
        
        // Execute request
        $response = curl_exec($ch);
        $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        
        // Check for errors
        if (curl_errno($ch)) {
            error_log("cURL error on page $page_num: " . curl_error($ch));
            curl_close($ch);
            return null;
        }
        
        curl_close($ch);
        
        // Check HTTP status code
        if ($http_code !== 200) {
            error_log("HTTP error on page $page_num: Status code $http_code");
            return null;
        }
        
        // Search for profile ID in the response
        // Check if the profile ID appears in the HTML
        if (stripos($response, $profile_id) !== false) {
            return true;
        }
        
        return false;
        
    } catch (Exception $e) {
        error_log("Error searching page $page_num: " . $e->getMessage());
        return null;
    }
}

/**
 * Main search handler
 * 
 * @return array The search results
 */
function handleSearch() {
    // Get POST data
    $input = file_get_contents('php://input');
    $data = json_decode($input, true);
    
    if (json_last_error() !== JSON_ERROR_NONE) {
        return [
            'error' => 'Invalid JSON data',
            'success' => false
        ];
    }
    
    // Extract parameters
    $keyword = isset($data['keyword']) ? trim($data['keyword']) : '';
    $profile_url = isset($data['profile_url']) ? trim($data['profile_url']) : '';
    $max_pages = isset($data['max_pages']) ? intval($data['max_pages']) : 100;
    
    // Validate input
    if (empty($keyword) || empty($profile_url)) {
        return [
            'error' => 'Keyword and profile URL are required',
            'success' => false
        ];
    }
    
    // Extract profile ID from URL
    $profile_id = extractProfileId($profile_url);
    if ($profile_id === null) {
        return [
            'error' => 'Invalid profile URL format',
            'success' => false
        ];
    }
    
    // Limit max pages to 1000
    $max_pages = min($max_pages, 1000);
    
    // Search through pages
    for ($page_num = 1; $page_num <= $max_pages; $page_num++) {
        // Add delay to avoid rate limiting (except for first page)
        if ($page_num > 1) {
            sleep(1); // 1 second delay between requests
        }
        
        $found = searchProfileOnPage($keyword, $profile_id, $page_num);
        
        if ($found === true) {
            // Calculate approximate position
            // Assuming ~10 results per page
            $min_position = ($page_num - 1) * 10 + 1;
            $max_position = $page_num * 10;
            
            return [
                'success' => true,
                'found' => true,
                'page' => $page_num,
                'position_range' => "$min_position-$max_position",
                'message' => "Profile found on page $page_num (approximate position $min_position-$max_position)"
            ];
        }
        
        // Log progress for debugging
        if ($page_num % 10 === 0) {
            error_log("Searched $page_num pages...");
        }
    }
    
    // Profile not found
    return [
        'success' => true,
        'found' => false,
        'message' => "Profile not found in first $max_pages pages"
    ];
}

// Main execution
try {
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $result = handleSearch();
        echo json_encode($result);
    } else {
        // Return error for non-POST requests
        http_response_code(405);
        echo json_encode([
            'error' => 'Method not allowed. Use POST request.',
            'success' => false
        ]);
    }
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode([
        'error' => 'Internal server error: ' . $e->getMessage(),
        'success' => false
    ]);
}
?>
