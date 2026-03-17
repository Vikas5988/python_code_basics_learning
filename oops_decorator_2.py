# DECORATOR FUNCTION — accepts any function 'fx' as argument
def greet(fx):
    
    # *args   → captures any number of Positional arguments  (e.g. 11, 2)
    # **kwargs → captures any number of Keyword arguments    (e.g. a=11, b=2)
    # Together they make mfx() flexible enough to wrap ANY function, regardless of its parameters
    def mfx(*args, **kwargs):
        print("Welcome to Python")
        
        fx(*args, **kwargs)   # Passes the received arguments into the original function (add)
                              # Without *args/**kwargs here, add(11,2) would fail — no values passed
        
        print("Thanks for visiting")
    
    return mfx   # Returns wrapper function — WITHOUT this, @greet would make 'add' = None

# @greet automatically does: add = greet(add)
# 'add' now points to mfx, with original add() stored inside as 'fx'
@greet
def add(a, b):        # Expects exactly 2 positional arguments
    print(a + b)

add(11,2)

# Execution flow when add(11, 2) is called:
# 1. mfx(11, 2) runs         → args=(11,2), kwargs={}
# 2. prints "Welcome to Python"
# 3. fx(11, 2) runs          → original add(11, 2) → prints 13
# 4. prints "Thanks for visiting"
