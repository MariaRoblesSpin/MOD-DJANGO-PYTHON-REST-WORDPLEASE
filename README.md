# MOD-DJANGO-PYTHON-REST-WORDPLEASE

Se crea una plataforma para contener blogs llamada WordPlease. La plataforma ofrece dos funcionalidades, un sitio Web para la consulta y creación de blogs y sus artículos y un API_Rest para el acceso a través de programas si para algún fin se requiere, por ejemplo para crear una APP móvil.

## Sitio WEB

Se han implementado todas las URLs solicitadas en la especificación del ejercicio:

*	http://localhost:8000/ Acceso a la página principal del sitio. Se muestran a cualquiera que acceda sin autenticación los posts publicados de todos los blogueros. Se muestran inicialmente solo los 5 últimos publicados, existiendo un enlace para verlos todos si así lo desea el usuario.
*	http://localhost:8000/blogs  Muestra un listado de todos los blogs existentes
*	http://localhost:8000/blogs/nombreusuario Muestra los posts del usuario ordenados por fecha de última modificación de más reciente a más antiguo.
*	http://localhost:8000/blogs/nombreusuario/idpost Muestra el detalle de un post
*	http://localhost:8000/new_post Permite la creación de nuevos post a usuarios autenticados
*	http://localhost:8000/login permite autenticarse a usuarios previamente registrados
*	http://localhost:8000/logout permite desautenticarse a usuarios autenticados
*	http://localhost:8000/signup permite registrase a un usuario en la plataforma

La navegación entre URLs, varía dependiendo de que el usuario esté autenticado o no:

* Los usuarios no autenticados pueden: 
  * darse de alta en la plataforma para luego autenticarse y crear su propio blog, 
  * ver los posts publicados de todos los blogueros,
  * ver una lista de blogs existentes.
* Los usuarios autenticados pueden: 
  * hacer login y logout en la plataforma, 
  * ver sus posts tanto los publicados cómo los no publicados,
  * añadir nuevos post.

## API_REST

Utilizando Django REST Framework, se han implementado los end points solicitados en el enunciado del ejercicio de la siguiente manera:

### 1. Registrar un usuario

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/users </td>
   </tr>

   <tr>
      <td>Método http</td>
      <td>POST</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Usuarios</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td>Cualquiera, no requiere autenticación</td>
   </tr>
</table>

### 2. Consultar detalle de un usuario

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/users/<int:Id_usuario></td>
   </tr>

   <tr>
      <td>Método http</td>
      <td>GET</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Usuarios</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td>Requiere autenticación. Puede consultar los detalles de un usuario el propio usuario o un usuario administrador.</td>
   </tr>
</table>

### 3. Actualizar los datos del usuario

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/users/<int:Id_usuario></td>
   </tr>

   <tr>
      <td>Método http</td>
      <td>PUT</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Usuarios</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td>Requiere autenticación. Puede actualizar los detalles de un usuario el propio usuario o un usuario administrador.</td>
   </tr>
</table>

### 4. Borrar un usuario

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/users/<int:Id_usuario></td>
   </tr>

   <tr>
      <td>Método http</td>
      <td>DELETE</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Usuarios</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td>Requiere autenticación. Puede borrar los detalles de un usuario el propio usuario o un usuario administrador.</td>
   </tr>
</table>

### 5. Consultar los blogs existentes en la plataforma

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/users</td>
   </tr>

   <tr>
      <td>Método http</td>
      <td>GET</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Blogs</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td>Requiere autenticación. Puede consultar los detalles de un usuario el propio usuario o un usuario administrador.</td>
   </tr>
   <tr>
      <td>Búsqueda y ordenación</td>
      <td>http://localhost:8000/api/users/search=username<br/>
http://localhost:8000/api/users/ordering=username
</td>
   </tr>
</table>

### 6. Leer los post de un blog

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/posts/<str:nombreusuario> </td>
   </tr>

   <tr>
      <td>Método http</td>
      <td>GET</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Posts</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td>Sin autenticación suministra todos los post publicados. Con autenticación: para usuario no administrador muestra todos sus posts publicados o no, para usuario administrador muestra los posts de todos los usuarios publicados o no.
<br/>Los posts se muestran siempre ordenados por fecha de publicación de mas reciente a más antiguo.</td>
   </tr>
   <tr>
      <td>Búsqueda y ordenación</td>
      <td>http://localhost:8000/api/posts/<str:nombreusuario>?search=cadena<br/>
      http://localhost:8000/api/posts/<str:nombreusuario>?ordering=title<br/>
http://localhost:8000/api/posts/<str:nombreusuario>?ordering=fecha_publicacion
</td>
   </tr>
</table>

### 7. Crear un post

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/posts/<str:nombreusuario></td>
   </tr>

   <tr>
      <td>Método http</td>
      <td>POST</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Posts</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td>Requiere autenticación. El post se da de alta en el blog del usuario autenticado.</td>
   </tr>
</table>

### 8. Ver detalles de un post

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/posts/int:id_post</td>
   </tr>

   <tr>
      <td>Método http</td>
      <td>GET</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Posts</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td>Si el usuario no está autenticado muestra los detalles si en un post públicado, si el usuario está autenticado y es el autor del post o es un administrador muestra los detalles del post aunque no esté publicado. </td>
   </tr>
</table>

### 9. Actualizar un post

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/posts/int:id_post</td>
   </tr>

   <tr>
      <td>Método http</td>
      <td>PUT</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Posts</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td> Requiere autenticación, solo el autor de un post o un administrador puede modificar un post. </td>
   </tr>
</table>

### 10.	Borrar un post

 <table>
   <tr>
      <td>End point</td>
      <td>http://localhost:8000/api/posts/int:id_post</td>
   </tr>
   <tr>
      <td>Método http</td>
      <td>DELETE</td>
   </tr>
    <tr>
      <td>Tipo API</td>
      <td>Posts</td>
   </tr>
    <tr>
      <td>Condiciones</td>
      <td> Requiere autenticación, solo el autor de un post o un administrador puede borrar un post.  </td>
   </tr>
</table>

## Otras acciones llevadas a cabo 
-	Instalado y customizado PyCharm.
-	Creado un modelo independiente de categorías para que el administrador pueda gestionarlas.
-	Incluida validación anti-palabrotas en el body de un post. 
-	Customizada la administración del modelo Post en http://localhost:8000/admin
-	Instalado bootstrap.
-	Instalada Django api rest.
-	Postman para las pruebas del API Rest.





