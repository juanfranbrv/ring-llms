# ring-llms

## Descripción
Esta es una aplicación Streamlit creada con UV, un gestor de paquetes y entornos virtuales ultrarrápido.

## Características
- Interfaz de usuario moderna con Streamlit
- Gestión de dependencias con UV
- Estructura de proyecto optimizada

## Requisitos
- Python 3.8 o superior
- UV (instalado con `curl -LsSf https://astral.sh/uv/install.sh | sh` o `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`)

## Instalación

1. Clona este repositorio o descárgalo:
   ```bash
   git clone <url-del-repositorio>
   cd ring-llms
   ```

2. Sincroniza las dependencias con UV:
   ```bash
   uv sync
   ```

## Uso

Para ejecutar la aplicación:
```bash
uv run streamlit run app.py
```

O si tienes el entorno virtual activado:
```bash
streamlit run app.py
```

## Estructura del proyecto
```
ring-llms/
├── app.py                # Aplicación principal de Streamlit
├── .streamlit/           # Configuración de Streamlit
│   └── secrets.toml      # Secretos (no incluidos en Git)
├── .venv/                # Entorno virtual (generado por UV)
├── pyproject.toml        # Configuración del proyecto y dependencias
└── README.md             # Este archivo
```

## Licencia
Este proyecto está disponible bajo la licencia MIT.

## Créditos
Creado con [streamlit-uv.py](https://github.com/usuario/streamlit-uv)
