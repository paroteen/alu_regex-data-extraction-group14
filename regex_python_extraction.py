#!/usr/bin/env python3

import re

# Define the test text with all the data included
Regex_text = """
Emails: user@example.com, firstname.lastname@company.co.uk
URLs: https://user@example.com, http://subdomain.example.org/page
Phone numbers: (123) 456-7890, 123-456-7890, 123.456.7890
Credit card numbers: 1234 5678 9012 3456, 1234-5678-9012-3456
Times: 14:30, 2:30 PM
HTML Tags: <p>, <div class="example">, <img src="image.jpg" alt="description">
Hashtags: #example, #ThisIsAHashtag
Currency amounts: $19.99, $1,234.56
"""

# Define regex patterns
email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
url_pattern = r'https?:\/\/[^\s,<>"]+'
phone_pattern = r'\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}'
credit_card_pattern = r'(?:\d{4}[ -]?){3}\d{4}'
time_pattern = r'(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM))?'
html_tag_pattern = r'<[^>]+>'
hashtag_pattern = r'#\w+'
currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

# Extract using regex patterns
emails = re.findall(email_pattern, Regex_text)
urls = re.findall(url_pattern, Regex_text)
phone_numbers = re.findall(phone_pattern, Regex_text)
credit_cards = re.findall(credit_card_pattern, Regex_text)
times = re.findall(time_pattern, Regex_text)
html_tags = re.findall(html_tag_pattern, Regex_text)
hashtags = re.findall(hashtag_pattern, Regex_text)
currency_amounts = re.findall(currency_pattern, Regex_text)

# Function to print data vertically
def print_vertical(label, items):
    print(f"{label}:")
    for item in sorted(set(items)):  # Remove duplicates and sort
        print(f"  {item}")
    print()  # Blank line for separation

# Print extracted data vertically
print_vertical("Emails", emails)
print_vertical("URLs", urls)
print_vertical("Phone Numbers", phone_numbers)
print_vertical("Credit Card Numbers", credit_cards)
print_vertical("Times", times)
print_vertical("HTML Tags", html_tags)
print_vertical("Hashtags", hashtags)
print_vertical("Currency Amounts", currency_amounts)
