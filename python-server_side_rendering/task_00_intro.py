import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(i, dict) for i in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Iterate over the list of attendees
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders in the template
        invitation = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )

        # Generate output file name
        output_filename = f'output_{index}.txt'

        # Write the processed template to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(invitation)

        print(f"Generated invitation for {attendee.get('name', 'N/A')} in {output_filename}")

# Testing the function
if __name__ == "__main__":
    # Read the template from a file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)

