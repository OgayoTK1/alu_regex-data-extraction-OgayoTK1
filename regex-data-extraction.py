#!/usr/bin/env python3

import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern = r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/\S*)?'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    return re.findall(pattern, text)

def extract_credit_cards(text):
    pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
    return re.findall(pattern, text)

def extract_time(text):
    pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d\b|\b(?:1[0-2]|0?[1-9]):[0-5]\d (?:AM|PM)\b'
    return re.findall(pattern, text)

def extract_html_tags(text):
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r'#[a-zA-Z0-9_]+'
    return re.findall(pattern, text)

def extract_currency(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)

# Sample text for testing
sample_text = """
    Contact us at aterogayo@gmail.com or visit https://www.aterogayo@gmail.com for details.
    Call (123) 456-7890 or 123-456-7890.
    Your credit card number is 1234-5678-9012-3456.
    The event starts at 14:30 or 2:30 PM.
    <div class="content">Welcome</div>
    #Regex #Python
    The price is $1,234.56.
"""

# Testing the functions
print("Emails:", extract_emails(sample_text))
print("URLs:", extract_urls(sample_text))
print("Phone Numbers:", extract_phone_numbers(sample_text))
print("Credit Cards:", extract_credit_cards(sample_text))
print("Time:", extract_time(sample_text))
print("HTML Tags:", extract_html_tags(sample_text))
print("Hashtags:", extract_hashtags(sample_text))
print("Currency:", extract_currency(sample_text))

