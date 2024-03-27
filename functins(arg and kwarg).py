def example_function(*args, **kwargs):
    print("Positional arguments (*args):")
    for arg in args:
        print(arg)
        
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

example_function(1, 2, 3, 4, name="Alice", age=30)
