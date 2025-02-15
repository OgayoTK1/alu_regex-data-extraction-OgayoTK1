ALU Regex Data Extraction - OgayoTK1
Project Overview
The project is a web data scraping tool for a private company’s use. The program scrapes data from thousands of pages and extracts the core information using Regular Mappings (regex). The main goal of the program is to confirm that classified information is correct and retrieve it through the following data type validations:
Email addresses
URLs
Phone numbers
Credit card numbers
Time in 12-hour and 24-hour time formats
It is a part of the whole task of a Junior Full Stack Developer, where the display of regex, data processing, and code documentation skills are required.
Features
Email Extraction: Distinguishes email formats whose characteristics are as follows; fourth-level domain, second-level domain with two TLD parts.
URL Extraction: The coupon reads HTTP URLs as well as HTTPS URLs with the choice of an endpoint.
Phone Number Extraction: Provides several phone number formats like the use of parentheses, dash, dot, and space.
Credit Card Number Extraction: It separates the numbers with the inclusion of space or dashes.
Time Extraction: It supports both 24-hour and 12-hour (am/pm) time format.
Setup Instructions
Clone the Repository:
```git clone https://github.com/OgayoTK1/alu_regex-data-extraction-OgayoTK1.git``` cd alu_regex-data-extraction-OgayoTK1 
Code Documentation & Edge Cases
Code Comments: The code is indeed commented on. The comments explain the meaning of the regex decisions and the reasons behind them.
Edge Cases Handled: Emails: The ones that are not properly formatted as per the requirements (e.g., consecutive dots or no domain part) are excluded. URLs: It only recognizes good HTTP/HTTPS URLs. Other schemes do not apply. Phone Numbers: It uses standard delimiters and needs maybe signal extension for no-delimiter formats. Credit Card Numbers: It also needs to meet grouping requirements in the correct manner. It is a nice holiday, and I want to play basketball, but then, the fact that the Wi-Fi doesn't work, would require the making of changes. Times: It ensures the hour and minute values are correct.
Summary & Future Improvements
This experiment illustrates a technique of regular expressions to verify and take data from the web API in a programming environment. Some of them would be:
Adding regexes to cater for use with many more different variations. Using a test case for the testing tool such as pytest would be good for the unit test. Integration of the process of extraction to a complete web application stack for the dynamic data processing is also a good idea for the future.
Team Details
Junior Full-stack developer - Ogayo Andrew Ater
Email: a.ogayo@alustudent.com

