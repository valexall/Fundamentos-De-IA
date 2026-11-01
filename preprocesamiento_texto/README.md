# Preprocesamiento de texto

La actividad sigue los temas y ejemplos de los slides de la semana 7:

- limpieza de texto;
- tokenización de palabras y oraciones;
- eliminación de stopwords;
- stemming en español;
- lematización en español;
- vectorización mediante TF-IDF.

## Ejecución del script

Instala las dependencias desde la raíz:

```powershell
python -m pip install -r requirements.txt
python -m spacy download es_core_news_sm
python preprocesamiento_texto\preprocesamiento_texto.py
```

El notebook `preprocesamiento_texto.ipynb` contiene el mismo procedimiento preparado
para Google Colab.
