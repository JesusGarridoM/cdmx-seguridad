# Download the victims in investigation files of the FGJ dataset 
# of the CDMX from the portal datos.cdmx.gob.mx

import requests

def download_dataset(url, file_name):
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

# Ejemplo de uso
url = "https://archivo.datos.cdmx.gob.mx/FGJ/victimas/victimasFGJ_acumulado_2024_01.csv"
file_name = "/data/victimasFGJ_acumulado_2024_01.csv"

try:
    download_dataset(url, file_name)
except RuntimeError as error:
    print(error)
