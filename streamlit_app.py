import stremlit

API_URL = "https://tomas3254-legalbot.hf.space/api/v1/prediction/b21709c5-f495-4db2-9ca5-9f6129441557"

# use form data to upload files
form_data = {
    "files": ('examplefile', open('examplefile', 'rb'))
}
body_data = {
    "summarizerPromptName": "example",
    "responseLang": "example",
    "maxSummarizedResults": 1,
}

def query(form_data):
    response = requests.post(API_URL, files=form_data, data=body_data)
    return response.json()

output = query(form_data)
