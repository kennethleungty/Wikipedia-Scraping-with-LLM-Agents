system_prompt = """
You are a helpful assistant and an expert in all things related to music and songs.
The output must be in a JSON format enclosed in curly brackets, and does not contain any additional details or explanation.

Example:
'genre': 'Disco, Pop',
'label': 'Sony Music',
'language': 'Korean'
'producers': 'Alex Boh, Betty, Germaine',
'songwriters': 'John Johnson, Adam Smith'
"""


def generate_input_prompt(song: str, artist: str) -> str:
    input_prompt = f"""
    This is the song to review:
    - Song title: {song}, performed by {artist}

    Based on the above song information, accurately answer the following questions in order:
    - What is the genre of the song?
    - What is the name of the record label company?
    - What is the main language of the song?
    - Who are the producers of the song?
    - Who are the songwriters of the song?

    If you do not know the answer to any of these questions, return the answer as 'Unknown'. Do not make up any answers.

    Output the above answer strictly in JSON format enclosed with curly brackets. Do not include anything like ```json in the output.
    """

    return input_prompt
