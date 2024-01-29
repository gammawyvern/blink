use druid::widget::{Flex, TextBox};
use druid::{AppLauncher, Data, Lens, LocalizedString, Widget, WindowDesc, WidgetExt};

const WINDOW_TITLE: LocalizedString<EditState> = LocalizedString::new("blink");
const WINDOW_SIZE: (f64, f64) = (600.0, 600.0);
const TEXTBOX_PADDING: f64 = 20.0;

#[derive(Clone, Data, Lens)]
struct EditState {
    text: String,
}

fn main() {
    let main_window = WindowDesc::new(build_root_widget())
        .title(WINDOW_TITLE)
        .window_size(WINDOW_SIZE)
        .show_titlebar(false)
        .resizable(false);

    let initial_state = EditState {
        text: "".into(),
    };

    AppLauncher::with_window(main_window)
        .launch(initial_state)
        .expect("Failed to launch application");
}

fn build_root_widget() -> impl Widget<EditState> {
    let textbox = TextBox::multiline()
        .with_line_wrapping(false)
        .lens(EditState::text)
        .fix_height(WINDOW_SIZE.0 - TEXTBOX_PADDING)
        .fix_width(WINDOW_SIZE.1 - TEXTBOX_PADDING);

    Flex::column()
        .with_child(textbox)
        .center()
}
