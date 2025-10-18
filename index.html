<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upwork Profile Rank Checker</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            max-width: 600px;
            width: 100%;
        }

        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 10px;
            font-size: 28px;
        }

        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
            font-size: 14px;
        }

        .form-group {
            margin-bottom: 25px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 600;
            font-size: 14px;
        }

        input[type="text"],
        input[type="number"],
        input[type="url"] {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 14px;
            transition: border-color 0.3s;
        }

        input[type="text"]:focus,
        input[type="number"]:focus,
        input[type="url"]:focus {
            outline: none;
            border-color: #667eea;
        }

        .input-hint {
            font-size: 12px;
            color: #999;
            margin-top: 5px;
        }

        button {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }

        button:hover:not(:disabled) {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }

        button:disabled {
            opacity: 0.6;
            cursor: not-allowed;
        }

        .loading {
            display: none;
            text-align: center;
            margin-top: 20px;
        }

        .spinner {
            border: 3px solid #f3f3f3;
            border-top: 3px solid #667eea;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .result {
            display: none;
            margin-top: 25px;
            padding: 20px;
            border-radius: 8px;
            font-size: 14px;
        }

        .result.success {
            background: #d4edda;
            border: 1px solid #c3e6cb;
            color: #155724;
        }

        .result.error {
            background: #f8d7da;
            border: 1px solid #f5c6cb;
            color: #721c24;
        }

        .result.not-found {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            color: #856404;
        }

        .result-title {
            font-weight: 600;
            font-size: 16px;
            margin-bottom: 10px;
        }

        .result-details {
            line-height: 1.6;
        }

        .result-highlight {
            font-weight: 700;
            color: #667eea;
        }

        .example {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-top: 30px;
            font-size: 12px;
        }

        .example-title {
            font-weight: 600;
            margin-bottom: 8px;
            color: #333;
        }

        .example-text {
            color: #666;
            line-height: 1.5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Upwork Profile Rank Checker</h1>
        <p class="subtitle">Find your profile ranking for any keyword search</p>

        <form id="searchForm">
            <div class="form-group">
                <label for="keyword">Search Keyword</label>
                <input 
                    type="text" 
                    id="keyword" 
                    name="keyword" 
                    placeholder="e.g., UX designer" 
                    required
                >
                <div class="input-hint">Enter the keyword/skill you want to search for</div>
            </div>

            <div class="form-group">
                <label for="profile_url">Your Upwork Profile URL</label>
                <input 
                    type="url" 
                    id="profile_url" 
                    name="profile_url" 
                    placeholder="https://www.upwork.com/freelancers/~0101b6eacecad1f139" 
                    required
                >
                <div class="input-hint">Paste your full Upwork profile URL</div>
            </div>

            <div class="form-group">
                <label for="max_pages">Maximum Pages to Search</label>
                <input 
                    type="number" 
                    id="max_pages" 
                    name="max_pages" 
                    value="100" 
                    min="1" 
                    max="1000"
                >
                <div class="input-hint">Search up to 1000 pages (default: 100)</div>
            </div>

            <button type="submit" id="searchBtn">Search My Rank</button>
        </form>

        <div class="loading" id="loading">
            <div class="spinner"></div>
            <p id="loadingText">Searching...</p>
        </div>

        <div class="result" id="result"></div>

        <div class="example">
            <div class="example-title">How to use:</div>
            <div class="example-text">
                1. Enter your design keyword (e.g., "UX designer")<br>
                2. Paste your Upwork profile URL<br>
                3. Set maximum pages to search (optional)<br>
                4. Click "Search My Rank" to find your position
            </div>
        </div>
    </div>

    <script>
        const form = document.getElementById('searchForm');
        const loading = document.getElementById('loading');
        const result = document.getElementById('result');
        const searchBtn = document.getElementById('searchBtn');
        const loadingText = document.getElementById('loadingText');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const keyword = document.getElementById('keyword').value;
            const profile_url = document.getElementById('profile_url').value;
            const max_pages = document.getElementById('max_pages').value;

            // Show loading
            loading.style.display = 'block';
            result.style.display = 'none';
            searchBtn.disabled = true;
            loadingText.textContent = 'Searching through Upwork pages...';

            try {
                const response = await fetch('profile_rank_check.php', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        keyword: keyword,
                        profile_url: profile_url,
                        max_pages: parseInt(max_pages)
                    })
                });

                const data = await response.json();

                // Hide loading
                loading.style.display = 'none';
                searchBtn.disabled = false;

                // Show result
                result.style.display = 'block';

                if (data.error) {
                    result.className = 'result error';
                    result.innerHTML = `
                        <div class="result-title">❌ Error</div>
                        <div class="result-details">${data.error}</div>
                    `;
                } else if (data.found) {
                    result.className = 'result success';
                    result.innerHTML = `
                        <div class="result-title">✅ Profile Found!</div>
                        <div class="result-details">
                            Your profile was found on <span class="result-highlight">Page ${data.page}</span><br>
                            Approximate position: <span class="result-highlight">${data.position_range}</span><br>
                            <br>
                            This means your profile appears approximately ${data.position_range.split('-')[0]} to ${data.position_range.split('-')[1]} 
                            in the search results for "${keyword}".
                        </div>
                    `;
                } else {
                    result.className = 'result not-found';
                    result.innerHTML = `
                        <div class="result-title">⚠️ Not Found</div>
                        <div class="result-details">
                            ${data.message}<br>
                            <br>
                            Your profile might be ranked lower, or the search parameters need adjustment.
                            Try searching with different keywords or increase the maximum pages.
                        </div>
                    `;
                }

            } catch (error) {
                loading.style.display = 'none';
                searchBtn.disabled = false;
                result.style.display = 'block';
                result.className = 'result error';
                result.innerHTML = `
                    <div class="result-title">❌ Error</div>
                    <div class="result-details">
                        An error occurred while searching. Please try again.<br>
                        Error: ${error.message}
                    </div>
                `;
            }
        });
    </script>
</body>
</html>
