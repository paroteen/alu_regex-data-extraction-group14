![Regex hackaton](https://i.ytimg.com/vi/GyJtxd14DTc/maxresdefault.jpg)
# Regex Data Extraction Using Python - Group 14

## Project Overview

Welcome to **Regex Data Extraction**, a project created for the **Regex Onboarding Hackathon**. In this project, our team is tasked with developing an API that extracts and displays specific types of data from thousands of web pages. We will leverage the power of **Regular Expressions (Regex)** to parse and retrieve the required information efficiently.

### Prologue

Congratulations! You’ve graduated from your three-year program and are on your way to making a career as a Junior Full Stack Developer. Excitingly, you’ve landed a short-term gig to develop a **Web Application** for a private organization, and you’ve assembled the right team to tackle this task!

The web app will use an API to aggregate data from various web sources and return relevant information based on the user’s request. To extract specific data types from thousands of pages of string responses, we will implement **Regular Expressions** (Regex).

---

## Data Types to Extract

Here are the specific data types our application will extract using regular expressions:

1. **Email Addresses**  
   Examples:  
   - `user@example.com`  
   - `firstname.lastname@company.co.uk`

2. **URLs**  
   Examples:  
   - `https://www.example.com`  
   - `http://subdomain.example.org/page`

3. **Phone Numbers**  
   Examples:  
   - `(123) 456-7890`  
   - `123-456-7890`  
   - `123.456.7890`

4. **Credit Card Numbers**  
   Examples:  
   - `1234 5678 9012 3456`  
   - `1234-5678-9012-3456`

5. **Time Formats**  
   Examples:  
   - `14:30` (24-hour format)  
   - `2:30 PM` (12-hour format)

6. **HTML Tags**  
   Examples:  
   - `<p>`  
   - `<div class="example">`  
   - `<img src="image.jpg" alt="description">`

7. **Hashtags**  
   Examples:  
   - `#example`  
   - `#ThisIsAHashtag`

8. **Currency Amounts**  
   Examples:  
   - `$19.99`  
   - `$1,234.56`

---

## The Task

In this hackathon, we will use regular expressions to efficiently extract data from hundreds of thousands of pages of strings received from our API. The data types listed above will be extracted based on their defined patterns.

### Project Requirements

- Each group will implement solutions for a minimum of **5 out of the 8 challenges** listed above. If all challenges are completed, the remaining three will be considered **bonus challenges**.
- The project will be implemented using Python.
- Each team member must commit code to the project repository at least once.

---

## Team Information

- **Team Name**: Group N
- **GitHub Repository**: [alu_regex-data-extraction-group14](https://github.com/alu_regex-data-extraction-groupN)

---

## Repository Structure

The repository will be structured as follows:

```bash
alu_regex-data-extraction-group14/
│
├── regex/
│   ├── email_extractor.py  
│   ├── url_extractor.py    
│   ├── phone_extractor.py  
│   ├── cc_extractor.py     
│   ├── time_extractor.py   
│   ├── html_extractor.py   
│   ├── hashtag_extractor.py 
│   ├── currency_extractor.py 
│
├── README.md
├── CONTRIBUTING.md
└── tests/
    ├── test_email_extractor.py  
    ├── test_url_extractor.py    
    └── ...
