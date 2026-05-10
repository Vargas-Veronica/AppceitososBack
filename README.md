# Aceitosos Web

Proyecto Django backend para la aplicación Aceitosos.

## Estructura principal

- `back/` - backend Django
  - `ecommerce/` - proyecto Django
  - `api/` - app API
  - `requirements.txt` - dependencias Python
  - `venv38/` - virtual environment existente (no incluido en Git)
- `front/` - carpeta de frontend vacía actualmente

## Requisitos

- Python 3.8+ instalado
- MySQL o MariaDB instalado y en ejecución
- (Opcional) un entorno virtual Python

## Configuración recomendada

1. Abrir terminal en `back/`:

```powershell
cd c:\Users\varga\OneDrive\Escritorio\aceitososWeb\back
```

2. Crear y activar un entorno virtual nuevo (recomendado):

```powershell
python -m venv venv
venv\Scripts\activate
```

3. Instalar dependencias:

```powershell
pip install -r requirements.txt
```

> Si prefieres usar el `venv38` existente, activa:
>
> ```powershell
> .\venv38\Scripts\activate
> ```

## Base de datos

La configuración actual en `back/ecommerce/ecommerce/settings.py` usa MySQL:

- Nombre de base de datos: `aceitososdb`
- Usuario: `root`
- Contraseña: `''` (vacía)
- Host: `localhost`
- Puerto: `3306`

Asegúrate de crear la base de datos antes de ejecutar migraciones:

```sql
CREATE DATABASE aceitososdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Si no quieres usar MySQL, debes modificar `DATABASES` en `back/ecommerce/ecommerce/settings.py` para usar SQLite u otra configuración.

## Migraciones y carga inicial

```powershell
python ecommerce/manage.py migrate
```

Opcional: crear superusuario

```powershell
python ecommerce/manage.py createsuperuser
```

## Ejecutar el servidor

```powershell
python ecommerce/manage.py runserver
```

Luego abre en el navegador:

```text
http://127.0.0.1:8000/
```

## Notas importantes

- El backend está configurado para usar `django-cors-headers`, `knox` y `whitenoise`.
- El `front/` está vacío, por lo que no hay frontend incluido en este repositorio.
- Si usas `ngrok` o un host remoto, revisa los valores de `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS` y `CSRF_TRUSTED_ORIGINS` en `back/ecommerce/ecommerce/settings.py`.
- Si el proyecto falla por falta de dependencia, ejecuta `pip install -r requirements.txt` nuevamente.

## Comandos útiles

```powershell
cd back
venv\Scripts\activate
pip install -r requirements.txt
python ecommerce/manage.py migrate
python ecommerce/manage.py runserver
```
