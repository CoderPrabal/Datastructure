import dis

def example(x):
    for i in range(x):
        print(2*i)

print(dis.dis(example))
#https://www.pypy.org/
#normal_language->compiler->machine_code->execute
#python ->compiler->bytecode->interpret->execute