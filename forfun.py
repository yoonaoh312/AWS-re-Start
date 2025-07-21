"""
Your module description
"""
# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)
    
# def bacon():
#     ham = 101
#     eggs = 0
    
# spam()

# def spam():
#     print(eggs)
# eggs = 42
# spam()
# print(eggs)

# def spam():
#     eggs = 'spam local'
#     print(eggs)
# def bacon():
#     eggs = 'bacon local'
#     print(eggs)
#     spam()
#     print(eggs)
    
# eggs='global'
# bacon()
# print(eggs)

def spam():
    global eggs
    eggs = 'spam'
    # eggs = 'global'
    
spam()
print(eggs)