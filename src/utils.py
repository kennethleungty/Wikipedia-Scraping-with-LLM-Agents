def read_markdown_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."


# Define  callback function to return default values
def default_values(retry_state):
    # Return a set of default values if error occurs
    output = {
        "genre": "Unable to extract",
        "label": "Unable to extract",
        "language": "Unable to extract",
        "producers": "Unable to extract",
        "songwriters": "Unable to extract",
    }

    return output
