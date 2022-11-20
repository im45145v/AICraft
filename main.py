import os
import openai
import requests
import cohere
import deso
import var1

co = cohere.Client(var1.coapi)
openai.api_key = var1.dallekey

desoSocial = deso.Social(var1.PUBLIC_KEY, var1.SEED_HEX)
desoMedia = deso.Media(var1.PUBLIC_KEY, var1.SEED_HEX)

a = input("Title\n")
b = input("Audience\n")
c = input("Tone of Voice\n")

response = co.generate(
  model='xlarge',
  prompt=
  'This block will generate an introductory paragraph to a NFT post given a title, audience, and tone of voice.\n--\nTitle: Best Activities in school\nAudience: Millennials\nTone of Voice: Lighthearted\nto run: school with lots of childrean playing in a ground to have lots of fun  and enjoy with teacher\n--\nTitle: pink cat\nAudience: petowners\nTone of Voice: cute\nto run: pink cats with a cute fur are playing in a natural place\n--\nTitle: pink cat\nAudience: pet owners\nTone of Voice: cute\nto run: pink cats with a cute fur are playing in a natural place\n--\nTitle: '
  + a + '\nAudience: ' + b + '\nTone of Voice: ' + c + '\nto run:',
  max_tokens=100,
  temperature=0.8,
  k=0,
  p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=["--"],
  return_likelihoods='NONE')
p = response.generations[0].text
print(p)
response = openai.Image.create(prompt=p, n=1, size="1024x1024")
image_url = response['data'][0]['url']

r = requests.get(image_url)
if r.status_code:
  fp = open('image.png', 'wb')
  fp.write(r.content)
  fp.close()
imageFileList = [('file', ('screenshot.jpg', open("image.png","rb"), 'image/png'))]
x = desoMedia.uploadImage(imageFileList)
y = x.json()
z = y['ImageURL']
q = desoSocial.submitPost(body=p, imageURLs=[z])
