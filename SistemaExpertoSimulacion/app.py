import os
import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

try:
    from pyswip import Prolog
except ImportError:
    print("Error: No se pudo importar 'pyswip'.")
    sys.exit(1)

def cargar_conocimiento(prolog):
    archivo_pl = "enfermedades.pl"
    if not os.path.exists(archivo_pl):
        messagebox.showerror("Error", f"No se encuentra el archivo '{archivo_pl}'.")
        sys.exit(1)
    
    archivo_pl = archivo_pl.replace('\\', '/')
    try:
        prolog.consult(archivo_pl)
    except Exception as e:
        messagebox.showerror("Error de Prolog", f"No se pudo cargar Prolog. Detalles: {e}")
        sys.exit(1)

def obtener_todos_los_sintomas(prolog):
    sintomas = list(prolog.query("sintomas_posibles(S)"))
    if sintomas:
        return [str(s.decode('utf-8') if isinstance(s, bytes) else s) for s in sintomas[0]["S"]]
    return []

def diagnosticar(prolog, sintomas_usuario):
    if not sintomas_usuario:
        return []
    
    sintomas_str = "[" + ", ".join(sintomas_usuario) + "]"
    query_str = f"diagnosticar(Enfermedad, {sintomas_str}, Coincidencias)"
    resultados = list(prolog.query(query_str))
    
    diagnosticos = []
    for res in resultados:
        diagnosticos.append({
            "enfermedad": str(res["Enfermedad"]),
            "coincidencias": int(res["Coincidencias"])
        })
    
    diagnosticos.sort(key=lambda x: x["coincidencias"], reverse=True)
    return diagnosticos

class SistemaExpertoGUI:
    def __init__(self, root, prolog, sintomas):
        self.root = root
        self.prolog = prolog
        self.sintomas = sintomas
        self.variables_sintomas = {}
        
        self.root.title("Simulador de Sistema Experto Médico")
        self.root.geometry("500x600")
        self.root.configure(padx=20, pady=20)
        
        self.crear_widgets()
        
    def crear_widgets(self):
        lbl_titulo = ttk.Label(self.root, text="Diagnóstico Médico", font=("Helvetica", 16, "bold"))
        lbl_titulo.pack(pady=(0, 10))
        
        lbl_instrucciones = ttk.Label(self.root, text="Selecciona los síntomas que presentas:")
        lbl_instrucciones.pack(anchor="w", pady=(0, 10))
        
        frame_lista = ttk.Frame(self.root)
        frame_lista.pack(fill="both", expand=True)
        
        canvas = tk.Canvas(frame_lista)
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=canvas.yview)
        
        self.frame_sintomas = ttk.Frame(canvas)
        self.frame_sintomas.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.frame_sintomas, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        

        for sintoma in self.sintomas:
            var = tk.BooleanVar()
            self.variables_sintomas[sintoma] = var
            texto_sintoma = sintoma.replace('_', ' ').capitalize()
            chk = ttk.Checkbutton(self.frame_sintomas, text=texto_sintoma, variable=var)
            chk.pack(anchor="w", pady=2)
            

        btn_diagnosticar = ttk.Button(self.root, text="Realizar Diagnóstico", command=self.ejecutar_diagnostico)
        btn_diagnosticar.pack(pady=20)
  
        lbl_resultado = ttk.Label(self.root, text="Resultados:", font=("Helvetica", 12, "bold"))
        lbl_resultado.pack(anchor="w")
        
        self.txt_resultado = tk.Text(self.root, height=8, width=50, state="disabled", font=("Helvetica", 10))
        self.txt_resultado.pack(fill="both", expand=True, pady=(5, 0))

    def ejecutar_diagnostico(self):
        sintomas_seleccionados = [s for s, var in self.variables_sintomas.items() if var.get()]
        
        if not sintomas_seleccionados:
            messagebox.showwarning("Advertencia", "Debes seleccionar al menos un síntoma.")
            return
            
        posibles_enfermedades = diagnosticar(self.prolog, sintomas_seleccionados)
        
        self.txt_resultado.config(state="normal")
        self.txt_resultado.delete(1.0, tk.END)
        
        if posibles_enfermedades:
            self.txt_resultado.insert(tk.END, "Podrías tener:\n\n")
            for diag in posibles_enfermedades:
                enfermedad = diag["enfermedad"].replace('_', ' ').capitalize()
                texto = f" • {enfermedad} (Nivel de coincidencia: {diag['coincidencias']} síntomas)\n"
                self.txt_resultado.insert(tk.END, texto)
            self.txt_resultado.insert(tk.END, "\nNota: Esto es solo un simulador.")
        else:
            self.txt_resultado.insert(tk.END, "No se encontró ninguna enfermedad que\ncoincida con tus síntomas.")
            
        self.txt_resultado.config(state="disabled")

def main():
    prolog = Prolog()
    cargar_conocimiento(prolog)
    
    todos_sintomas = obtener_todos_los_sintomas(prolog)
    if not todos_sintomas:
        print("No se encontraron síntomas en la base de conocimiento.")
        return

    root = tk.Tk()
    
    try:
        root.tk.call("source", "azure.tcl")
        root.tk.call("set_theme", "light")
    except:
        pass 
        
    app = SistemaExpertoGUI(root, prolog, todos_sintomas)
    root.mainloop()

if __name__ == "__main__":
    main()
