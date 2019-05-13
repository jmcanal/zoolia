import sys
from sklearn.model_selection import train_test_split


def main():
    """
    Create emotion list from text file
    :return:
    """
    data_file = sys.argv[1]
    train_file = sys.argv[2]
    dev_file = sys.argv[3]
    devtest_file = sys.argv[4]
    test_file = sys.argv[5]

    data = [line.strip("\n") for line in open(data_file, "r")]

    x_train, x_test = train_test_split(data, test_size=0.3)
    x_train, x_dev = train_test_split(x_train, test_size=0.3)
    x_devtest, x_test = train_test_split(x_test, test_size=0.3)

    with open(train_file, 'w') as train:
        print("\n".join(x_train), file=train)

    with open(dev_file, 'w') as dev:
        print("\n".join(x_dev), file=dev)

    with open(devtest_file, 'w') as devtest:
        print("\n".join(x_devtest), file=devtest)

    with open(test_file, 'w') as test:
        print("\n".join(x_test), file=test)


if __name__ == "__main__":
    main()