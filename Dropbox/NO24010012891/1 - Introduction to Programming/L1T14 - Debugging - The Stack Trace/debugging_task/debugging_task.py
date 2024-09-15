# Defining a function that prints the values of specified keys from a dictionary.
def print_values_of(dictionary, *keys):
    for key in keys:
        if key in dictionary:
            print(dictionary[key])
        else:
            print(f"Key '{key}' not found in the dictionary.")

# Example usage of the phrases to be used.
simpson_catch_phrases = {
    "lisa": "BAAAAAART!",
    "bart": "Eat My Shorts!",
    "marge": "Mmm~mmmmm",
    "homer": "d'oh!",
    "maggie": "(Pacifier Suck)"
}

# Print values for specified keys
print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')
