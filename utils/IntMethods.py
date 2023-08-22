def format_memory_size(size_in_bytes):
    # Define the unit sizes and labels
    units = ["B", "KB", "MB", "GB"]
    base = 1024

    # Find the appropriate unit size
    size = size_in_bytes
    unit_index = 0
    while size >= base and unit_index < len(units) - 1:
        size /= base
        unit_index += 1

    # Format the size with two decimal places
    formatted_size = "{:.2f}".format(size)

    # Append the unit label
    formatted_size += units[unit_index]

    return formatted_size


def format_seconds(number) -> str:
    return f"{round(number, 2)}s"
