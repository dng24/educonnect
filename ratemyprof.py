import csv
import requests
from bs4 import BeautifulSoup

def query_rmp(first_name, last_name):
    search_url = "https://www.ratemyprofessors.com/search/professors/696?q=%s+%s" % (first_name, last_name)

    resp = requests.get(search_url)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        scripts = soup.find_all("script")
        
        for s in scripts:
            stuff = str(s)
            if "window.__RELAY_STORE__" in stuff:
                i = stuff.find("legacyId")
                end = stuff.index(",", i)
                prof_id = stuff[i + 10:end]
                break
    else:
        return None


    prof_url = "https://www.ratemyprofessors.com/professor/" + prof_id

    resp = requests.get(prof_url)
    print(prof_url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        comments = soup.find_all(class_=lambda x: x and 'Comments' in x)
        stripped_comments = [comment.text.strip() for comment in comments]
        out_comments = ",".join(stripped_comments)
        return out_comments
    else:
        return None


def get_reviews(names):
    outputs = [["Professor_Column", "Results"]]
    for name in names:
        name_arr = name.split(", ")
        first_name = name_arr[1]
        last_name = name_arr[0]
        reviews = query_rmp(first_name, last_name)
        output = [first_name + " " + last_name, reviews]
        outputs.append(output)

    return outputs

def main():
    with open("names.txt", "r") as f:
        names = f.read().split("\n")

    outputs = get_reviews(names)
    with open("reviews.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for prof in outputs:
            writer.writerow(prof)


if __name__ == "__main__":
    get_reviews()
