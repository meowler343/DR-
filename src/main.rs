use iced::widget::{button, column, container, text_editor, text, row};
use iced::{Application, Command, Element, Settings, Theme, executor};

pub fn main() -> iced::Result {
    DrStudio::run(Settings::default())
}

struct DrStudio {
    content: text_editor::Content,
    status: String,
}

#[derive(Debug, Clone)]
enum Message {
    Edit(text_editor::Action),
    RunCode,
}

impl Application for DrStudio {
    type Executor = executor::Default;
    type Message = Message;
    type Theme = Theme;
    type Flags = ();

    fn new(_flags: ()) -> (Self, Command<Message>) {
        (
            Self {
                content: text_editor::Content::new(),
                status: String::from("Система DR# готова..."),
            },
            Command::none(),
        )
    }

    fn title(&self) -> String {
        String::from("DR# IDE - Expert Chainsaw")
    }

    fn update(&mut self, message: Message) -> Command<Message> {
        match message {
            Message::Edit(action) => {
                self.content.perform(action);
                Command::none()
            }
            Message::RunCode => {
                self.status = String::from("Запуск компилятора...");
                // Здесь будет вызов твоего main.py через std::process::Command
                Command::none()
            }
        }
    }

    fn view(&self) -> Element<Message> {
        let editor = text_editor(&self.content)
            .on_action(Message::Edit);

        let controls = row!.spacing(20);

        container(column![controls, editor].spacing(10))
            .padding(20)
            .into()
    }
}
