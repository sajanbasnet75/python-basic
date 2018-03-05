# Define gibberish
def gibberish(*args):#argu passed will acts as tuples args(luke,leia,han)..
    """Concatenate strings in *args together."""

    # Initialize an empty string: hodgepodge
    hodgepodge=""       

    # Concatenate the strings in args
    for word in args:
        hodgepodge += word+"  "

    # Return hodgepodge
    return hodgepodge

# Call gibberish() with one string: one_word
one_word = gibberish("hello")

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)
