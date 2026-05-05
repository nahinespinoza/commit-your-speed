"""
Commit Your Speed — Lanzador
Doble-click en este archivo para iniciar el juego.
Requiere Python 3 (viene instalado en Windows 10/11).
"""
import http.server
import socketserver
import webbrowser
import threading
import os

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, format, *args):
        pass  # silencia logs
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

class ReuseServer(socketserver.TCPServer):
    allow_reuse_address = True  # evita "Address already in use"

def abrir_browser():
    import time
    time.sleep(0.8)
    webbrowser.open(f'http://localhost:{PORT}/commit-your-speed-github.html')

print("=" * 50)
print("  Commit Your Speed — Club de Software")
print("=" * 50)
print(f"\n  Servidor corriendo en http://localhost:{PORT}")
print("  Abriendo el juego en el navegador...")
print("\n  [Presiona Ctrl+C para detener]\n")

threading.Thread(target=abrir_browser, daemon=True).start()

with ReuseServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  Servidor detenido.")