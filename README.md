# cdmx-seguridad

Descarga e instala el repo 
O asegurate de introducir la ruta del certificado `CERT_PATH` en el `.env`

Cambia el usuario de `filebeat.yml`a root
```
sudo chown root:root filebeat/*
sudo chmod go-w filebeat/*
```

Copia las configuraciones de logstash a la carpeta de tu cluster
```
cp logstash/cdmx-seguridad.conf ../elk-sandbox/logstash/pipeline/
cp logstash/cdmx-seguridad.json ../elk-sandbox/logstash/templates/
```
Agrega las lineas `logstash/pipelines.yml` al archivo de `pipelines.yml` logstash
```
cat logstash/pipelines.yml > ../elk-sandbox/logstash/config/pipelines.yml
```
El archivo `pipelines.yml` tendria que quedar algo asi
```
# - pipeline.id: main
#   path.config: "/usr/share/logstash/pipeline"

- pipeline.id: cdmx-seguridad
  path.config: "/usr/share/logstash/pipeline/cdmx-seguridad.conf"
```
Reinicia logstash
```
docker restart elk-sandbox-logstash01-1
```