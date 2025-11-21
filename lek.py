def is_even(n):
    if(n % 2 == 0):
        return "jämnt"
    else:
        return "udda"
    
tal = 3
x = is_even(tal)
print(f"talet {tal} är {x}")