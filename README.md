# Web Marmato Cultura y Turismo


## Requerimientos

* Python >= 3.5

### Virtualenv

#### Instalación

```bash
apt install python-virtualenv
```

#### Crear Ambiente

```bash
virtualenv -p python3 env
```

## Deploy

```bash
cd web/
python freeze.py
```

### Virtualenv

```bash
env/bin/python web/freeze.py
```

## Run

```bash
cd web/
python run.py
```

### Virtualenv

```bash
env/bin/python web/run.py
```

* La aplicación se ejecutará sobre localhost:5000

## Test deploy

```bash
env/bin/python -m http.server <port>
```

## Referencias

### Plantilla de w3layouts

A Design by W3Layouts
Author: W3layouts
Author URL: http://w3layouts.com
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
