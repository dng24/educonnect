import csv
import openai

# Fetch the OpenAI API key from an environment variable
with open("openai.key", "r") as f:
    key = f.read().strip()
openai.api_key = key

# Function to make a generic OpenAI API call
# Function to make a generic OpenAI API call using the chat model
analysis_types = [
    "quality of lectures in their class with 100 being very high and 0 being low, output should be only a number "
    "even it is hard to approximate, just answer as a number, no text just a number, there should not be any text in "
    "the output at all",
    "difficulty of workload in their class ranked from 0-100, with 100 being very high and 0 being low, "
    "output should be only a number even it is hard to approximate, just answer as a number, no text just a "
    "number , there should not be any text in "
    "the output at all",
    "the difficulty of exams ranked from 0-100, with 100 being very high and 0 being low output should be only a "
    "number even it is hard to approximate, just answer as a number, no text just a number, there should not be any "
    "text in "
    "the output at all",
    "opportunity to ask questions in their class ranked from 0-100, with 100 being very high and 0 being low "
    "output should be only a number even it is hard to approximate, just answer as a number, no text just a "
    "number , there should not be any text in"
    "the output at all",
    "opportunity to ask questions outside of class ranked from 0-100, with 100 being very high and 0 being low "
    "output should be only a number even it is hard to approximate, just answer as a number, no text just a number, "
    "there should not be any text in "
    "the output at all"
]

strengths_and_weaknesses_prompts = [
    "the strengths this professor has in general, the format should be a single sentence of a description no lists or "
    "new lines",
    "the weaknesses this professor has in general, the format should be a single sentence of a description no lists or "
    "new lines "
]
def make_openai_chat_call(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()


def process_data(professor_name, analysis_type, review):
    prompt = f"Based on professor {professor_name}, and with this data {review}, what would be the value of {analysis_type}?"
    result = make_openai_chat_call(prompt)
    return result

def process_strengths_and_weaknesses(professor_name, strengths_weaknesses, review):
    prompt = f"based of professor {professor_name}, and with this data {review}, what would be a small description of {strengths_weaknesses}?"
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
    results = [prof_name]  # Start with the professor's name.
    for analysis_type in analysis_types:
        # For each analysis type, generate a prompt and get the result.
        result = process_data(prof_name, analysis_type, prof_reviews)
        # Try to cast the result as an integer. If it fails, default to "50".
        try:
            _ = int(result)  # Attempt to cast result to int to check if it's a valid number
        except ValueError:
            result = "50"  # Default to "50" if the result cannot be cast to int
        results.append(result)  # Append each result to the list.

    for strengths_and_weakness in strengths_and_weaknesses_prompts:
        result = process_strengths_and_weaknesses(prof_name, strengths_and_weakness, prof_reviews)
        results.append(result)  # Append each result to the list.

    # Concatenate and print the results for this professor.
    results_string = " / ".join(results)
    print(results_string)
    return results_string



if __name__ == "__main__":
    csv_file_path = 'Test.csv'
    professor_column = 'Professor_Column'  # Make sure this matches your CSV column name for professors
    process_single_row("Rasika Bhallero",
                       "She is a crappy lecturer and she doesn't know how to teach her class, her workload is "
                       "extremely difficult, "
                       "and she doesn't answer online pizza out side of class, "
                       "her class is terrible I would not want to retake it again,"
                       "I loved her as a lectuere,"
                       "She doesn't respond to her emails,"
                       "She does not like teaching")

    process_single_row("Leena Razzaq",
                       "She is a crappy lecturer and she doesn't know how to teach her class, her workload is "
                       "extremely difficult, ")

    process_single_row("Ben Lerner", "he has a small workload")


