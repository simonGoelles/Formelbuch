# this is a suprise tool that will help us later
from Crude_experimental import create, read, update, delete


if __name__ == '__main__':
    print("--- create() ---")
    id = create()
    print("--- read() ---")
    read(id)
    print("--- update() ---")
    update(id)
    print("--- delete() ---")
    delete(id)