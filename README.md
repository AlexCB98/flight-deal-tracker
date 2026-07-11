# Flight Deal Tracker

A Python project that searches for real flight deals using SerpAPI.

The program reads destinations from a JSON file, finds the cheapest flights, compares the prices with a target price, and saves good deals.

---

## Features

- Reads destinations from JSON
- Searches real flights with SerpAPI
- Finds the cheapest flight
- Compares prices with a target price
- Saves new deals in JSON
- Prevents duplicate deals
- Uses environment variables for the API key

---

## What I practiced

- APIs
- HTTP requests
- JSON
- OOP
- Environment variables
- Error handling
- Lists and dictionaries
- File handling

---

## Project structure

```
main.py
data_manager.py
flight_search.py
flight_data.py
notification_manager.py
data.json
flight_deals.json
.env
```

---

## How to run

Install the required packages:

```bash
pip install requests python-dotenv
```

Create a `.env` file:

```env
SERP_API_KEY=your_api_key_here
```

Run the project:

```bash
python main.py
```

---

## Technologies used

- Python
- SerpAPI
- Requests
- Python Dotenv
- JSON

---

## Note

This project was created as part of my Python learning journey through Angela Yu’s Udemy course.

---

## Author

Alex — Aspiring Python developer building projects step by step through daily practice, with the long-term goal of becoming a professional software developer.