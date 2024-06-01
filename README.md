# Proyecto "Predicting Red Hat Business Value"
## Miembros del grupo
- Alejandro Sarasti Sierra, CC: 1001014501, Ingeniería de Sistemas
  
## Datos  
Los datos del proyecto vienen de La competición de Kaggle ["Predicting Red Hat Business Value"](https://www.kaggle.com/competitions/predicting-red-hat-business-value/overview)

## ¿Cómo correr el código?

### fase-1

1. Ingresa a tu cuenta de Kaggle y en configuraciones busca el apartado de "API".
2. Haz clic en **Create New API Token**, descargara un archivo .json en tu maquina.
3. Ve al archivo [Modelo_inicial](https://github.com/sarasti2/AI_UdeA_2024-1/tree/main/fase-1/Modelo_inicial.ipynb).
4. Sube el archivo .json en el entorno de trabajo y corre el codigo.

### fase-2

1. Siga los pasos descritos en la fase uni, mientras corre el arhivo [01 - generate-data-and-model.ipynb](https://github.com/sarasti2/AI_UdeA_2024-1/blob/f5445466929b11628ff525b1c1503e7dbbdb2df4/fase-2/01%20-%20generate-data-and-model.ipynb)
2. Simplemente corra el archivo [02 - runscripts.ipynb](https://github.com/sarasti2/AI_UdeA_2024-1/blob/main/fase-2/02%20-%20runscripts.ipynb) desde colab como lo haria normalmente.
3. Revise el [dockerfile](https://github.com/sarasti2/AI_UdeA_2024-1/tree/main/fase-2/docker), y los [scripts](https://github.com/sarasti2/AI_UdeA_2024-1/tree/main/fase-2/scripts) que se utilizaron en el proyecto.

### fase-3

Nota: Para correr esta fase requiere tener instalado (docker)[https://www.docker.com/)

1. Construya el docker

    docker build -t api .

2. Ejecute el contenedor de docker

    docker run -it -p 5001:5000 api

3. En un terminal dedicado corra el archivo [client.py](fase-3/client.py)
   
