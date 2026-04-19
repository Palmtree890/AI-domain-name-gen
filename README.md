# AI Domain Name Generator

This project is an AI-powered domain name generator that uses the Gemini API to suggest creative and available domain names based on user input.

## Features

- **Interactive Prompts**: Asks the user for a business description and keywords to tailor domain name suggestions.
- **Gemini API Integration**: Leverages the Gemini API for intelligent domain name generation.
- **Environment Variable for API Key**: Securely manages the Gemini API key using environment variables.

## Setup and Installation

Follow these steps to set up and run the AI Domain Name Generator:

### 1. Clone the Repository

If you haven't already, clone this repository to your local machine:

```bash
git clone https://github.com/Palmtree890/AI-domain-name-gen/
cd ai-DNS-gen
```

### 2. Create a Virtual Environment (Recommended)

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate.ps1`
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 4. Set up your Gemini API Key

This project requires a Gemini API key.

1.  **Get your API Key**: Obtain a Gemini API key from the [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  **Create .env file**: Copy the provided example environment file:
    ```bash
    cp .env.example .env
    ```
3.  **Edit .env**: Open the newly created `.env` file and replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key:
    ```
    GEMINI_API_KEY=your_actual_gemini_api_key_here
    ```

### 5. Run the Application

Once everything is set up, you can run the domain name generator:

```bash
python main.py
```

The application will then prompt you to describe your business and provide keywords.

## Usage

1.  Run the script: `python main.py`
2.  When prompted, enter a description of your business or website.
3.  Enter any relevant keywords, separated by commas.
4.  The AI will then suggest a domain name based on your input.

## Project Structure

-   `main.py`: The main application script that handles user interaction and calls the Gemini API.
-   `requirements.txt`: Lists the Python dependencies required for the project.
-   `.env.example`: An example file for setting up environment variables, specifically your Gemini API key.
-   `.gitignore`: Specifies intentionally untracked files to ignore by Git.
```
