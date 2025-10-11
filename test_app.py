"""
Test script to demonstrate the Upwork Profile Rank Checker logic
This script simulates the core functionality without requiring a web server
"""

import re

def extract_profile_id(profile_url):
    """Extract the profile ID from Upwork profile URL"""
    # Profile URL format: https://www.upwork.com/freelancers/~0101b6eacecad1f139
    match = re.search(r'~([a-f0-9]+)', profile_url)
    if match:
        return match.group(1)
    return None

def test_profile_extraction():
    """Test profile ID extraction"""
    print("=" * 60)
    print("Testing Profile ID Extraction")
    print("=" * 60)
    
    test_urls = [
        "https://www.upwork.com/freelancers/~0101b6eacecad1f139",
        "https://www.upwork.com/freelancers/~abc123def456",
        "https://www.upwork.com/freelancers/~0101b6eacecad1f139?referrer_url_path=/nx/search/talent/"
    ]
    
    for url in test_urls:
        profile_id = extract_profile_id(url)
        print(f"\nURL: {url}")
        print(f"Extracted ID: {profile_id}")

def test_position_calculation():
    """Test position calculation from page number"""
    print("\n" + "=" * 60)
    print("Testing Position Calculation")
    print("=" * 60)
    
    test_pages = [1, 5, 10, 50, 100, 500, 1000]
    
    for page in test_pages:
        min_position = (page - 1) * 10 + 1
        max_position = page * 10
        print(f"\nPage {page}: Position {min_position}-{max_position}")

def test_search_url_construction():
    """Test search URL construction"""
    print("\n" + "=" * 60)
    print("Testing Search URL Construction")
    print("=" * 60)
    
    test_cases = [
        ("UX designer", 1),
        ("Web Developer", 5),
        ("Python Expert", 100),
    ]
    
    for keyword, page in test_cases:
        search_url = f"https://www.upwork.com/nx/search/talent/?nbs=1&q={keyword.replace(' ', '%20')}&page={page}"
        print(f"\nKeyword: '{keyword}', Page: {page}")
        print(f"URL: {search_url}")

def demonstrate_workflow():
    """Demonstrate the complete workflow"""
    print("\n" + "=" * 60)
    print("Complete Workflow Demonstration")
    print("=" * 60)
    
    # Example input
    keyword = "UX designer"
    profile_url = "https://www.upwork.com/freelancers/~0101b6eacecad1f139"
    max_pages = 100
    found_on_page = 5  # Simulated result
    
    print(f"\nInput:")
    print(f"  Keyword: {keyword}")
    print(f"  Profile URL: {profile_url}")
    print(f"  Max Pages: {max_pages}")
    
    # Extract profile ID
    profile_id = extract_profile_id(profile_url)
    print(f"\nExtracted Profile ID: {profile_id}")
    
    # Simulate search
    print(f"\nSimulating search through pages 1 to {max_pages}...")
    print(f"Profile found on page {found_on_page}!")
    
    # Calculate position
    min_position = (found_on_page - 1) * 10 + 1
    max_position = found_on_page * 10
    
    print(f"\nResult:")
    print(f"  ✅ Profile Found!")
    print(f"  Page: {found_on_page}")
    print(f"  Approximate Position: {min_position}-{max_position}")
    print(f"  Message: Your profile appears approximately {min_position} to {max_position}")
    print(f"           in the search results for '{keyword}'")

if __name__ == "__main__":
    print("\n🔍 Upwork Profile Rank Checker - Test Suite\n")
    
    test_profile_extraction()
    test_position_calculation()
    test_search_url_construction()
    demonstrate_workflow()
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)
    print("\nNote: This is a demonstration of the application logic.")
    print("To run the full application with web interface:")
    print("  1. Install dependencies: pip install -r requirements.txt")
    print("  2. Run the server: python app.py")
    print("  3. Open browser: http://localhost:5000")
    print()
