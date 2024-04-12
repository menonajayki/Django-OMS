from octorest import OctoRest


def main():
    octo_url = "http://octopi.local/"
    octo_apikey = "3342ACFDFCF0460AA0BF4E148A125F3B"
    client = OctoRest(url=octo_url, apikey=octo_apikey)
    file_path = "red.gcode" # give name of file to be printed

    try:
        """

        print("Toggling the print!")
        client.toggle()
        """

        client.select(file_path)
        client.start()
        print("Print job started successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
