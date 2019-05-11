import os

def toFahrenheit(tempC):
	print(os.getpid(), '::toF:: ', tempC)
	return ((float(9)/5)* tempC + 32)


def toCentigrade(tempF):
	print(os.getpid(), '::toC:: ', tempF)
	return ((float(5)/9)* (tempF-32))

if __name__ == '__main__':
    temps = (36, 37,38,39)
    F = map(toFahrenheit, temps)
    F1 = list(F)
    C = map(toCentigrade, F1)
    C1 = list(C)

    print('-----------------------')
    print(F1)
    print(C1)
