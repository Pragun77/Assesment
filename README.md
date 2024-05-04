# Assesment
Assesment for DoorLabs
# Dependencies
Libraries to install
- python
- requests
- BeautifulSoup
- re
- openai
- googleapiclient

# Setup Instructions
- Install all the Dependencies and clone the repository
  
# Operation Instruction
- Run the the main.py and it will give the desired spreadsheet output

# Main.py
- ## Functions:
    - <u>scrape_and_clean()</u>: The scrape_and_clean function is designed to extract text content from a webpage specified by a given URL and perform cleaning operations to remove unwanted HTML tags and excess white spaces. It begins by sending a GET request to the provided URL and checks if the response status code is 200, indicating a successful retrieval. Upon success, it utilizes the BeautifulSoup library to parse the HTML content and locate the main content within a div tag. It then iterates through a predefined list of unwanted HTML tags, removing elements with those tags from the main content. Subsequently, it employs regular expressions to eliminate any remaining HTML tags and extra white spaces, resulting in a cleaned text. Finally, it returns the cleaned text or, if the retrieval fails, it prints an error message and returns None. This function is valuable for extracting and preparing textual data from webpages for subsequent analysis or processing tasks.
    - <u>authenticate_sheets()</u>: The authenticate_sheets function establishes authentication for accessing Google Sheets API using a provided Google API key. It utilizes the build function from the Google API Client Library to create a service object for Google Sheets API version 4. The function then returns access to spreadsheets within the authenticated service, allowing subsequent operations such as reading, writing, or modifying Google Sheets data.
    - <u>fetch_data_from_google_sheets()</u>: The fetch_data_from_google_sheets function retrieves data from a specified range within a Google Sheets spreadsheet identified by its ID. It first authenticates with Google Sheets using the provided authenticate_sheets function, passing in a Google API key. Then, it utilizes the authenticated service to fetch data from the specified range within the spreadsheet. The function returns the fetched values, if any, as a list of lists, where each inner list represents a row of data from the spreadsheet.
    - <u>OpenAI_Outputs()</u>: The OpenAI_Outputs function leverages OpenAI's text-based model to generate outputs based on a given prompt. It begins by setting up the OpenAI API key and initializing an empty list to store the outputs. The function generates three consecutive outputs: the first based on the initial prompt, the second using the text of the first output as the new prompt, and the third combining the text of the initial prompt with the text of the first two outputs. Each output is generated with a maximum token limit of 100. However, there are minor issues in the code where the prompts for the second and third outputs are incorrectly assigned the output objects themselves rather than their text content, which are corrected to accurately use the text of the outputs.
    - <u>create_spreadsheet()</u>: The create_spreadsheet function facilitates the creation of a new Google Sheets spreadsheet named "Company Data". It first authenticates with Google Sheets using the provided authenticate_sheets function and a Google API key. Then, it defines the properties of the new spreadsheet, setting its title to "Company Data". Subsequently, it utilizes the authenticated service to create the spreadsheet and retrieves its unique identifier (spreadsheet ID). Finally, it returns the spreadsheet ID, allowing further operations on the newly created spreadsheet.
    - <u>update_spreadsheet()</u>: The update_spreadsheet function updates the contents of a Google Sheets spreadsheet with the provided values. It first authenticates with Google Sheets using the provided authenticate_sheets function and a Google API key. Then, it constructs a body containing the values to be updated in the spreadsheet. The function proceeds to execute the update operation on the spreadsheet by calling the values().update method with parameters specifying the spreadsheet ID (obtained from the create_spreadsheet function), the range to update (in this case, cells from A1 to F1 in Sheet1), the input value option as 'RAW', and the body containing the values to be updated.
