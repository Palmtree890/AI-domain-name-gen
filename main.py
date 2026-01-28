import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


# Function to get Gemini API key from environment variables
def get_gemini_api_key():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set.")
    return api_key

# Function to interact with Gemini API
def generate_domain_name(prompt):
    try:
        api_key = get_gemini_api_key()
        genai.configure(api_key=api_key)
        # The genai library automatically picks up the API key from the environment
        # as long as GEMINI_API_KEY or GOOGLE_API_KEY is set.
        # No explicit genai.configure() or api_key parameter in GenerativeModel needed.
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Main function
def main():
    print("AI Domain Name Generator")
    print("------------------------")

    # Gather user input
    business_description = input("Describe your business or website (you can use spaces): ")
    keywords = input("Enter any keywords (comma-separated, you can use spaces): ")

    # Construct prompt for Gemini with a more structured format
    prompt = (
        f"Generate a creative and available domain name for a business or website based on the following information:\n\n"
        f"Business Description: {business_description}\n"
        f"Keywords: {keywords}\n\n"
        f"Please suggest several options."
    )

    # Generate domain name using Gemini
    domain_name = generate_domain_name(prompt)

    # Print the result
    print("\nSuggested Domain Name:")
    print(domain_name)

if __name__ == "__main__":
    main()