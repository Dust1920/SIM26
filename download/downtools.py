import requests as r

# Descarga de .xlsx a partir de url. 
def downxlsx(url, save_path):
    down = r.get(url)
    with open(save_path, "wb") as data:
        data.write(down.content)
    return save_path