"""
Your module description
"""
userReply = input('do you need to shop a package? (Enter yes or no)')

if userReply == 'yes':
    print('we can help you ship that package')
    
else:
    print('please come back when you need to ship a package. Thank you')
    


userReply = input('would you like to buy stamps, buy an envelope, pr make a copy?(enter stamps, envelope, or copy)')
if userReply == 'stamps':
    print('we have many stamp designs to choose from.')
elif userReply == 'envelope':
    print('we have many envelope sizes to choose from. ')
elif userReply == 'copy':
    copies = input('how many copies would you like? (enter a number)')
    print('here are {} copies. '.format(copies))
else:
    print('Thnak you, please come again')