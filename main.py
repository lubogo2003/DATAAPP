import flet as ft

def main(page: ft.Page):
    page.title = "Simple Counter App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Counter value
    counter = ft.Ref[ft.Text]()

    # Function to increment the counter
    def increment_counter(e):
        counter.current.value = str(int(counter.current.value) + 1)
        page.update()

    # Add widgets to the page
    page.add(
        ft.Text("Counter App", size=30, weight=ft.FontWeight.BOLD),
        ft.Text(ref=counter, value="0", size=50),
        ft.ElevatedButton("Increment", on_click=increment_counter),
    )

# Run the app
ft.app(target=main)
