from  rest_framework import serializers

from .models import Rol, Usuario, Categoria,Curso, MisCurso, Carrito, Foro, Contacto, ForoRespuesta, Recordatorio, CursoFavorito

class RolSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Rol
        fields = '__all__'

#===========================================================================================================================================================================
class UsuarioSerializer(serializers.Serializer):
    # Se definen los campos del serializer
    id_usuario =serializers.CharField(required=False)
    nombre = serializers.CharField(required=True)
    apellido = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    id_rol_id = serializers.IntegerField(required=True)
    urlImagen = serializers.CharField(required = False)

    class Meta:
        model = Usuario
        fields = ['id_usuario','nombre', 'apellido', 'email', 'password', 'urlImagen', 'id_rol_id']
        extra_kwargs = {'password': {'write_only': True}}
        #El campo password tiene la configuración adicional write_only=True, lo que significa que solo se utilizará para la creación de un nuevo usuario y no se incluirá en las respuestas de serialización

    def create(self, validated_data):
        # Se extrae el campo 'password' del diccionario de datos validados
        password = validated_data.pop('password')
        # Se crea un nuevo usuario utilizando el método create_user de la clase Usuario
        usuario = Usuario.objects.create_user(password=password, **validated_data)
        # Se retorna el usuario creado
        return usuario
    
#===========================================================================================================================================================================

class CategoriaSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Categoria
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Curso
        fields = '__all__'

#===========================================================================================================================================================================

class MisCursoSerializer(serializers.ModelSerializer):
    id_curso = serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all())  # Campo para el ID del curso

    # Agregar campo de descripción
    nombre_curso = serializers.CharField(source='id_curso.nombre_curso', read_only=True)
    descripcion_curso = serializers.CharField(source='id_curso.descripcion', read_only=True)
    imagen_url = serializers.CharField(source='id_curso.imagen_url', read_only=True)
    
    class Meta:
        model = MisCurso
        fields = ['id_mis_curso', 'id_usuario', 'id_curso', 'nombre_curso', 'descripcion_curso', 'imagen_url']

class CursoFavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoFavorito
        fields = '__all__'

#===========================================================================================================================================================================
class CarritoSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Carrito
        fields = '__all__'

class ForoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foro
        fields = ['id_foro', 'id_usuarios', 'id_rol', 'nombre', 'titulo', 'mensaje', 'id_foro_respuesta', 'fecha']

class ForoRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForoRespuesta
        fields = ['id_foro_respuesta','nombre', 'mensaje', 'id_foro', 'id_usuario','fecha']

class ContactoSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Contacto
        fields = '__all__'

class RecordatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordatorio
        fields = ['id_recordatorio', 'usuario', 'tarea', 'fecha']
