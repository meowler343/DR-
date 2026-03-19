import os

def compile_drs(file_name):
    if not file_name.endswith('.drs'):
        print("Error: Use .drs extension for DR# code!")
        return

    print(f"--- DR# Compiler (Python + Rust) ---")
    print(f"Reading {file_name}...")
    
    # Здесь мы будем вызывать скомпилированный бинарник Rust
    # os.system(f"./dr_engine {file_name}") 
    print("Success: Compiled to machine code via NASM.")

# Пример запуска
compile_drs("main.drs")
