import requests
def main():
    print('Search the art instute of chicago!!!')
    artist=input('Enter the name of artist: ')
    try:
        response=requests.get(
            'https://api.artic.edu/api/v1/artworks/search',
            {'q':artist}
            )
#the next line here makes sure our api call was successful if status
#code is within 200 and 299, otherwise if it is 400 or higher, it raises
#an exception to indicate failure
        response.raise_for_status()
    except requests.HTTPError:
        print('couldnt complete request')
        return
    content=response.json()
    for artwork in content["data"]:
        print(f"* {artwork["title"]}")
main()