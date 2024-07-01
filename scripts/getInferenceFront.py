import os
#from dotenv import load_dotenv
#import requests
#import subprocess

'''
def getInference():
        load_dotenv()
        api_url = os.getenv("API_URL")

        directorio_destino = "../source_user_image/"
        nombre_archivo = "inference.nii.gz"
        ruta_completa_destino = os.path.join(directorio_destino, nombre_archivo)

        if not api_url:
            print("La variable API_URL no está definida en el archivo .env")
            exit(1)

        # Obtener la ruta de la imagen del primer argumento de línea de comandos
        imagen = sys.argv[1]

        # Verificar si se proporcionó una ruta de imagen como argumento
        if imagen:
            try:
                    # Configura los datos de la solicitud (la imagen como archivo)
                    command = f"SBATCH EXE_inference.sh {imagen}"

                    # Ejecutar el comando como un subprocess
                    resultado = subprocess.run(command, shell=True, capture_output=True, text=True)

                    # Imprime la salida del comando
                    print(resultado.stdout)

                    while True:
                            # Realiza una solicitud GET para verificar si la imagen resultado está lista
                            response_imagen_resultado = requests.get("http://servidor-remoto.com/ruta/a/imagenResultado.nii.gz")

                            if response_imagen_resultado.status_code == 200:
                                # La imagen resultado está lista, descárgala
                                with open(ruta_completa_destino, "wb") as archivo_local:
                                    archivo_local.write(response_imagen_resultado.content)
                                return True
                            else:
                                # La imagen resultado aún no está lista, espera antes de verificar nuevamente
                                print("Esperando la disponibilidad de la imagen resultado...")
                                time.sleep(5)  # Espera 5 segundos antes de volver a verificar

                        

        #         # Realiza la solicitud POST a la API FastAPI
        #         response = requests.post(api_url, files=files)

        #         # Verifica el código de estado de la respuesta
        #         if response.status_code == 200:
        #             print("Imagen enviada correctamente")
        #         else:
        #             print(f"Error al enviar la imagen. Código de estado: {response.status_code}")
        # except FileNotFoundError:
        #     print("Archivo no encontrado. Verifica la ruta de la imagen.")
            except Exception as e:
                print(f"Error: {e}")
                return False
        else:
            print("Debes proporcionar la ruta de la imagen como argumento")
            return False
'''

def getInference():
    os.system('EXE_runService.sh')
