// core.rs - Сердце твоего компилятора
pub struct DrCompiler {
    pub version: String,
}

impl DrCompiler {
    pub fn new() -> Self {
        Self {
            version: String::from("0.1.0-alpha"),
        }
    }

    pub fn run(&self, file_path: &str) {
        if file_path.ends_with(".drs") {
            println!("[DR# Engine] Запуск файла: {}", file_path);
            // Тут будет вызов твоего NASM для ASM-вставок
        } else {
            eprintln!("Ошибка: Ожидался файл .drs");
        }
    }
}
