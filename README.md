# Código de Honor · Contadeus International

App interactiva (Streamlit) con tarjetas del Código de Honor, la Misión, la Visión, y un quiz rápido para que el equipo aprenda jugando.

## Cómo publicarla gratis (GitHub + Streamlit Community Cloud)

### 1. Sube el proyecto a GitHub
1. Crea una cuenta en [github.com](https://github.com) si no tienes una.
2. Crea un repositorio nuevo (por ejemplo `codigo-de-honor-contadeus`). Puede ser público o privado.
3. Sube estos 3 archivos al repositorio:
   - `app.py`
   - `requirements.txt`
   - `README.md`

   Puedes hacerlo arrastrando los archivos desde la web de GitHub ("Add file" → "Upload files"), sin necesidad de usar la terminal.

### 2. Despliega en Streamlit Community Cloud
1. Entra a [streamlit.io](https://streamlit.io) y haz clic en "Sign up" / "Get started" (puedes entrar directo con tu cuenta de GitHub).
2. Una vez dentro, haz clic en **"New app"**.
3. Selecciona el repositorio que acabas de crear, la rama `main`, y el archivo principal `app.py`.
4. Haz clic en **"Deploy"**. En 1-2 minutos tendrás un link público (algo como `https://codigo-de-honor-contadeus.streamlit.app`).
5. Comparte ese link con el equipo por WhatsApp, correo o donde prefieran. Funciona en celular y computadora, sin instalar nada.

### 3. Actualizaciones futuras
Cualquier cambio que subas al archivo `app.py` en GitHub se refleja automáticamente en la app publicada (Streamlit la vuelve a desplegar sola).

## Probarla en tu computadora (opcional, antes de publicar)
Si tienes Python instalado:
```bash
pip install -r requirements.txt
streamlit run app.py
```
Esto abre la app en tu navegador en `http://localhost:8501`.
