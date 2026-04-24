# task_00_intro.py
import logging

logging.basicConfig(level=logging.ERROR)

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        logging.error(f"Invalid input type: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error(f"Invalid input type: attendees must be a list of dictionaries")
        return

    # Check for empty inputs
    if not template:
        logging.error("Template is empty, no output files generated.")
        return
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        content = template

        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder)
            if value is None:
                value = "N/A"
            content = content.replace(f"{{{placeholder}}}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, 'w') as f:
            f.write(content)
