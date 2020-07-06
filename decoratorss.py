def executor(func1):
    def executing_now():
        print("Executing func1()...")
        func1()
        print("func1() executed.")
    return executing_now()

@executor
def who_is_rohit():
    print("Rohit is a good boy.")

# who_is_rohit = executor(who_is_rohit)

who_is_rohit