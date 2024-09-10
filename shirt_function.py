def make_shirt(size="large", message="I Love Python"):
    """Gets t-shirt size"""
    print(f'You ordered a {size.title()} shirt that reads: {message}')
#make_shirt('medium', 'you suck!')
#make_shirt(size='XXX-Large', message="Eat my shorts!")
make_shirt()
make_shirt(size='medium')
make_shirt(size="XXX-Large", message="Python is FUN!")