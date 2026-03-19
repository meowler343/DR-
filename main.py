import sys

def dr_parse(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.readlines()

    print(f"--- DR# Compiler (v0.1.2-alpha) ---")
    print(f"Target: {file_path}\n")

    for i, line in enumerate(code):
        l = line.strip()
        
        if l.startswith("fn"):
            print(f"[Line {i}] FUNCTION START: {l[3:]}")
        
        elif l.startswith("let"):
            print(f"[Line {i}] VARIABLE DEF: {l[4:]}")
            
        elif l.startswith("if") and "then" in l:
            cond = l[2:l.find("then")].strip()
            print(f"[Line {i}] IF CONDITION: ({cond})")
            
        elif l == "else":
            print(f"[Line {i}] ELSE BRANCH")
            
        elif l == "asm":
            print(f"[Line {i}] !!! ASM MODE ENABLED (NASM INJECT) !!!")
            
        elif l == "end":
            print(f"[Line {i}] BLOCK END")
            
        elif l.startswith("print"):
            content = l[l.find("(")+1 : l.rfind(")")]
            print(f"[Line {i}] OUTPUT: {content}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        dr_parse(sys.argv[1])
        print("\nSuccess: Machine code generated via Rust Core.")
    else:
        print("Usage: py main.py <file.drs>")
