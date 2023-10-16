import os

problemTxt = 'problems.txt' #Файл с текстами задачи

tempF = 'LastRes.txt' #Место временного файла

outputF = 'AllreadyConverted/txt.txt' #Место итогого файла 

dir = 'ForConvert/'   #Дириктория с кодом !Может добавлю какойто метод вовода задач но для этого нужен pdf учебника :(


def calcIO(f, n):  #Сохранение результата программы (f)   n раз в временный файл tempF 
    print('Выполняю '+ f + ' Кол-во раз ' + str(n) )
    for i in range(n):
        os.system('python3 '+f+' >> ' + tempF)
    
    txt = ''.join(open(tempF).readlines())

    os.system('rm '+ tempF)
    return txt

edfile = open(outputF, 'w+')        #Открывает итоговый файл с "готовой" работой для редактирования 


for file in os.listdir(dir):
    
    x = open(dir+file).readlines()
    txt = ''

    txt += ('  Текст задачи \n \n')

    txt +=(''.join(open(problemTxt).readlines()).split('@$\n')[os.listdir(dir).index(file)] + '\n')

    txt +=('  Код программы \n \n')
    
    for i in x:
        txt+=(i)
    txt +=('\n')


    txt +=('  Результат работы программы \n  input/output  \n')

    #Пока не разобрался как брать инпут юзера в отдельный файл

    txt += (calcIO(dir + file, int(input('Сколько раз запускать прорамму ?  '))))
    
    
    edfile.write(txt)


print('Файл готов расположен в '+ outputF)


