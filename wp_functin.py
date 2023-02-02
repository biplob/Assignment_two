import os
import requests
from dotenv import load_dotenv

def list_html_list(any_list):
    start = '<!-- wp:list --><ul'
    for element in any_list:
        start += f'<!-- wp:list-item --><li>{element}</li><!-- /wp:list-item -->'
    ends = '</ul><!-- /wp:list -->'
    code = start + ends
    return code

#print(list_html_list(['1','2','3']))

def dict_list(dicts):
    start = '<!-- wp:list --><ul>'
    for key, value in dicts.items():
        start += f'<!-- wp:list-item --><li><strong>{key.title()}: {value.title()}</strong></li><!-- /wp:list-item -->'
    ends = '</ul><!-- /wp:list -->'
    codes = start + ends
    return codes

# print(dict_list({'name': 'Michael', 'Age': '40'}))

def headers(username, password):
    import base64
    load_dotenv()
    username = os.getenv('username')
    password = os.getenv('password')
    credential = f'{username}:{password}'
    token = base64.b64encode(credential.encode())
    header = {'Authorization': f'Basic {token.decode("utf-8")}'}
    return header


def imge_url(src, name):
    first_line = '<!-- wp:image {"align":"center","sizeSlug":"large"} -->'
    second_line = f'<figure class="wp-block-image aligncenter size-large"><img src="{src}" alt="{name}"/>'
    third_line = f'<figcaption class="wp-element-caption">{name}</figcaption></figure><!-- /wp:image -->'
    code = f'{first_line}{second_line}{third_line}'
    return code


def wp_h2(text):
    return f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'

def wp_para(text):
    return f'<!-- wp:paragraph --><p>{text}a</p><!-- /wp:paragraph -->'


def openai_text(prompt):
       import os
       import openai
       from dotenv import load_dotenv
       load_dotenv()
       openai.api_key = os.getenv('API_KEY')

       response = openai.Completion.create(
           model="text-davinci-003",
           prompt=prompt,
           temperature=0.7,
           max_tokens=256,
           top_p=1,
           frequency_penalty=0,
           presence_penalty=0
       )
       data = response.get('choices')[0].get('text').strip()
       return data

# print(openai_text('Write a 150 words conclusion about How national digester in bangladesh'))

