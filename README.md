# Gestión de Productos

Aplicación web en Django para administrar un catálogo de productos con categorías, etiquetas y detalles adicionales. Permite gestionar todo desde una interfaz simple basada en Bootstrap.

## Características

- CRUD completo de productos (crear, listar, ver detalle, editar y eliminar).
- Gestión de categorías con descripción y etiquetas asociadas. 
- Sistema de etiquetas reutilizables para clasificar productos. 
- Página de inicio con enlaces a Productos, Categorías, Etiquetas y Detalles.
- Formularios con validación y estilos Bootstrap. 
- Campos de detalles de producto (dimensiones y peso) gestionados en un modelo separado. 

## Tecnologías

- Python 3  
- Django 5  
- SQLite (por defecto)  
- Bootstrap 5 

## Uso

- Inicio: muestra la bienvenida y enlaces a las secciones principales. 
- Productos: lista con tabla, botones Ver/Editar/Eliminar y botón “Nuevo producto”. 
- Crear/Editar producto: formulario con nombre, descripción, precio, categoría (select), etiquetas (checkbox múltiple) y detalles (dimensiones, peso). 
- Categorías y Etiquetas: secciones similares para administrar categorías y etiquetas desde la web. 
