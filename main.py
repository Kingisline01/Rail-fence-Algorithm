def rail_fence_encrypt(text, key):
    # Create an array to store the rails
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    
    # To find the direction
    direction_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        # Reverse the direction if we've reached the top or bottom rail
        if (row == 0) or (row == key - 1):
            direction_down = not direction_down
        
        # Fill the rail array with characters of the text
        rail[row][col] = text[i]
        col += 1
        
        # Move to the next row
        if direction_down:
            row += 1
        else:
            row -= 1
    
    # Create the ciphertext using the rail array
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

# getting the input from the user
text = input("Enter the text: ")

# getting the key/depth from the user
key = int(input("Enter the Key value"))

text = text
key = key
encrypted_text = rail_fence_encrypt(text, key)
print("Encrypted Text: ", encrypted_text)
