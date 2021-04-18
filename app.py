from helper import pets
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>

  <p> Browse through the links below to find your new furry friend </p1>

  <ul>
  <li><a href='/animals/dogs'>Dogs</a> </li>
  <li><a href='/animals/cats'>Cats</a></li>
  <li><a href='/animals/rabbits'>Rabbits</a></li>
  </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type} </h1>'
  html += '<ul>'
  for x, idx in enumerate(pets[pet_type]):
    html += '<li>'
    #html += f'{x}'
    idx = x
    html += f'<a href= "/animals/{pet_type}/{idx}">name</a>'
    html += '</li>'
  html += '</ul>'
  return html
  

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
 pet = pets[pet_type]
 pet_name = pet[pet_id]['name']
 h1_pet_name = '<h1>{}</h1>'.format(pet_name)
 # pet = pets[pet_type]
 in_pet = pet[pet_id]
 pet_desc=pet[pet_id]['description']
 pet_b = pet[pet_id]['breed']
 pet_a = pet[pet_id]['age']
 pet_url=pet[pet_id]['url']

 img_pet_url='<img src= "{}"/>'.format(pet_url)

 li_pet_ba = '<ul><li>breed: {}</li><li>age: {}</li></ul>'.format(pet_b, pet_a)
 p1_pet_desc = '<p1>{}</p1>'.format(pet_desc)
 #img_url = pet[pet_id]['url']
 #<img src="https://www.google.com/"/>

 return str(h1_pet_name)  + str(pet_desc) + str(li_pet_ba)  + str(img_pet_url)




