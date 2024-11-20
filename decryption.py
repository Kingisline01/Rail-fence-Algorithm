def rail_fence_decrypt(cipher, key):
    # Create an array to store the rails
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    
    # To find the direction
    direction_down = None
    row, col = 0, 0
    
    # Mark the positions in the rail array
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
    
    # Fill the rail array with characters from the ciphertext
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (rail[i][j] == '*') and (index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1
    
    # Read the decrypted text using the rail array
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False
        
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        
        if direction_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


encrypted_text = input("Enter the encrypted text: ")
key = int(input("Enter the key: "))

cipher = encrypted_text
decrypted_text = rail_fence_decrypt(cipher, key)
print("Decrypted Text: ", decrypted_text)
