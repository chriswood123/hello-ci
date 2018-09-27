import os

def say_hello(hello_string):
    return 'Hello {}'.format(hello_string)

if __name__ == '__main__':
    if 'PLUGIN_HELLO' in os.environ:
        hello_string = os.environ['PLUGIN_HELLO']
    else:
        hello_string = 'world'

    print(say_hello(hello_string))