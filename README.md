# Django Email Marketing Tool

A comprehensive Django tool designed for managing DNS and IP-related tasks essential for email marketing workflows. This tool can generate and check domain availability, decode email headers, handle IP-to-subnet conversions, and more.

## Features

- **Domain Generation**: Generates purchasable DNS names.
- **Domain Availability Check**: Verifies if domains are available.
- **Random Word Generator**: Useful for unique domain creation.
- **Email Header Decoder**: Simplifies email traceability.
- **IP/Subnet Management**: Converts IPs to subnets, checks reverse IPs.
- **Blacklist Checker**: Validates DNS/IPs against Spamhaus.

## Reason or Motivation

Managing large-scale email campaigns involves understanding and handling DNS and IP issues efficiently.
This tool provides all necessary functionalities to help users maintain high email deliverability and avoid blacklisting by spam filters. By offering easy domain and IP management, it aims to make email marketing workflows seamless and effective.

## Access

The app is hosted at: [https://ehlo.paulcristea.xyz](https://ehlo.paulcristea.xyz) (Heroku).

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: JavaScript, AJAX, Bootstrap
- **Database**: SQLite (default; customizable)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/devraider/django-email-marketing.git
    cd django-email-marketing
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the server:
    ```bash
    python manage.py runserver
    ```
