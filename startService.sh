#!/bin/sh
echo "|    Feito por Diego Nascimento"
echo "|    github.com/diegonvs"
echo "|    Iniciando serviço:"
echo "|    Coletando trending topics a cada 5 minutos"
echo "|    Iniciando o flask..."

while [ 1 ]; do
     python getTrends.py && python service.py &
     sleep 300
done