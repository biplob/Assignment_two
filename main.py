# import all necessary liberies
from requests import post
import wp_funcs as wp


# extracting keyword from file
with open('keywords.txt', 'r+') as file:
    lines = file.readlines()


for line in lines:
      # Contents of word press post
      keyword = line.strip("\n").replace("best", "")
      title = f'Buying guid for {keyword}'.title()
      slug = title.replace(" ", "-").lower()


      # intro
      intro_heading = wp.wp_h2('Introduction')
      intro_text = wp.openai_text(f'Write a short description about {keyword}').strip().strip("\n")
      intro = intro_heading + wp.wp_para(intro_text)


      # Point 1
      text = f'Why {keyword} is important'
      p1_heading = wp.wp_h2(text)
      p1_text = wp.openai_text(text)
      point_1 = p1_heading + wp.wp_para(p1_text)


      # Point 2
      text = f'How to choose the {line}? Write 4 lines.'
      p2_heading = wp.wp_h2(f'How to choose the {line}')
      p2_text = wp.openai_text(text).strip()
      point_2 = p2_heading + wp.wp_para(p2_text)


      # Point 3

      text = f'what features should be considered while buying a {keyword}? write 200 words.'
      p3_heading = wp.wp_h2(f'features should be considered while buying a {keyword}'.title())
      p3_text = wp.openai_text(text).strip()
      point_3 = p3_heading + wp.wp_para(p3_text)


      # Conclusion
      text = f'Write a conclusion about {line} buying guide. Write a 200 word paragraph'
      concl_heading = wp.wp_h2('Conclusion')
      concl_text = wp.openai_text(text).strip()
      conclu = concl_heading + wp.wp_para(concl_text)



      content = intro + point_1 + point_2 + point_3 + conclu # post of content

      data = {
          'title': title,
          'content': content,
          'slug': slug,
      }

      api_url = "https://biplobsite.local/wp-json/wp/v2/posts"
      res = post(api_url, data=data, headers=wp.headers(), verify=False)
      print(f"{keyword} post done!")




