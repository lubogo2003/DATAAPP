import flet as ft

def main(page: ft.Page):
    page.title = "Simple Flet App"
    
    # Create a label
    label = ft.Text(value="Hello, Flet!", size=30)
    
    # Function to handle button click
    def on_button_click(event):
        label.value = "Button Clicked!"
        page.update()
    
    # Create a button
    button = ft.Button(text="Click Me", on_click=on_button_click)
    
    # Add the label and button to the page
    page.add(label, button)

# Run the app
ft.app(target=main)
