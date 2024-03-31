import csv
import openai
import os

# Fetch the OpenAI API key from an environment variable
openai.api_key = "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"

# Function to make a generic OpenAI API call
# Function to make a generic OpenAI API call using the chat model
analysis_types = [
        "quality of lectures in their class with 100 being very high and 0 being low, output should be only a number "
        "even it is hard to approximate, just answer as a number, no text just a number",
        "difficulty of workload in their class ranked from 0-100, with 100 being very high and 0 being low, "
        "output should be only a number even it is hard to approximate, just answer as a number, no text just a "
        "number",
        "the difficulty of exams ranked from 0-100, with 100 being very high and 0 being low output should be only a "
        "number even it is hard to approximate, just answer as a number, no text just a number",
        "opportunity to ask questions in their class ranked from 0-100, with 100 being very high and 0 being low "
        "output should be only a number even it is hard to approximate, just answer as a number, no text just a "
        "number",
        "opportunity to ask questions outside of class ranked from 0-100, with 100 being very high and 0 being low "
        "output should be only a number even it is hard to approximate, just answer as a number, no text just a number "
    ]
def make_openai_chat_call(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

def process_data(professor_name, analysis_type):
    prompt = f"Based on professor {professor_name}, what would be the value of {analysis_type}?"
    result = make_openai_chat_call(prompt)
    return result

def process_csv(csv_file_path, professor_column):
    data_from_csv = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_from_csv.append(row)



    for row in data_from_csv:
        professor_name = row[professor_column]
        results = [professor_name]  # Start with professor's name
        for analysis_type in analysis_types:
            result = process_data(professor_name, analysis_type)
            results.append(result)  # Append each result
        # Concatenate and print the results
        results_string = " / ".join(results)
        print(results_string)


def process_single_row(prof_name, prof_reviews):
    # Initially, we're not using prof_reviews directly in this function,
    # but it's prepared for future enhancements where reviews might affect the analysis.

    results = [prof_name]  # Start with the professor's name.
    for analysis_type in analysis_types:
        # For each analysis type, generate a prompt and get the result.
        result = process_data(prof_name, analysis_type)
        results.append(result)  # Append each result to the list.

    # Concatenate and print the results for this professor.
    results_string = " / ".join(results)
    print(results_string)
    return results_string

if __name__ == "__main__":
    csv_file_path = 'Test.csv'
    professor_column = 'Professor_Column'  # Make sure this matches your CSV column name for professors
    process_single_row("Leena Razzaq", "She is a crappy lecturer and she doesn't know how to teach her class, her workload is extremely difficult, "
                                       "and she doesn't answer online pizza out side of class")