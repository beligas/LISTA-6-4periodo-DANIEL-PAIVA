import subprocess

def listar_pcbelgas():
    try:
        resultado_pcbelgas = subprocess.check_output('net user', shell=True, text=True)

        linhas_pcbelgas = resultado_pcbelgas.splitlines()
        linhas_pcbelgas = linhas_pcbelgas[4:-2]  

        usuarios_brutos_pcbelgas = " ".join(linhas_pcbelgas)

        usuarios_pcbelgas = usuarios_brutos_pcbelgas.split()

        return usuarios_pcbelgas

    except subprocess.CalledProcessError as e:
        return []

def main():
    usuarios_pcbelgas = listar_pcbelgas()
    for usuario_pcbelgas in usuarios_pcbelgas:
        print(usuario_pcbelgas)

if __name__ == "__main__":
    main()
