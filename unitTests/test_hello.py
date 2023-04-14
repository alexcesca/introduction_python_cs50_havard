from hello_func import hello


def teste_default():
    assert hello() == "hello, world"


def teste_arguments():
    assert hello("alex") == "hello, alex"
