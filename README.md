# Programa para el cálculo del presupuesto del enlace

El presente programa permite obtener la potencia de recepción estimada o presupuestada para un enlace en el modelo de propagación en el espacio libre.

## Modo de uso
1. Completar los parámetros necesarios en el archivo configuracion.yaml

Ejemplo:

config:
  Ptx: 16 # dBm
  frecuencia: 1000 # MHz
  distancia: 10 # Km
  perdida_conector: 0.25 # dB
  perdida_cable: 0.1 # dB / m
  ht: 50 # m
  hr: 50 # m
  Gtx: 27 # dB
  Grx: 27 # dB
  FM: # Margen de desvanecimiento
    R: 0.99999 # Confiabilidad
    A: 1 # Factor de rugosidad
        - 4 si el terreno es llano o acuático.
        - 1 terreno medio.
        - 0,25 terreno accidentado.
    B: 1 # Factor meteorológico
        - 0.5 zonas calientes y húmedas.
        - 1 zonas medias
        - 0,125 zonas secas y montañosas


2. Correr el programa mediante el archivo `main.py`:

```
# python main.py
```

 o también:

```
# chmod + x main.py
# ./main.py
```