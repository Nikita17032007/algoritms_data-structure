#Bubble algoritm - алгоритм, когда элементы сравниваются попарно и он повторяется, пока список не будет отсортирован

a = [5,7,4,3,8,2]   #неотсортированный список
n = 6   #количество символов

#как раобает этот код: он попарно сравнивает все элементы списка, переставляя их по возрастанию

for run in range(n-1):   #тут указывается каол-во повторений кода
    for i in range(n-1-run):    #тк мы сравниваем элементы попарно, а у последнего элемента пары нет, то мы указываем range n-1 (5). -run нужен для оптимизации кода (чтоб каждый раз не сравнивать например 7 и 8)
        if a[i] > a[i+1]:
            a[1], a[i+1] = a[i+1], a[1]

#упражнение
x = [1,4,2,3,4]
y = 5

for run in range (y-1):
    for i in range (y-1-run):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]

    print(x)