

def scope_imp():
    def local_imp():
        text = "local variable"
        print(text)

    def nonlocal_imp():
        nonlocal text
        text = "non local variable"

    def global_imp():
        global text
        text = "global variable"
    
    text = "variable"

    local_imp()
    print("local scope:", text)
    nonlocal_imp()
    print("non local:",text)
    global_imp()
    print("global:",text)


scope_imp()
print(text)