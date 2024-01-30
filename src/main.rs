use druid::widget::{Button, Flex, TextBox, CrossAxisAlignment};
use druid::{AppLauncher, Data, Lens, LocalizedString, Widget, WindowDesc, WidgetExt};

const WINDOW_TITLE: LocalizedString<EditState> = LocalizedString::new("blink");
const WINDOW_SIZE: (f64, f64) = (600.0, 600.0);
const MENU_HEIGHT: f64 = 40.0;
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
    let menu = Flex::row()
        .cross_axis_alignment(CrossAxisAlignment::Center)
        .with_child(Button::new("File")
            .fix_height(MENU_HEIGHT))
        .with_spacer(10.0)
        .with_child(Button::new("Edit")
            .fix_height(MENU_HEIGHT));

    let textbox = TextBox::multiline()
        .with_line_wrapping(false)
        .lens(EditState::text)
        .fix_height(WINDOW_SIZE.0 - TEXTBOX_PADDING - MENU_HEIGHT)
        .fix_width(WINDOW_SIZE.1 - TEXTBOX_PADDING - MENU_HEIGHT);

    Flex::column()
        .with_child(menu)
        .with_spacer(TEXTBOX_PADDING)
        .with_child(textbox)
        .center()
}
