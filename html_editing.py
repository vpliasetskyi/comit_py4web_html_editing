# Last time modified: 07/03/26
# Author: pliasetskyi

html_base = ""

with open("garbage.html", "r") as website:
    html_base = website.read()
    

page_title = "My Python Website"

html_modified = html_base.replace("<title>Document", f"<title>{page_title}") 

# print(html_modified)

daisy_ui ="""

<!-- Daisy UI -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
<script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
<!-- Daisy ui themes -->
<link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />

"""

html_modified = html_modified.replace("</head>", daisy_ui +"\n</head>" )

theme = "business"
html_modified = html_modified.replace('<html lang="en">', f'<html lang="en" data-theme="{theme}">')

nav_bar = """
<div class="navbar bg-base-100 shadow-sm">
  <a class="btn btn-ghost text-xl">daisyUI</a>
</div>
"""


html_modified = html_modified.replace('<body>', '<body>\n'+ nav_bar)

with open("index.html", "w") as file:
    file.write(html_modified)


# Create functions to modify html:


# Find the tag and insert any conten we need from daisyUI after some element or before

# Insert a new component at the bottom of chosen tag 
def insert_append(insert_before_tag,new_component):
      global html_modified

      with open ("index.html", "r") as file:
            html_modified = file.read()

      if insert_before_tag in html_modified:
            html_modified = html_modified.replace(insert_before_tag, f"{new_component}\n{insert_before_tag}") 
            
            with open("index.html", "w") as file:
                 file.write(html_modified)
            print("Component appended to the bottom of the  html element")
      else:
            print("Error:  tag not found. Check your html structure")

# Modify inside of any tag 

def modify_inside_element(tag_element, new_component):
    global html_modified
    
    with open("index.html", "r") as file:
        html_modified = file.read() 
        
    if tag_element in html_modified:
        html_modified = html_modified.replace(tag_element, f"{tag_element}{new_component}")
        
        with open("index.html", "w") as file:
            file.write(html_modified)
        print("Tag modified in html file")
        
    else:
        print("Error: tag not found. Check your html structure")

# Insert any element after chosen tag

def put_after_element(insert_at_tag,new_component):
       global html_modified

       if insert_at_tag in html_modified:
           html_modified = html_modified.replace(insert_at_tag, f"{insert_at_tag}\n {new_component}")    

       with open("index.html", "w") as file:
                file.write(html_modified)
                print("Component inserted after chosen  html element")

# Modify and overwrite existing content
def reset_tag_content(tag_start,new_content):
    global html_modified

    with open("index.html", "r") as file:
        html_modified = file.read()

    start_index = (html_modified.find(tag_start))
    
    if start_index != -1:
        end_index = html_modified.find(">", start_index)
        
        if end_index != -1:
            before_tag = html_modified[:start_index]
            after_tag = html_modified[end_index + 1:]
            
            html_modified = f"{before_tag}{tag_start}{new_content}>{after_tag}"

            with open("index.html", "w") as file:
                file.write(html_modified)
            print("Successfully reset the image tag content")

# Modify container content 

def modify_container_text(tag_type, new_text):
    global html_modified

    with open("index.html", "r") as file:
        html_modified = file.read()

    start_tag = f"<{tag_type}"
    start_indx = html_modified.find(start_tag)

    if start_indx != -1:
      
        content_start = html_modified.find(">", start_indx) + 1
        
        closing_tag = f"</{tag_type}>"
        content_end = html_modified.find(closing_tag, content_start)

        if content_start != 0 and content_end != -1:
          
            before = html_modified[:content_start]
            after = html_modified[content_end:]
            html_modified = f"{before}{new_text}{after}"

            with open("index.html", "w") as file:
                file.write(html_modified)
            print(f"Content inside <{tag_type}> updated")
    else:
        print(f"Error: Tag <{tag_type}> not found")                      

# Insert  card element from daisy

product_card ="""  

<div class="card bg-base-100 w-96 shadow-sm">
  <figure>
    <img
      src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
      alt="Shoes" />
  </figure>
  <div class="card-body">
    <h2 class="card-title">Card Title</h2>
    <p>A card component has a figure, a body part, and inside body there are title and actions parts</p>
    <div class="card-actions justify-end">
      <button class="btn btn-primary">Buy Now</button>
    </div>
  </div>
</div>
"""    
new_image = """
      src="images/vacuum.png"
      alt="ROBOVACCUM3000"
"""
new_title = """SUPER-PUPER-AI ROBOVACCUM3000""" 
new_p = """Clean your house and eliminate your family"""
fix_borders ="""border border-base-200"""

insert_append("</body>", product_card)

reset_tag_content("<img",new_image)

modify_container_text("h2",new_title)

modify_container_text("p",new_p)



                      
    
                                                            

