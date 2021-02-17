from pyHS100 import Discover


def main():
    """
    print ip addresses of smart plugs
    :return:
    """
    for dev in Discover.discover().values():
        print(dev)


if __name__ == '__main__':
    main()
