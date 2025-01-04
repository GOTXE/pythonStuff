# Nota
[documentación oficial de Git](https://git-scm.com/doc) para obtener más información detallada.

# Comandos Básicos para Administrar tu Repositorio

- **`git init`**: Inicializa un nuevo repositorio Git en el directorio actual.
  - **Ejemplo**: `git init` (dentro de tu carpeta de proyecto)

- **`git clone`**: Clona (copia) un repositorio existente en una nueva ubicación.
  - **Ejemplo**: `git clone https://github.com/usuario/proyecto.git`

- **`git status`**: Muestra el estado actual del repositorio, indicando qué archivos han sido modificados, añadidos o eliminados.
  - **Ejemplo**: `git status` (muestra qué archivos han sido modificados, etc.)

- **`git add`**: Agrega los cambios de un archivo al área de preparación (staging area) para ser incluidos en el próximo commit.
  - **Ejemplo**: `git add archivo1.txt archivo2.py` (añade dos archivos al siguiente commit)

- **`git commit`**: Crea un nuevo commit (instantánea) de los cambios que se encuentran en el área de preparación.
  - **Ejemplo**: `git commit -m "Agregando nuevas funcionalidades"`

- **`git push`**: Envía los commits locales a un repositorio remoto.
  - **Ejemplo**: `git push origin main` (envía los cambios a la rama principal del repositorio remoto)

- **`git pull`**: Descarga los cambios de un repositorio remoto y los fusiona con tu rama local.
  - **Ejemplo**: `git pull origin main` (descarga los cambios más recientes de la rama principal)

# Comandos para Gestionar Ramas

- **`git branch`**: Muestra una lista de las ramas existentes.
  - **Ejemplo**: `git branch` (muestra todas las ramas)

- **`git checkout`**: Cambia a una rama existente o crea una nueva.
  - **Ejemplo**: `git checkout nueva-rama` (cambia a la rama "nueva-rama" o la crea)

- **`git merge`**: Fusiona una rama en otra.
  - **Ejemplo**: `git merge otra-rama` (fusiona la rama "otra-rama" en la rama actual)

- **`git rebase`**: Reubica una serie de commits en una nueva base.
  - **Ejemplo**: `git rebase main` (reubica los commits de la rama actual sobre la rama "main")

# Otros Comandos Útiles

- **`git log`**: Muestra el historial de commits.
  - **Ejemplo**: `git log` (muestra todos los commits)

- **`git diff`**: Muestra las diferencias entre dos commits o entre el área de trabajo y el último commit.
  - **Ejemplo**: `git diff HEAD~1` (muestra las diferencias entre el último commit y el anterior)

- **`git reset`**: Deshace los cambios más recientes.
  - **Ejemplo**: `git reset HEAD~1` (deshace el último commit)

- **`git revert`**: Deshace un commit específico.
  - **Ejemplo**: `git revert <hash_del_commit>` (deshace un commit específico)

- **`git tag`**: Crea una etiqueta para marcar un punto específico en el historial.
  - **Ejemplo**: `git tag v1.0` (crea una etiqueta llamada "v1.0" en el commit actual)

# Explicación Rápida de Algunos Conceptos Clave

- **Repositorio**: Un directorio que contiene todos los archivos de tu proyecto y el historial de cambios.
- **Commit**: Una instantánea de tu proyecto en un momento dado.
- **Rama**: Una línea de desarrollo independiente.
- **Área de preparación (staging area)**: Un área intermedia donde se preparan los cambios antes de ser incluidos en un commit.
- **Origen remoto**: El repositorio remoto al que se envían los cambios.

# Ejemplo de un Flujo de Trabajo Típico

1. **Clonar un repositorio**: `git clone https://github.com/usuario/proyecto.git`
2. **Crear una nueva rama**: `git checkout -b nueva-rama`
3. **Realizar cambios**: Editar archivos.
4. **Añadir cambios al área de preparación**: `git add archivo1.txt archivo2.py`
5. **Crear un commit**: `git commit -m "Mensaje descriptivo del commit"`
6. **Enviar los cambios al repositorio remoto**: `git push origin nueva-rama`
