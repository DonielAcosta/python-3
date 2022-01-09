def run():
    for cont in range(1000):
        if cont % 2 != 0:
            continue
        print(cont)


if __name__ == '__main__':
    run()