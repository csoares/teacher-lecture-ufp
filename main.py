from bs4 import BeautifulSoup
import requests

# lists
urls = []

# website to be scrape
url = "http://ects.ufp.pt//"
# function created

f = open('informations.csv', 'a')


def scrape(site):
    global url
    currSite = ""

    # getting the request from url
    r = requests.get(site)
    s = BeautifulSoup(r.text, "html.parser")

    course = s.select_one('.E2')
    teacher = s.select_one('.B2E2R2')
    if course and teacher:
        code = site.split("+")
        print(code[1] + " "+code[2] + " " + code[3])
        print("course -" + course.text + " teacher -" + teacher.text)
        f.write(code[1] + ";"+code[2] + ";" + code[3] +
                ";" + course.text+";"+teacher.text+"\n")

    for i in s.find_all("a"):
        href = i.attrs['href']

        if href == "?wcu=P" or href.startswith('?wcu=I'):
            continue

        if href.startswith("/") or href.startswith("?"):
            currSite = url+href

        if currSite != "" and currSite not in urls:
            urls.append(currSite)
            scrape(currSite)


# main function
if __name__ == "__main__":

    # calling function
    scrape(url)
    f.close()
