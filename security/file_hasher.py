import hashlib
import os

def generate_file_hash():
    print("=" * 60)
    print("          GERADOR DE HASH SHA-256 (AUDITORIA)")
    print("=" * 60)
    
    # Solicita o arquivo ao usuário
    file_path = input("\nArraste o arquivo aqui e aperte Enter: ").strip('"')

    if not os.path.exists(file_path):
        print(f"\n[ERRO] O arquivo não foi encontrado: {file_path}")
        return

    try:
        # Cria o objeto de hash SHA-256
        sha256_hash = hashlib.sha256()
        
        # Lê o arquivo em pedaços (chunks) para não travar o PC com arquivos grandes
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        resultado = sha256_hash.hexdigest()
        
        print("\n" + "-" * 60)
        print(f"ARQUIVO: {os.path.basename(file_path)}")
        print(f"HASH SHA-256: \033[1;33m{resultado}\033[0m")
        print("-" * 60)
        print("\nEste código é único. Se o arquivo mudar 1 bit, o hash será outro.")

    except Exception as e:
        print(f"\n[ERRO] Falha ao processar arquivo: {e}")

if __name__ == "__main__":
    generate_file_hash()
    input("\nPressione Enter para sair...")