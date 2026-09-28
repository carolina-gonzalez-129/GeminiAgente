#Agente BACO — prueba con MockAPI y Strands
import requests
import strands
from strands import Agent,tool
import strands.vended_tools
from strands.models.gemini import GeminiModel
"""
  lo use para ir trackeando como se ejecutaba, primero se cargó el modelo, dsps registro las tools, el system prompt
  
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)
"""

# ============================================================
# MODELO
# ============================================================
model = GeminiModel(
    model_id="gemini-3.6-flash",
    client_args={"api_key": "AQ.Ab8RN6KAVIBhSsMZ7RwcI0NbcC_1yAObn9sUu1IT15Wy1VlnuA"}
)

# ============================================================
# ============================================================
# TOOL : CONSULTAR ARTICULOS
#Esta tool simula el acceso al MCP, hacemos un get a una mockapi que contiene articulos de prueba
# ============================================================
URL_ARTICULOS = "https://6ab1de0e5b9b60f39d342e90.mockapi.io/uwu/articulos"

@tool
def buscar_articulos() -> list:
    """Lista los artículos cargados en la Base de Conocimiento.
    Usar solo si el usuario pide ver qué artículos hay."""
    r = requests.get(URL_ARTICULOS, timeout=10)
    if r.status_code != 200:
        return [f"Error al obtener artículos: {r.status_code}"]
    return [a["titulo"] for a in r.json() if "titulo" in a]
# ============================================================
# AGENTE BACO
# ============================================================
SYSTEM_PROMPT = """Sos BACO, asistente de una Base de Conocimiento.
Respondé directo a preguntas generales y conversación.
Si te piden algo que no podés hacer (ej: eliminar artículos), explicá que no tenés esa función.
Nunca inventes títulos ni datos de artículos."""

agent = Agent(
    model=model,
    tools=[buscar_articulos],
    system_prompt=SYSTEM_PROMPT
)


# ============================================================
# PRUEBAS
# ============================================================
print("\n" + "=" * 50)
print("🤖 CONSULTA 1")
print("=" * 50)
#Prueba de que el LLM funciona
agent("En una frase podrias decir qué diferencia procariotas de eucariotas?")
# ============================================================
# CONSULTA 2: HERRAMIENTA QUE NO TIENE
# ============================================================
print("\n" + "=" * 50)
print("🤖 CONSULTA 2")
print("=" * 50)
agent("Podrias ayudarme a eliminar artículos?")
# ============================================================
# CONSULTA 3: USO DE TOOL
# ============================================================
print("\n" + "=" * 50)
print("🤖 CONSULTA 3")
print("=" * 50)
agent("Podrias decirme que artículos hay en la base de conocimiento?")


# ============================================================
# FIN
# ============================================================

print("\n" + "=" * 50)
print("✅ Fin de las consultas")
print("=" * 50)
