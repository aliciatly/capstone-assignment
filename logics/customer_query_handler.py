import os
import json
import openai
from helper_functions import llm
import pandas as pd


# File path
file_path = 'data/ListingofCentres.csv'
file_path_2 = 'data/postalcode.csv'

# Read the CSV file into a DataFrame
childcare_centre = pd.read_csv(file_path)
postal_code =pd.read_csv(file_path_2)

#Transform childcare data
childcare_centre = childcare_centre[childcare_centre['postal_code'] != 0]
childcare_centre['postal_code_format'] = childcare_centre['postal_code'].astype(str).str.zfill(6)
childcare_centre['FirstTwoDigits'] = childcare_centre['postal_code_format'].astype(str).str[:2]
childcare_centre = childcare_centre[childcare_centre.centre_name != 'na']
childcare_centre['centre'] = childcare_centre['centre_name'] + ' ' + childcare_centre['postal_code_format']

#Transform postal_code data
postal_code['Area'] = postal_code['Area'].str.replace('\xa0', ' ')
postal_code['FirstTwoDigits'] = postal_code['Postal Code'].astype(str).str.zfill(2)

resultdf=childcare_centre.merge(postal_code,on="FirstTwoDigits",how='left')

area_centre = resultdf[['Area','centre']]
area_centre = area_centre[area_centre.centre != 'na']
area_centre = area_centre.reset_index(drop=True)
#= area_centre.to_dict('records')
#area_centre=area_centre.set_index('FirstTwoDigits').T.to_dict('list')
#area_dict = area_centre.set_index('Area')['FirstTwoDigits'].to_dict()
#area_dict=dict(zip(area_centre['FirstTwoDigits'], area_centre['Area']))
#area_dict = area_centre.to_json(orient="records")

#transform to json
resultdf = resultdf.drop_duplicates(subset=['centre'])
centre_json_str= resultdf.set_index('centre').T.to_json()
centre_json = json.loads(centre_json_str)
#centre_json = childcare_centre.to_json()


def identify_category_and_courses(user_message):
    input_words = user_message.split()
    area_json=pd.DataFrame()
    for word in input_words:
        area_json = pd.concat([area_json, resultdf[resultdf['Area'].str.contains(word, case=False, na=False)]])
    area_json=area_json.head(5)
    category_and_product_response_str = area_json.to_json(orient="records")
    category_and_product_response = json.loads(category_and_product_response_str)
    category_and_product_response = json.dumps(category_and_product_response, indent=2)
    return category_and_product_response

#TO DEBUG
#def get_course_details(list_of_relevant_category_n_course):
    #course_names_list = []
    #for x in list_of_relevant_category_n_course:
        #value = x.get('centre', 'default_value')
        #course_names_list.append(value)
    #return course_names_list


    #list_of_course_details = []
    #for course_name in course_names_list:
        #list_of_course_details.append(centre_json.get('centre'))
    #return course_names_list
#list_of_course_details


def generate_response_based_on_course_details(user_message, product_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about centre, \
    understand the relevant centre(s) from the following list.
    All available centre shown in the json data below:
    {product_details}

    Step 2:{delimiter} Use the information about the centre to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the centre information.
    Your response should be as detail as possible and \
    include information that is useful for customer to better understand the centre.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision.
    Complete with details such centre, area.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_by_messages(messages)
    response_to_customer = response_to_customer.split(delimiter)[-1]
    return response_to_customer


def process_user_message(user_input):
    delimiter = "```"

    # Process 1: If Courses are found, look them up
    category_n_course_name = identify_category_and_courses(user_input)

    # Process 2: Get the Course Details
    #course_details = get_course_details(category_n_course_name)

    # Process 3: Generate Response based on Course Details
    reply = generate_response_based_on_course_details(user_input, category_n_course_name)


    return reply

