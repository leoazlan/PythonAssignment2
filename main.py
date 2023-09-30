"""
Name:Mohamed Azlan
Date: 25/09/2023
Brief Project Description: Kivy GUI program to track travel places, load them from a csv file, and display them as buttons.
Users can mark places as visited/unvisited and add new places.
GitHub URL: https://github.com/JCUS-CP1404/cp1404-travel-tracker-assignment-2-leoazlan
"""
# Create your main program in this file, using the TravelTrackerApp class

# Create your main program in this file, using the TravelTrackerApp class
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

# Import Place and PlaceCollection classes from respective modules
from place import Place
from placecollection import PlaceCollection

# Constants representing the visited status
UNVISITED = "n"  # This represents an unvisited place
VISITED = "v"  # This represents a visited place

KV = """
BoxLayout:
    orientation: "vertical"
    BoxLayout:
        orientation: "horizontal"

        BoxLayout:
            orientation: "vertical"
            size_hint_x: 0.3

            Label:
                text: "Sort by:"
                size_hint_y: 0.1

            Spinner:
                id: sort_spinner
                size_hint_y: 0.1
                text: "Name"
                values: ("Name", "Country", "Priority", "Visited")

            Label:
                text: "Add New Place..."
                size_hint_y: 0.1
            Label:
                text: "Name:"
                size_hint_y: 0.1
            TextInput:
                id: name_input
                multiline: False
                size_hint_y: 0.1
            Label:
                text: "Country:"
                size_hint_y: 0.1
            TextInput:
                id: country_input
                multiline: False
                size_hint_y: 0.1
            Label:
                text: "Priority:"
                size_hint_y: 0.1
            TextInput:
                id: priority_input
                multiline: False
                size_hint_y: 0.1

            Button:
                text: "Add Place"
                size_hint_y: 0.1
                on_release: app.add_place()

            Button:
                text: "Clear"
                size_hint_y: 0.1
                on_release: app.clear_fields()
        BoxLayout:
            orientation: "vertical"
            Label:
                id: top_status_label
                size_hint_y: 0.1
                text: "Places to visit: 0"
            ScrollView:
                id: scroll_view
                GridLayout:
                    id: places_grid
                    cols: 1
                    size_hint_y: None
                    height: self.minimum_height
                    row_default_height: 150
                    row_force_default: True
            Label:
                id: bottom_status_label
                size_hint_y: 0.1
                text: "Welcome to Travel Tracker"
"""


class TravelTrackerApp(App):
    def build(self):
        self.title = "Travel Tracker"
        self.root = Builder.load_string(KV)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places('places.csv')
        self.place_collection.sort('name')
        self.root.ids.sort_spinner.bind(text=self.sort_text_change)
        self.update_grid()
        return self.root

    def clear_fields(self):
        self.root.ids.name_input.text = ''
        self.root.ids.country_input.text = ''
        self.root.ids.priority_input.text = ''

    def sort_text_change(self, spinner, text):
        self.place_collection.sort(text.lower())
        self.update_grid()

    def update_grid(self):
        self.root.ids.places_grid.clear_widgets()
        i = 0
        for place in self.place_collection.places:
            status = " (Visited)" if place.visited == VISITED else ""
            if status == "":
                i += 1
            btn_text = f"{place.name} in {place.country}, priority {place.priority}{status}"
            btn = Button(text=btn_text, background_color=(0.2, 0.2, 0.2, 1) if status == " (Visited)" else (0, 1, 1, 1))
            btn.bind(on_release=self.change_place_status)
            self.root.ids.places_grid.add_widget(btn)
        self.root.ids.top_status_label.text = f'Places to visit: {i}'

    def change_place_status(self, instance):
        btn_text = instance.text
        action = "visited" if " (Visited)" not in btn_text else "unvisited"
        place_name = btn_text.split(" in ")[0]
        for place in self.place_collection.places:
            if place.name == place_name:
                place.visited = VISITED if action == "visited" else UNVISITED
                if action == "visited":
                    self.root.ids.bottom_status_label.text = f'You visited {place_name}. Great travelling!'
                else:
                    self.root.ids.bottom_status_label.text = f'You need to visit {place_name}.'
                break
        self.place_collection.sort(self.root.ids.sort_spinner.text.lower())
        self.update_grid()
        self.place_collection.save_places()

    def add_place(self):
        name = self.root.ids.name_input.text
        country = self.root.ids.country_input.text
        priority = self.root.ids.priority_input.text
        try:
            priority = int(priority)
        except ValueError:
            self.root.ids.bottom_status_label.text = 'Please input a number for priority'
            return
        if not name.strip() or not country.strip() or priority < 1:
            self.root.ids.bottom_status_label.text = 'All columns must be filled, and priority must be greater than zero.'
            return
        self.place_collection.add_place(Place(name, country, priority, UNVISITED))
        self.place_collection.sort(self.root.ids.sort_spinner.text.lower())
        self.update_grid()
        self.place_collection.save_places()
        self.clear_fields()
        self.root.ids.bottom_status_label.text = 'Place added successfully. Welcome to Travel Tracker!'


if __name__ == '__main__':
    TravelTrackerApp().run()
