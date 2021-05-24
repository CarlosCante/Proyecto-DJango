# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.TextField(unique=True, blank=True, null=True)  # This field type is a guess.
    first_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    last_name = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Competencia(models.Model):
    id_competencia = models.BigIntegerField(primary_key=True)
    anio = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=60)
    pais_id_pais = models.ForeignKey('Pais', db_column='pais_id_pais')
    equipo_campeon = models.ForeignKey('Equipo', db_column='equipo_campeon')

    class Meta:
        managed = False
        db_table = 'competencia'


class ContratoJugador(models.Model):
    id_contrato = models.BigIntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=60, blank=True, null=True)
    jugador_id_jugador = models.ForeignKey('Jugador', db_column='jugador_id_jugador')
    equipo_id_equipo = models.ForeignKey('Equipo', db_column='equipo_id_equipo')

    class Meta:
        managed = False
        db_table = 'contrato_jugador'


class ContratoTecnico(models.Model):
    id_contrato = models.BigIntegerField(primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    estado = models.CharField(max_length=60)
    tecnico_id_tecnico = models.ForeignKey('Tecnico', db_column='tecnico_id_tecnico')
    equipo_id_equipo = models.ForeignKey('Equipo', db_column='equipo_id_equipo')

    class Meta:
        managed = False
        db_table = 'contrato_tecnico'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.TextField(blank=True, null=True)  # This field type is a guess.
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.TextField(blank=True, null=True)  # This field type is a guess.
    model = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.TextField(blank=True, null=True)  # This field type is a guess.
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.TextField(primary_key=True)  # This field type is a guess.
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipo(models.Model):
    id_equipo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    fecha_fundacion = models.DateField(blank=True, null=True)
    foto = models.CharField(max_length=1500, blank=True, null=True)
    pais_id_pais = models.ForeignKey('Pais', db_column='pais_id_pais')

    class Meta:
        managed = False
        db_table = 'equipo'


class Estadio(models.Model):
    id_estadio = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)
    fecha_inauguracion = models.DateField(blank=True, null=True)
    capacidad = models.BigIntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    estado = models.CharField(max_length=150, blank=True, null=True)
    foto = models.CharField(max_length=1500, blank=True, null=True)
    pais_id_pais = models.ForeignKey('Pais', db_column='pais_id_pais')

    class Meta:
        managed = False
        db_table = 'estadio'


class Incidencia(models.Model):
    id_incidencia = models.BigIntegerField(primary_key=True)
    incidencia = models.CharField(max_length=150, blank=True, null=True)
    minuto = models.BigIntegerField(blank=True, null=True)
    jugador_id_jugador = models.ForeignKey('Jugador', db_column='jugador_id_jugador')
    partido_id_partido = models.ForeignKey('Partido', db_column='partido_id_partido')

    class Meta:
        managed = False
        db_table = 'incidencia'


class Jugador(models.Model):
    id_jugador = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    fecha_de_nacimiento = models.DateField()
    posicion = models.CharField(max_length=60)
    estado = models.CharField(max_length=60)
    pais_id_pais = models.ForeignKey('Pais', db_column='pais_id_pais')

    class Meta:
        managed = False
        db_table = 'jugador'


class Membresia(models.Model):
    id_membresia = models.BigIntegerField(primary_key=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    usuario_id_usuario = models.ForeignKey('Usuario', db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'membresia'


class ModificacionUsuario(models.Model):
    id_modificacion = models.BigIntegerField(primary_key=True)
    tipo = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=3000)
    usuario_realizo = models.ForeignKey('Usuario', db_column='usuario_realizo')
    usuario_modifcado = models.ForeignKey('Usuario', db_column='usuario_modifcado')

    class Meta:
        managed = False
        db_table = 'modificacion_usuario'


class Noticia(models.Model):
    id_noticia = models.BigIntegerField(primary_key=True)
    titulo = models.CharField(max_length=300)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=3000)
    usuario_id_usuario = models.ForeignKey('Usuario', db_column='usuario_id_usuario')
    equipo_id_equipo = models.ForeignKey(Equipo, db_column='equipo_id_equipo')

    class Meta:
        managed = False
        db_table = 'noticia'


class Pais(models.Model):
    id_pais = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Participacion(models.Model):
    equipo_id_equipo = models.ForeignKey(Equipo, db_column='equipo_id_equipo')
    competencia_id_competencia = models.ForeignKey(Competencia, db_column='competencia_id_competencia')

    class Meta:
        managed = False
        db_table = 'participacion'


class Partido(models.Model):
    id_partido = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    asistencia = models.BigIntegerField()
    resultado = models.CharField(max_length=30)
    incidencias_ocurridas = models.BigIntegerField()
    estado = models.CharField(max_length=60)
    estadio_id_estadio = models.ForeignKey(Estadio, db_column='estadio_id_estadio')
    equipo_visita = models.ForeignKey(Equipo, db_column='equipo_visita')
    equipo_local = models.ForeignKey(Equipo, db_column='equipo_local')

    class Meta:
        managed = False
        db_table = 'partido'


class Suscripcion(models.Model):
    id_suscripcion = models.BigIntegerField(primary_key=True)
    usuario_id_usuario = models.ForeignKey('Usuario', db_column='usuario_id_usuario')
    equipo_id_equipo = models.ForeignKey(Equipo, db_column='equipo_id_equipo')

    class Meta:
        managed = False
        db_table = 'suscripcion'


class Tecnico(models.Model):
    id_tecnico = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    fecha_de_nacimiento = models.DateField()
    estado = models.CharField(max_length=150)
    pais_id_pais = models.ForeignKey(Pais, db_column='pais_id_pais')
    foto = models.CharField(max_length=1500)

    class Meta:
        managed = False
        db_table = 'tecnico'


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    correo = models.CharField(max_length=150)
    telefono = models.BigIntegerField(blank=True, null=True)
    foto = models.CharField(max_length=1500)
    genero = models.CharField(max_length=3)
    fecha_de_nacimiento = models.DateField()
    fecha_de_registro = models.DateField()
    direccion = models.CharField(max_length=300, blank=True, null=True)
    tipo = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    no_tarjeta = models.CharField(max_length=150, blank=True, null=True)
    pais_id_pais = models.ForeignKey(Pais, db_column='pais_id_pais')
    estado_membresia = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'