def dr_compiler(source_code):
    lines = source_code.split('\n')
    for line in lines:
        if line.startswith("fn"):
            print(f"[DR#] Найдена функция: {line[3:]}")
        if "let" in line:
            print(f"[DR#] Объявление переменной: {line.strip()}")
        if "asm" in line:
            print("[DR#] ВНИМАНИЕ: Вход в режим ASM (NASM)")

# Тест нового синтаксиса
code = """
fn main
    let x = 10
    asm
"""
dr_compiler(code)
