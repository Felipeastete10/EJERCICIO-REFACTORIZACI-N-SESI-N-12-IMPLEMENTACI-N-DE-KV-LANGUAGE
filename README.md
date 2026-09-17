# 🧮 Calculadora Refactorizada en Kivy

Proyecto desarrollado para la **Sesión 12: Implementación de KV Language**. Separa la interfaz visual de la lógica de programación aplicando el patrón de arquitectura MVC.

---

## 📁 Estructura del Repositorio

| Archivo | Descripción |
| :--- | :--- |
| `main.py` | Controlador de eventos y lógica matemática. |
| `calculadora.kv` | Interfaz gráfica, jerarquía de layouts y estilos. |
| `USO_DE_IA.md` | Declaración detallada del uso de Inteligencia Artificial. |
| `screenshot.png` | Evidencia de ejecución de la interfaz. |

---

## 🎨 Arquitectura e Interfaz

* **Separación Estricta:** El archivo Python no contiene estilos visuales ni estructuras de layout hardcodeadas.
* **Diseño:** Distribución basada en un `BoxLayout` vertical principal más un `GridLayout` de 4×4.
* **Estilos:** Paleta de colores diferenciada por función (números, operadores, borrado y resultado).

---

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Felipeastete10/EJERCICIO-REFACTORIZACI-N-SESI-N-12-IMPLEMENTACI-N-DE-KV-LANGUAGE.git
