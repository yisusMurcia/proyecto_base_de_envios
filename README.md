# proyecto_base_de_envios

## Conexión a la base de datos

La prueba de conexión toma los parámetros de conexión de variables de entorno.
Completa los valores locales en `.env` y, desde PowerShell en la carpeta del
proyecto, ejecuta:

```powershell
$db = Get-Content .env -Raw | ConvertFrom-StringData; foreach ($key in $db.Keys) { $value = [string]$db[$key]; Set-Item -Path "Env:$key" -Value $value }; python .\prueba.py
```
