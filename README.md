Este proyecto es una simulación del sistema de gestión de pedidos de etiquetas autoadhesivas personalizadas para la empresa ficticia Solo Etiquetas.
Se desarrolló como caso de estudio dentro del marco de la materia Ingeniería de Software, con el objetivo de aplicar las etapas del ciclo de vida del desarrollo de software utilizando una metodología ágil 
con enfoque  híbrido, combinando elementos de Scrum y Kanban.

🎯 Finalidad del sistema
Permitir a los clientes gestionar de forma autónoma el diseño, la carga de imágenes, la selección del método de envío, el pago y la realización de pedidos de etiquetas. 
Todos los pedidos realizados quedan registrados y pueden ser consultados en el historial del cliente. Además, los administradores del sistema pueden consultar los pedidos de cualquier cliente.

🛠️ Tecnologías utilizadas
Lenguaje: Python 3
Paradigma: Programación Orientada a Objetos (OOP)
Testing: unittest

🧩 Estructura del sistema
Clases principales:
Usuario
UsuarioCliente
UsuarioAdministrador
Pedido
Imagen
MetodoDeEnvio
Pago

Funcionalidades implementadas
Clientes pueden:
Registrarse, iniciar sesión y eliminar su cuenta.
Cargar imágenes para sus etiquetas.
Realizar pedidos con una o más imágenes (con cálculo automático del total).
Visualizar su historial de pedidos.

Administradores pueden:
Consultar los pedidos realizados por cualquier cliente.
Eliminar cuentas de clientes.

El sistema permite:
Calcular automáticamente el total del pedido en función de la cantidad de imágenes.
Calcular el costo de envío según la zona seleccionada.


▶️ Cómo ejecutar el proyecto
1. Requisitos
Tener Python 3 instalado

2. Clonar el repositorio
git clone https://github.com/Isis-Rolon/Solo-Etiquetas.git
cd Solo-Etiquetas

3. Ejecutar los tests
python test_usuario.py
python test_pedido.py
python test_imagen.py
python test_metodo_envio.py
python test_pago.py

🔗 Enlace al repositorio
https://github.com/Isis-Rolon/Solo-Etiquetas

👥 Roles del equipo
Product Owner: Claudia López
Scrum Master: Ricardo Díaz
Equipo de Desarrollo: Emanuel Camilli – Francisco Rolón – Isis Rolón

📚 Materia
Trabajo práctico integrador para la materia Ingeniería de Software

