

def scope_imp():
    def local_imp():
        text = "local variable"
        print(text)

    def nonlocal_imp():
        nonlocal text
        text = "non local variable"
        print(text)

    def global_imp():
        global text
        text = "global variable"
        print(text)
    
    text = "variable"

    local_imp()
    print("local scope:", text)
    nonlocal_imp()
    print("non local:",text)
    global_imp()
    print("global:",text)


text = "global scope"
scope_imp()
print(text)