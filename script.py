import json
import logging
from usuario import Usuario

# Configurar logging para manejar las excepciones
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def crear_instancia_usuario(data):
    """
    Crea una instancia de Usuario a partir de un diccionario de datos.
    Maneja excepciones al crear la instancia y registra los errores en error.log.
    
    Args:
        data (dict): Diccionario con datos del usuario.
    
    Returns:
        Usuario: Instancia de Usuario si no hay errores, None en caso contrario.
    """
    try:
        # Crear instancia de Usuario a partir del diccionario
        return Usuario(
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            email=data.get('email'),
            genero=data.get('genero')
        )
    except Exception as e:
        # Registrar cualquier error al crear la instancia
        logging.error(f"Error al crear instancia de Usuario: {e}")
        return None

def main():
    """
    Lee el archivo usuarios.txt, crea instancias de Usuario y maneja errores.
    Registra errores en error.log y almacena instancias válidas en una lista.
    """
    usuarios = []
    
    try:
        # Abrir el archivo usuarios.txt en modo lectura
        with open('usuarios.txt', 'r') as file:
            for line in file:
                try:
                    # Cargar datos JSON de la línea
                    data = json.loads(line.strip())
                    
                    # Crear instancia de Usuario
                    usuario = crear_instancia_usuario(data)
                    
                    if usuario:
                        # Agregar usuario a la lista si se creó correctamente
                        usuarios.append(usuario)
                except json.JSONDecodeError as e:
                    # Registrar error de decodificación JSON
                    logging.error(f"Error al decodificar JSON: {e}")
                except Exception as e:
                    # Registrar cualquier otro error durante el procesamiento de la línea
                    logging.error(f"Error al procesar línea: {e}")

    except FileNotFoundError as e:
        # Registrar error si el archivo no se encuentra
        logging.error(f"Archivo no encontrado: {e}")
    except Exception as e:
        # Registrar cualquier otro error al leer el archivo
        logging.error(f"Error al leer el archivo: {e}")

    # Mostrar el número total de instancias de Usuario creadas
    print(f"Se han creado {len(usuarios)} instancias de Usuario.")

if __name__ == "__main__":
    main()
