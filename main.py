# программа берет из файла строки- ответы экзаменуемых,правильные ответы, критерии оценивания
# составляет статитику по каждому заданию
# диограму распределения оценок
# список фамилия:оценка в алфавитном порядке
import matplotlib.pyplot as plt


def main():
    r_answers, criterio, results = opening()
    results = performance(results, criterio, r_answers)
    outer(results)


def opening():
    a = input('Введите название файла: ')
    with open(a) as f_in:
        line = f_in.readline()
        ans = line[line.find(':') + 2:-1]
        marks = []
        for i in range(3):
            line = f_in.readline()
            mark = int(line[line.find('оценка') + 7:line.find('ставится')])
            c = int(line[line.find('=') + 1:line.find('=') + 3])
            marks.append([mark, c])
        res = []
        for lines in f_in:
            line = lines.strip()
            res.append(line.split(': '))

        return ans, marks, res


def performance(res, marks, ans):
    stat = [0] * 10
    c5, c4, c3, c2 = 0, 0, 0, 0
    for ind in res:
        t1 = list(ind[1])
        t2 = list(ans)
        r = 0
        for o in range(10):
            if t1[o] == t2[o]:
                stat[o] += 1
                r += 1
        if r >= marks[0][1]:
            m = marks[0][0]
            c5 += 1
        elif r >= marks[1][1]:
            m = marks[1][0]
            c4 += 1
        elif r >= marks[2][1]:
            m = marks[2][0]
            c3 += 1
        else:
            m = 2
            c2 += 1
        ind.append(r)
        ind.append(m)
        res = sorted(res)
    s = len(res)
    bar(stat)
    pie(c2, c3, c4, c5, s)
    return res


def outer(res):
    with open('output.txt', 'w') as f_out:
        print('{:25s}{:8s}{:8s}'.format('Фамилия Имя', 'баллы', 'оценка'), file=f_out)
        print('_' * 40, file=f_out)
        for i in res:
            print('{:20s}{:8d}{:8d}'.format(i[0], i[2], i[3]), file=f_out)


def bar(stat):
    left_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    bar_width = 10
    plt.bar(left_edges, stat, bar_width, color=('r', 'g', 'b', 'm', 'k'))
    plt.title('Статистика выполнения по заданиям ')
    plt.xlabel('Задание')
    plt.ylabel('Кол-во выполнений')
    plt.xticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90], ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    plt.yticks([0, 5, 10, 15, 20], ['0', '5', '10', '15', '20'])
    plt.show()


def pie(c2, c3, c4, c5, summ):
    plt.title('Статистика распределения оценок')
    l = ['2 ' + '{:4.2%}'.format(c2 / summ), '3 ' + '{:4.2%}'.format(c3 / summ), '4 ' + '{:4.2%}'.format(c4 / summ),
         '5 ' + '{:4.2%}'.format(c5 / summ)]
    plt.pie([c2, c3, c4, c5], labels=l)
    plt.show()


if __name__ == '__main__':
    main()
