import json
import logging
from usuario import Usuario

# Configurar logging para manejar las excepciones
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def crear_instancia_usuario(data):
    try:
        # Crear instancia de Usuario a partir del diccionario
        return Usuario(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            email=data.get('email'),
            genero=data.get('genero')
        )
    except Exception as e:
        logging.error(f"Error al crear instancia de Usuario: {e}")
        return None

def main():
    usuarios = []
    
    try:
        with open('usuarios.txt', 'r') as file:
            for line in file:
                try:
                    # Cargar datos JSON de la línea
                    data = json.loads(line.strip())
                    
                    # Crear instancia de Usuario
                    usuario = crear_instancia_usuario(data)
                    
                    if usuario:
                        usuarios.append(usuario)
                except json.JSONDecodeError as e:
                    logging.error(f"Error al decodificar JSON: {e}")
                except Exception as e:
                    logging.error(f"Error al procesar línea: {e}")

    except FileNotFoundError as e:
        logging.error(f"Archivo no encontrado: {e}")
    except Exception as e:
        logging.error(f"Error al leer el archivo: {e}")

    # Aquí puedes hacer lo que necesites con la lista de usuarios
    print(f"Se han creado {len(usuarios)} instancias de Usuario.")

if __name__ == "__main__":
    main()
