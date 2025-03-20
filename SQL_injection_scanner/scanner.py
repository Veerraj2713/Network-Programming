import requests
from bs4 import BeautifulSoup
import urllib.parse


s = requests.Session()
s.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Safari/537.36"})


#method to get all forms
def get_all_forms(url):
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    return soup.find_all("form")

def form_details(form):
    detailsOfForm = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    detailsOfForm["action"] = action
    detailsOfForm["method"] = method
    detailsOfForm["inputs"] = inputs
    return detailsOfForm

def vulnerable(response):
    errors = {
        "quoted string not properly terminated",
        "unclosed quotation mark after the character string",
        "you have an error in your sql syntax",
    }
    
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False

def scan_sql_injection(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")

    for form in forms:
        details = form_details(form)
        form_action = details['action']
        
        # Handle relative and absolute URLs properly
        if form_action.startswith('http'):
            target_url = form_action
        elif form_action.startswith('//'):
            target_url = 'https:' + form_action
        elif form_action.startswith('/'):
            target_url = urllib.parse.urljoin(url, form_action)
        else:
            target_url = urllib.parse.urljoin(url, form_action)
            
        print(f"\nTesting form with action: {target_url}")

        for i in "\"'":
            data = {}
            for input_tag in details['inputs']:
                if input_tag['name']:  # Only process inputs that have names
                    if input_tag['type'] == "hidden" or input_tag['value']:
                        data[input_tag['name']] = input_tag['value'] + i
                    elif input_tag['type'] != "submit":
                        data[input_tag['name']] = f"test{i}"

            if details["method"] == "post":
                res = s.post(target_url, data=data)
            elif details["method"] == "get":
                res = s.get(target_url, params=data)

            if vulnerable(res):
                print("[+] SQL Injection vulnerability detected, link:", url)
                print("[+] Form:", target_url)
                print("[+] Payload:", data)
                return
        
        print("[-] No SQL Injection vulnerability detected in this form")

if __name__ == "__main__":
    # url = sys.argv[1]
    urlToBeChecked = "https://bekbrace.com"
    scan_sql_injection(urlToBeChecked)
