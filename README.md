# Modelos RMR3

## Instalación de Librerías
Cada modelo posee su propio set de librerías, los ejecutables son Jupyter notebooks.
1. El modelo [YOLOV7](./yolov7/Yolo_Training.ipynb), sus dependencias son las siguientes. [Requirements BASE](yolov7/requirements.txt) [Requirements GPU](./yolov7/requirements-gpu.txt). Las dependencias de GPU son obligatorias para entrenamiento ya que el modelo como está configurado hace uso de esta.
2. El modelo [Optimizado](./Tensor-ScratchModel+Op.ipynb), posee sus dependencias dentro del mismo Jupyter Notebook.
3. El modelo [Optimizado con Mejoras](./Tensor-ScratchModel_Iter1.ipynb), posee sus dependencias dentro del mismo Jupyter Notebook.

Se recomienda usar un entorno de Python diferente para cada uno y la versión de Python usada es la versión 3.10,
las versiones de CUDA deben cambiarse si difieren o si son marcadas como obsoletas en un futuro, las de este proyecto es CUDA==11.2.67 o el release 11.2. La tarjeta usada es una NVIDIA RTX 4070 sin embargo es compatible con las versiones de la serie 3000, es posible que para series anteriores se requiera hacer un downgrade.

# Ejecutar

## Ejecución de Archivo Jupyter Notebook y Instalación
### Ejecución de Archivo Jupyter Notebook

1. Crea un entorno virtual usando virtualenv: virtualenv venv.
  Activa el entorno virtual:
  En Windows: `venv\Scripts\activate.exe`
  En Linux/ Unix o MacOS: `source venv/bin/activate`
2. Instalación de Dependencias:

  Instala las dependencias requeridas para el modelo YOLO: 
  - `pip install -r requirements.txt`
  - `pip install -r requirements-gpu.txt`

### Ejecutar Jupyter Notebook:

### Instalación de Jupyter Notebook con Anaconda
Método 1: Instalar Anaconda

  Sigue este [video tutorial](https://www.youtube.com/watch?v=E2fKTS8slLo) para instalar Miniconda y Jupyter.
  
  Crea un entorno con Jupyter: `conda create -n nombre_entorno jupyter`
  Activa el entorno: `conda activate nombre_entorno`.
  
Método 2: Instalación de Jupyter Notebook con PyCharm
  Configurar PyCharm:
  
  Abre PyCharm y sigue esta [documentación](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html) para configurar el soporte de Jupyter Notebook.
  Crear y Ejecutar Notebook:
  
  Ya puedes ejecutar las celdas directamente desde PyCharm.

Ejecuta Jupyter Notebook: jupyter notebook.
  Acceder desde el Navegador:

  Abre tu navegador y ve a `http://localhost:8888`.
  Selecciona el archivo .ipynb para abrirlo y ejecutar celdas, en el caso de PyCharm se puede hacer desde el mismo IDE.
