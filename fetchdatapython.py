from ipworks import HTTP, IPWorksError
import json

def fetch_data(url, license_string):
    try:
        http = HTTP()
        http.runtime_license = license_string
        http.get(url)
        return http

    except IPWorksError as e:
        print(f"Error fetching data: {e}")
        return None

def main():
    license_string = "31505448415A303331323234333057454254523141310055454154505653454746474E5454484F00303030303030303000003938353434334237444A39550000#IPWORKS#EXPIRING_TRIAL#20240411"
    url = "https://dummyjson.com/products"
    data = fetch_data(url, license_string)

    if data:
        
        response_body = data.transferred_data
        print("Data fetched successfully:\n")
        # print(response_body)

        json_file = json.loads(response_body.decode("utf-8"))
        for product in json_file["products"]:
             print("title: "+product["title"])

if __name__ == "__main__":
    main()
