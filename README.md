# FilGoal Web Scraper

A web scraping tool for extracting football matches details for a specific day from the FilGoal website, filtered by a specified date, using Python and BeautifulSoup.

## Features

- Allows the user to input a specific date (in `YYYY-MM-DD` format) to retrieve match details.
- Extracts match data, including:
  - Championship name
  - Match date
  - Team names
  - Match score
  - Match status
- Saves the extracted data in a CSV file.

## Prerequisites

Before running the script, ensure you have the following Python packages installed:

- `requests`
- `beautifulsoup4`
- `csv`
You can install these packages using the following command:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/KhaledEkramy/Filgoal-Data-Scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Filgoal-Data-Scraper
   ```

3. Run the script:

   ```bash
   python3 filgoal_scraping.py
   ```

4. Enter the match date in `YYYY-MM-DD` format when prompted.

5. Provide the location where you want to save the CSV file.

## Code Overview

The script performs the following steps:

1. **Date Validation:** Checks if the entered date is in the correct `YYYY-MM-DD` format.
2. **Web Scraping:** Uses `requests` and `BeautifulSoup` to fetch the match details from the FilGoal website.
3. **Data Extraction:** Extracts details such as championship name, teams, scores, and match status.
4. **Data Storage:** Saves the extracted match details in a CSV file at the specified location.

## Example

```bash
Enter matches day in the following format: YYYY-MM-DD   2024-10-23
The date format is correct.
Enter location where you wanna save the file: /path/to/save/location/
```

This will create a CSV file named `2024-10-23_matches.csv` in the specified directory.
## Output Example
![image](https://github.com/user-attachments/assets/49da2795-0365-4ee1-b95a-5d24ac5b8ce8)

## File Structure

- `scraper.py`: The main script for web scraping.
- `README.md`: Documentation for the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
