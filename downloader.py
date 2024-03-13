# Download the victims in investigation files of the FGJ dataset 
# of the CDMX from the portal datos.cdmx.gob.mx

import requests

def download_file(url, file_name):
    # Download CSV
    print("Connecting to datos.cdmx.gob.mx...")
    response = requests.get(url, stream=True)

    # Verify response code
    if response.status_code == 200:
        # Show download progress
        total_size = int(response.headers.get("content-length"))
        print(f"Downloading dataset ({total_size/1048576:.2f}M)...")
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                progress = (file.tell() / total_size) * 100
                print(f"\rProgress: {progress:.2f}%", end="")
        print("\nDownload completed!")
    else:
        raise RuntimeError(f"Error: {response.status_code}")

# Descargar archivo de victimas
url = "https://archivo.datos.cdmx.gob.mx/FGJ/victimas/victimasFGJ_acumulado_2024_01.csv"
file_name = "/data/cdmx-seguridad/victimasFGJ_acumulado_2024_01.csv"

try:
    download_file(url, file_name)
except RuntimeError as error:
    print(error)

# Descargar catalogo de colonias
url = "https://datos.cdmx.gob.mx/dataset/02c6ce99-dbd8-47d8-aee1-ae885a12bb2f/resource/026b42d3-a609-44c7-a83d-22b2150caffc/download/catlogo-de-colonias.json"
file_name = "/data/cdmx-colonias/catalogo-de-colonias.geojson"

try:
    download_file(url, file_name)
except RuntimeError as error:
    print(error)
