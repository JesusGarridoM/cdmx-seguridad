#!/bin/bash

# Script para levantar ambiente de manera automatica

echo 'Levantando ambiente elk-sandbox...'
cd ../elk-sandbox
docker compose up -d &
wait $!
if [ $? -eq 0 ]
  then
    sudo docker cp elk-sandbox-es01-1:/usr/share/elasticsearch/config/certs/ca/ certs/
    wait $!
    if [ $? -eq 0 ]
      then
        cd ../cdmx-seguridad
        echo 'Modificando archivos de filebeat...'
        sudo chown root:root filebeat/*
        sudo chmod go-w filebeat/*
        echo Levantando cdmx-seguridad...
        docker compose up -d &
        wait $!
        if [ $? -eq 0 ]
          then
            echo 'Exportando configuracion a logstash...'
            cp logstash/cdmx-seguridad.conf ../elk-sandbox/logstash/pipeline/
            sudo cp logstash/cdmx-seguridad.json ../elk-sandbox/logstash/templates/
            cat logstash/pipelines.yml > ../elk-sandbox/logstash/config/pipelines.yml
            echo 'Reiniciando logstash...'
            docker restart elk-sandbox-logstash01-1 &
            wait $!
            if [ $? -eq 0 ]
              then
                echo 'Listo!'
              else
                echo 'Hubo un problema al reiniciar logstash'
            fi
          else
            echo 'Ocurrio un problema al levantar el ambiente cdmx-seguridad'
        fi
      else
        echo 'Ocurrio un problema al copiar los certificados'
    fi
  else
    echo 'Ocurrio un problema al levantar el ambiente elk-sandbox'
fi