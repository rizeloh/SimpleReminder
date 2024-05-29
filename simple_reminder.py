import time
import datetime

def set_reminder(reminder_time, message):
    """
    Set a reminder that will display a message at the specified time.

    Parameters:
    reminder_time (str): The time to trigger the reminder in HH:MM format.
    message (str): The reminder message to display.

    Returns:
    None
    """
    # Convert the reminder time to a datetime object
    now = datetime.datetime.now()
    reminder_time = datetime.datetime.strptime(reminder_time, "%H:%M").replace(
        year=now.year, month=now.month, day=now.day
    )

    # If the reminder time has already passed today, set it for tomorrow
    if reminder_time < now:
        reminder_time = reminder_time + datetime.timedelta(days=1)

    print(f"Reminder set for {reminder_time.strftime('%Y-%m-%d %H:%M')}")

    # Calculate the time to sleep until the reminder
    time_to_sleep = (reminder_time - now).total_seconds()
    
    # Sleep until the reminder time
    time.sleep(time_to_sleep)

    # Display the reminder message
    print(f"Reminder: {message}")

if __name__ == "__main__":
    # Example usage
    reminder_time = "15:30"  # Set the reminder time in HH:MM format
    message = "Time to take a break!"
    set_reminder(reminder_time, message)
