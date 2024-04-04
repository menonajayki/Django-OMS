from octorest import OctoRest

def main():
    octo_url = "http://octopi.local/"
    octo_apikey = "3342ACFDFCF0460AA0BF4E148A125F3B"
    client = OctoRest(url=octo_url, apikey=octo_apikey)

    file_path = "test.gcode"
    print("Initiating print job...")
    #client.select(file_path, print=True)
    client.upload(file=file_path, select=True, print=True)
    client.start()
    print("Print job started successfully!")

if __name__ == "__main__":
    main()
