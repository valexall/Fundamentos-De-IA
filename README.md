# Fundamentos de IA

Ejercicios y proyectos del curso de Fundamentos de Inteligencia Artificial.

## Contenido

- `redesBayesianas/`: ejemplos de redes bayesianas con `pgmpy`.
- `SistemaExpertoSimulacion/`: simulador medico con Python, Tkinter y Prolog.
- `preprocesamiento_imagenes/`: transformaciones y data augmentation con OpenCV.
- `preprocesamiento_texto/`: limpieza, tokenización, normalización y vectorización de texto.

## Requisitos

- Python 3.12 o superior.
- Jupyter Notebook o VS Code con soporte para notebooks.
- SWI-Prolog instalado y disponible en el `PATH` para ejecutar el sistema experto.

Las dependencias de Python se encuentran en `requirements.txt`.

## Instalacion

En Windows, desde la raiz del repositorio:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Instala SWI-Prolog desde su sitio oficial: <https://www.swi-prolog.org/Download.html>.

## Ejecucion

### Sistema experto medico

```powershell
cd SistemaExpertoSimulacion
python app.py
```

### Redes bayesianas

Abre cualquiera de los notebooks de `redesBayesianas/` en Jupyter o VS Code y ejecuta sus celdas.

## Nota

El sistema experto medico es un simulador educativo y no reemplaza el diagnostico de un profesional de la salud.
