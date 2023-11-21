import requests

url = "https://color-palette-from-image.p.rapidapi.com/url"

payload = {
    "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAASwAAACoCAMAAABt9SM9AAAANlBMVEWy1+nygpv68eIlJkQTPD6z2ugINjsROz8QODnmh5/1gpvtjqD99OX78eL99eoiJD0lJUYkJ0Q2Eid4AAABDklEQVR4nO3QRwGAMAAEsDLLpvg3i4fjwyORkFJy0zym6rJuXWo/+tR53a09Q+jDlSxZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZsmTJkiVLlixZf856AaTS3IBb6qTQAAAAAElFTkSuQmCC",
    "size": 4,
    "variance": 3
}

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "41a3ba0304msh70e39da77886287p15b14ajsn4cf7e9069aff",
    "X-RapidAPI-Host": "color-palette-from-image.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

# Print raw response content
print(response.text)

# Check if response is successful before attempting to parse JSON
if response.ok:
    try:
        # Try to parse JSON if the response is successful
        print(response.json())
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
else:
    print(f"Request failed with status code {response.status_code}")
