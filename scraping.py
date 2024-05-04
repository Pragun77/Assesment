import requests
from bs4 import BeautifulSoup
import re
import openai
from openai import OpenAI
from googleapiclient.discovery import build


SPREADSHEET_ID = '1alCKvTGH_47wJBNnCqY7ALn7Gvq6k6O0M8Pl5a3ygfg'
RANGE_NAME_1 = 'Target Company Data!A1:B47'
RANGE_NAME_2 = 'Prompts!A1:C2'
GOOGLE_API_KEY = 'AIzaSyDDBXC4Lnie2AjkCG0d9-qf5npcoX44xls'
OPENAI_API_KEY = 'Your OpenAI API Key'



def scrape_and_clean(url):
    response = requests.get(url)
    
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        
        main_content = soup.find('div') 

        unwanted_tags = ['header', 'footer', 'aside', 'nav', 'script', 'style']
        for tag in unwanted_tags:
            for element in main_content.find_all(tag):
                element.extract()
        
        cleaned_text = re.sub(r'<[^>]*>', '', main_content.get_text(strip=True))
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        
        return cleaned_text
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return None
    
    
def authenticate_sheets(google_api_key):
    return build('sheets', 'v4', developerKey=google_api_key).spreadsheets()
    
def fetch_data_from_google_sheets(spreadsheet_id , range_name):
    
    sheets = authenticate_sheets(google_api_key=GOOGLE_API_KEY)
    results = sheets.values().get(spreadsheetId =spreadsheet_id, range= range_name).execute()
    values = results.get('values', [])
    
    return values

def OpenAI_Outputs(prompt1):

    openai.api_key = OPENAI_API_KEY
    
    outputs = []

    prompt_1 = prompt1
    
    output_1 = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_1,
        max_tokens=100
    )
    
    prompt_2 = output_1
    
    output_2 = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_2,
        max_tokens=100
    )
    prompt_3 = output_1 + output_2

    output_3 = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_3,
        max_tokens=100
    )
    
    outputs.append(output_1)
    outputs.append(output_2)
    outputs.append(output_3)
    
    return outputs

def create_spreadsheet():
    sheets = authenticate_sheets(google_api_key= GOOGLE_API_KEY)
    spreadsheet = {
        'properties': {
            'title': 'Company Data'
        }
    }
    spreadsheet = sheets.create(body=spreadsheet, fields='spreadsheetId').execute()
    return spreadsheet.get('spreadsheetId')

def update_spreadsheet(values):
    sheets = authenticate_sheets(google_api_key=GOOGLE_API_KEY)
    body = {
        'values': values
    }
    sheets.values().update(
        spreadsheetId=create_spreadsheet(),
        range='Sheet1!A1:F1',
        valueInputOption='RAW',
        body=body
    ).execute()
    

if __name__ == '__main__':
    company_data = fetch_data_from_google_sheets(spreadsheet_id= SPREADSHEET_ID, range_name=RANGE_NAME_1)
    
    values = [['Company Name', 'Company URL', 'Scraped and Formatted Homepage Data', 
               'Output from Prompt 1', 'Output from Prompt 2', 'Output from Prompt 3']]
    
    for i in range(1,len(company_data)):
        
        company_name = company_data[i][0]
        company_url = company_data[1][1]
        scraped_data = scrape_and_clean(company_url)
        prompts_output = OpenAI_Outputs(scraped_data)
        
        values.append([company_name, company_url, scraped_data, 
                       prompts_output[0], prompts_output[1], prompts_output[2]])
        
        update_spreadsheet(values=values)