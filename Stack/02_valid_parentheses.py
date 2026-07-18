def is_valid(s):
    stack = []  
    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # 1. Hum string 's' ke har bracket (char) par loop chalayenge
    for char in s:
        # 2. Agar char closing bracket hai (dictionary ki key hai)
        if char in mapping:
            # Stack se top element nikaalo agar khali nahi hai, nahi toh dummy '#' le lo
            if stack:
                top_element = stack.pop()
            else:
                top_element = '#'
            
            # Agar top element aur sahi opening bracket match nahi karte, toh turant False!
            if top_element != mapping[char]:
                return False
        else:
            # 3. Agar opening bracket hai, toh stack mein push (append) kar do
            stack.append(char)

    # 4. Loop ke bahar check karo: kya stack khali bacha?
    # Agar stack khali hai (len == 0), toh True return hoga, nahi toh False.
    return len(stack) == 0

# Test karke dekhte hain!
test_string = "([{}])"
print("Result :", is_valid(test_string)) # Output: True
