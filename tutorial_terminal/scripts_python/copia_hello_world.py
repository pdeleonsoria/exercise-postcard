
from datetime import datetime 
fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:$M:$S")

with open("/workspace/exercise-postcard/tutorial_terminal/scripts_python/res/text.txt", "a") as archivo:
	archivo.write(f"Tarea finalizada a las {fecha_hora_actual}")



