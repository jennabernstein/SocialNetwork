import PySimpleGUI as sg
from user import Profile

# Create a list of profile objects
profile_list = [
    Profile("user1", "John Doe", "john@example.com"),
    Profile("user2", "Alice Smith", "alice@example.com"),
    Profile("user3", "Bob Johnson", "bob@example.com"),
]

# Define the GUI layout for the add section
add_layout = [
    [sg.Text("Add New Profile", font=("Helvetica", 16), justification="center")],
    [sg.Text("Username:"), sg.InputText("", key="-ADD-USERNAME-")],
    [sg.Text("Name:"), sg.InputText("", key="-ADD-NAME-")],
    [sg.Text("Email:"), sg.InputText("", key="-ADD-EMAIL-")],
    [sg.Button("Add", key="-ADD-NEW-", size=(10, 1)), sg.Button("Cancel", key="-CANCEL-ADD-", size=(10, 1))],
]

# Define the GUI layout
profile_layout = [
    [sg.Text("Profile Information", font=("Helvetica", 16), justification="center", key="-PROFILE-INFO-", visible=False)],
    [sg.Text("Username:", visible=False), sg.Text("", key="-USERNAME-", visible=False)],
    [sg.Text("Name:", visible=False), sg.Text("", key="-NAME-", visible=False)],
    [sg.Text("Email:", visible=False), sg.Text("", key="-EMAIL-", visible=False)],  # Display the email
    [sg.Text("Number of Friends:", visible=False), sg.Text("", key="-NUM-FRIENDS-", visible=False)],  # New label for number of friends
    [sg.Button("Show Friends", key="-FRIENDS-", size=(15, 1), visible=False),
    sg.Button("Hide Friends", key="-HIDE-FRIENDS-", size=(15, 1), visible=False)], 
    [sg.Button("Edit", key="-EDIT-", size=(10, 1), visible=False)],
]

friends_layout = [
    [sg.Text("Friends", font=("Helvetica", 16), justification="center", key="-FRIENDS-INFO-", visible=False)],
    [sg.Listbox(values=[], size=(20, 10), key="-FRIEND-LIST-", visible=False, select_mode="LISTBOX_SELECT_MODE_SINGLE")]
]

edit_layout = [
    [sg.Text("Edit Profile", font=("Helvetica", 16), justification="left", key="-EDIT-INFO-", visible=False)],
    [sg.Text("Username:"), sg.InputText("", key="-EDIT-USERNAME-", visible=False)],
    [sg.Text("Name:"), sg.InputText("", key="-EDIT-NAME-", visible=False)],
    [sg.Text("Email:"), sg.InputText("", key="-EDIT-EMAIL-", visible=False)],
    [sg.Button("Save Changes", key="-SAVE-", size=(15, 1), visible=False), sg.Button("Cancel", key="-CANCEL-EDIT-", size=(10, 1), visible=False)],
]

# ... (Rest of your code remains unchanged) ...

# Define the GUI layout
layout = [
    [
        sg.Text("Enter Username to Search:"),
        sg.InputText(key="-SEARCH-"),
        sg.Button("Search"),
    ],
    [
        sg.Listbox(
            values=[profile.username for profile in profile_list],
            size=(20, 10),
            key="-PROFILE LIST-",
            enable_events=True,
            select_mode="LISTBOX_SELECT_MODE_SINGLE"
        ),
        sg.Column(profile_layout, key="-PROFILE-", element_justification="left"),
        sg.Column(edit_layout, key="-EDIT PROFILE-", element_justification="left", visible=False),
        sg.Column(friends_layout, key="-FRIENDS-", element_justification="left", visible=True),
    ],
    [
        sg.Button("Add New Profile", key="-ADD-", size=(15, 1)),
    ],
    [
        sg.Column(add_layout, key="-ADD-SECTION-", element_justification="left", visible=False),
    ],
]

# Create the window
window = sg.Window("Profile Search", layout)

selected_profile = None  # To keep track of the selected profile
original_values = {}  # To store the original profile values
friends_visible = True  # Track if friends list is visible

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Search":
        search_term = values["-SEARCH-"].strip().lower()  # Get the search term (lowercased for case-insensitive search)

        # Filter profiles based on the search term
        matching_profiles = [profile for profile in profile_list if search_term in profile.username.lower()]

        # Update the profile list in the GUI with usernames
        profile_usernames = [profile.username for profile in matching_profiles]
        window["-PROFILE LIST-"].update(values=profile_usernames)

        # Clear the profile details when a new search is performed
        window["-PROFILE-INFO-"].update(visible=False)
        window["-USERNAME-"].update(visible=False)
        window["-NAME-"].update(visible=False)
        window["-EMAIL-"].update(visible=False)  # Hide the email
        window["-NUM-FRIENDS-"].update(visible=False)  # Hide the number of friends label
        window["-FRIENDS-"].update(visible=False)  # Hide the "Show Friends" button
        window["-HIDE-FRIENDS-"].update(visible=False)  # Hide the "Hide Friends" button
        window["-EDIT-"].update(visible=False)

    elif event == "-PROFILE LIST-":
        if values["-PROFILE LIST-"]:
            username = values["-PROFILE LIST-"][0]

            # Find the selected profile in the profile_list
            selected_profile = next((profile for profile in profile_list if profile.username == username), None)

            # Update the profile details in the GUI
            if selected_profile:
                # Display profile information next to the labels
                window["-PROFILE-INFO-"].update(visible=True)
                window["-USERNAME-"].update("Username: " + selected_profile.username, visible=True)
                window["-NAME-"].update("Name: " + selected_profile.name, visible=True)
                window["-EMAIL-"].update("Email: " + selected_profile.email, visible=True)  # Display the email
                window["-NUM-FRIENDS-"].update("Number of Friends: " + str(selected_profile.getNumFriends()), visible=True)  # Show number of friends
                window["-FRIENDS-"].update(visible=True)  # Show the "Show Friends" button
                window["-EDIT-"].update(visible=True)

                # Store the original profile values
                original_values["-USERNAME-"] = selected_profile.username
                original_values["-NAME-"] = selected_profile.name
                original_values["-EMAIL-"] = selected_profile.email

                # Make the "Edit" button visible
                window["-EDIT-"].update(visible=True)
                window["-EDIT PROFILE-"].update(visible=False)  # Hide the edit profile section

                # Show the "Hide Friends" button
                window["-HIDE-FRIENDS-"].update(visible=False)

    elif event == "-EDIT-":
        if selected_profile:
            # Populate the edit view with the original profile values
            window["-EDIT-INFO-"].update(visible=True)
            window["-EDIT-USERNAME-"].update(original_values["-USERNAME-"], visible=True)
            window["-EDIT-NAME-"].update(original_values["-NAME-"], visible=True)
            window["-EDIT-EMAIL-"].update(original_values["-EMAIL-"], visible=True)

            # Hide the profile information when the "Edit" button is clicked
            window["-PROFILE-INFO-"].update(visible=False)
            window["-USERNAME-"].update(visible=False)
            window["-NAME-"].update(visible=False)
            window["-EMAIL-"].update(visible=False)  # Hide the email
            window["-NUM-FRIENDS-"].update(visible=False)  # Hide the number of friends label
            window["-FRIENDS-"].update(visible=False)  # Hide the "Show Friends" button
            window["-HIDE-FRIENDS-"].update(visible=False)  # Hide the "Hide Friends" button
            window["-EDIT-"].update(visible=False)  # Hide the edit button

            # Show the editable input fields
            window["-EDIT PROFILE-"].update(visible=True)
            window["-SAVE-"].update(visible=True)
            window["-CANCEL-EDIT-"].update(visible=True)

    elif event == "-SAVE-":
        if selected_profile:
            # Update the profile with changes if the "Save Changes" button is clicked
            selected_profile.setUsername(values["-EDIT-USERNAME-"])
            selected_profile.setName(values["-EDIT-NAME-"])
            selected_profile.setEmail(values["-EDIT-EMAIL-"])

            # Update the profile list in the GUI with usernames
            profile_usernames = [profile.username for profile in profile_list]
            window["-PROFILE LIST-"].update(values=profile_usernames)

            # Update the original values
            window["-PROFILE-INFO-"].update(visible=True)
            original_values["-USERNAME-"] = selected_profile.username
            original_values["-NAME-"] = selected_profile.name
            original_values["-EMAIL-"] = selected_profile.email

            # Show a message indicating changes have been saved
            sg.popup("Changes saved successfully!")

            # Show the profile details and hide the editable input fields
            window["-USERNAME-"].update(selected_profile.username, visible=True)
            window["-NAME-"].update(selected_profile.name, visible=True)
            window["-EMAIL-"].update("Email: " + selected_profile.email, visible=True)  # Display the email
            window["-NUM-FRIENDS-"].update("Number of Friends: " + str(selected_profile.getNumFriends()), visible=True)  # Show number of friends
            window["-FRIENDS-"].update(visible=True)  # Show the "Show Friends" button
            window["-HIDE-FRIENDS-"].update(visible=True)  # Show the "Hide Friends" button
            window["-EDIT-"].update(visible=True)

            # Hide the editable input fields and "Save Changes" button
            window["-EDIT PROFILE-"].update(visible=False)
            window["-SAVE-"].update(visible=False)
            window["-CANCEL-EDIT-"].update(visible=False)

    elif event == "-CANCEL-EDIT-":
        if selected_profile:
            # Revert the input fields to their original values
            window["-PROFILE-INFO-"].update(visible=True)
            window["-EDIT-USERNAME-"].update(original_values["-USERNAME-"], visible=True)
            window["-EDIT-NAME-"].update(original_values["-NAME-"], visible=True)

            # Show the profile details and hide the editable input fields
            window["-USERNAME-"].update(selected_profile.username, visible=True)
            window["-NAME-"].update(selected_profile.name, visible=True)
            window["-EMAIL-"].update("Email: " + selected_profile.email, visible=True)  # Display the email
            window["-NUM-FRIENDS-"].update("Number of Friends: " + str(selected_profile.getNumFriends()), visible=True)  # Show number of friends
            window["-FRIENDS-"].update(visible=True)  # Show the "Show Friends" button
            window["-HIDE-FRIENDS-"].update(visible=True)  # Show the "Hide Friends" button
            window["-EDIT-"].update(visible=True)

            # Hide the editable input fields and "Save Changes" button
            window["-EDIT PROFILE-"].update(visible=False)
            window["-SAVE-"].update(visible=False)
            window["-CANCEL-EDIT-"].update(visible=False)

    elif event == "-FRIENDS-":
        if selected_profile:
            friends = selected_profile.getFriends()
            window["-FRIEND-LIST-"].update(values=friends, visible=True)
            window["-FRIENDS-"].update(visible=False)
            window["-HIDE-FRIENDS-"].update(visible=True)

    elif event == "-HIDE-FRIENDS-":
        if selected_profile:
            # Hide the friend list when the "Hide Friends" button is clicked
            window["-FRIEND-LIST-"].update(visible=False)
            window["-HIDE-FRIENDS-"].update(visible=False)
            window["-FRIENDS-"].update(visible=True)

    elif event == "-ADD-":
        # Toggle the visibility of the "Add New Profile" section
        window["-ADD-"].update(visible=False)
        window["-ADD-SECTION-"].update(visible=True)

    elif event == "-CANCEL-ADD-":
        # Clear the input fields and hide the "Add New Profile" section
        window["-ADD-USERNAME-"].update("")
        window["-ADD-NAME-"].update("")
        window["-ADD-EMAIL-"].update("")
        window["-ADD-SECTION-"].update(visible=False)
        window["-ADD-"].update(visible=True)

    elif event == "-ADD-NEW-":
        # Get the values from the input fields for the new profile
        new_username = values["-ADD-USERNAME-"]
        new_name = values["-ADD-NAME-"]
        new_email = values["-ADD-EMAIL-"]
        profile_usernames = [profile.username for profile in profile_list]

        # Check if any of the fields are empty
        if not new_username or not new_name:
            sg.popup("Please fill in all required fields (Username and Name) to add a new profile.")
        elif new_username in profile_usernames:
            sg.popup("Username already being used. Choose a new one.")
        else:
            # Create a new profile object and add it to the profile list
            new_profile = Profile(new_username, new_name, new_email)
            profile_list.append(new_profile)

            # Clear the input fields
            window["-ADD-USERNAME-"].update("")
            window["-ADD-NAME-"].update("")
            window["-ADD-EMAIL-"].update("")

            # Show a message indicating the new profile has been added
            sg.popup("New profile added successfully!")

            # Update the profile list in the GUI with the new username
            profile_usernames.append(new_profile.username)
            window["-PROFILE LIST-"].update(values=profile_usernames)

            # Hide the "Add New Profile" section after adding a profile
            window["-ADD-"].update(visible=True)
            window["-ADD-SECTION-"].update(visible=False)

window.close()
