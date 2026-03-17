# Decorator Factory Function
def greet(fx):          # 'fx' receives the function being decorated (hello)
    
    def mfx():          # Inner/Wrapper function that wraps the original function
        print("Welcome to Python Learning")
        fx()            # Calls the original decorated function (hello)
        print("Thanks for Learning")   
    
    return mfx          # Returns the wrapper — WITHOUT THIS, hello() would become None and fail

# '@greet' syntax automatically does: hello = greet(hello)
# So calling hello() now calls mfx(), which wraps the original hello()
@greet
def hello():
    print("Hello World. I am exploring Python OOPS Concept.")
    

hello()     # Executes mfx() → prints banner → original hello() → closing message



# **How the decorator flow works:**

# 1. @greet is syntactic sugar — Python runs `hello = greet(hello)` behind the scenes
# 2. `greet(hello)` stores the original `hello` as `fx`, then returns `mfx`
# 3. Now `hello` points to `mfx`, so calling `hello()` runs the wrapper
# 4. Inside `mfx`, `fx()` calls back the original `hello` logic





