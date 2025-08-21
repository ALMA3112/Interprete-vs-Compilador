import subprocess
import re
import matplotlib.pyplot as plt

def run_and_parse(source, exe, label):
    # Compilar el código en C
    subprocess.run(["gcc", "-O3", "-std=c11", "-o", exe, source, "-lm"], check=True)
    
    # Ejecutar el programa compilado
    result = subprocess.run(["./" + exe], capture_output=True, text=True, check=True)
    lines = result.stdout.strip().split("\n")
    
    ns, tiempos, memorias = [], [], []
    
    for i in range(0, len(lines), 2):
        match_time = re.search(r"n=(\d+)\s+Tiempo = ([\d.]+)", lines[i])
        match_mem = re.search(r"n=(\d+)\s+Memoria = ([\d.]+)", lines[i+1])
        
        if match_time and match_mem:
            n = int(match_time.group(1))
            tiempo = float(match_time.group(2))
            memoria = float(match_mem.group(2))
            
            ns.append(n)
            tiempos.append(tiempo)
            memorias.append(memoria)
    
    # Gráfica tiempo
    plt.figure()
    plt.plot(ns, tiempos, marker="o", color="red", label=label)
    plt.xscale("log")
    plt.xlabel("Datos (n)")
    plt.ylabel("Tiempo (s)")
    plt.title(f"{label} - Datos vs Tiempo")
    plt.grid(True)
    plt.legend()
    plt.savefig("Recursivo_Tiempo.png")
    
    # Gráfica memoria
    plt.figure()
    plt.plot(ns, memorias, marker="o", color="red", label=label)
    plt.xscale("log")
    plt.xlabel("Datos (n)")
    plt.ylabel("Memoria (MB)")
    plt.title(f"{label} - Datos vs Memoria")
    plt.grid(True)
    plt.legend()
    plt.savefig("Recursivo_Memoria.png")
    
    print("✅ Gráficas generadas: Recursivo_Tiempo.png y Recursivo_Memoria.png")

def main():
    run_and_parse("Recursivo.c", "Recursivo", "C Recursivo")

if __name__ == "__main__":
    main()
