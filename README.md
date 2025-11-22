# Mood Music Recommender - SQA Automation Project

A Python-based music recommender that suggests songs based on your mood. This project also demonstrates **Software Quality Assurance (SQA) automation** using **PyTest**, making it ideal to showcase Python and testing skills.

## Features

- Detects user mood: Happy, Sad, or Unknown
- Recommends music playlists based on the detected mood
- Handles invalid or unknown mood input gracefully
- Fully tested with **automated unit tests** using PyTest

## Project Structure

mood_music_sqa/
├── app/
│ └── music_recommender.py # Main Python logic
├── tests/
│ └── test_music.py # PyTest test cases
└── README.md # Project documentation


## Getting Started

### Prerequisites

- Python 3.x
- PyTest (`pip install pytest`)

### Run Tests

1. Open terminal in project root
2. Activate virtual environment if using venv:

venv\Scripts\activate # Windows
source venv/bin/activate # Mac/Linux

3. Run tests:

pytest -v


All tests should pass if set up correctly.

## Example Output

tests/test_music.py::test_detect_happy PASSED
tests/test_music.py::test_detect_sad PASSED
tests/test_music.py::test_unknown_mood PASSED
tests/test_music.py::test_valid_recommendation PASSED
tests/test_music.py::test_invalid_mood_recommendation PASSED


## Tech Stack

- Python 3.x
- PyTest for automated testing

## Why This Project?

This project demonstrates:

- Writing automated test cases
- Using PyTest to validate Python logic
- Handling edge cases and invalid inputs

Perfect for sharing on GitHub and LinkedIn to highlight practical Python and SQA skills.

## Connect

- GitHub: [https://github.com/Shahriersaki/mood-sqa-automation](https://github.com/Shahriersaki/mood-sqa-automation)  
- LinkedIn: [Your LinkedIn Profile Link]
