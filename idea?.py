import os

problemTxt = '/problems.txt' #Файл с текстами задачи

tempF = '/IdeaGotBig/LastRes.txt' #Место временного файла

outputF = '/AllreadyConverted/txt.txt' #Место итогого файла 

dir = '/ForConvert/'   #Дириктория с кодом !Может добавлю какойто метод вовода задач но для этого нужен pdf учебника :(


def calcIO(f, n):  #Сохранение результата программы (f)   n раз в временный файл tempF 
    
    for i in range(n):
        os.system('python3 '+f+' >> ' + tempF)
    
    txt = ''.join(open(tempF).readlines())

    os.system('rm '+ tempF)
    return txt

edfile = open(outputF, 'w+')        #Открывает итоговый файл с "готовой" работой для редактирования 

#for file in os.listdir(dir):
    #x = open(dir+file).readlines()
    
    #dfile.write('  Текст задачи \n')
    
    #edfile.write(''.join(open(problemTxt).readlines()).split('@$\n')[os.listdir(dir).index(file)] + '\n')
    
    #edfile.write('  Код программы \n')
    
    #for i in x:
        #edfile.write(i)

    #edfile.write('\n')


    #edfile.write('  Результат работы программы \n')

    #Пока не разобрался как брать инпут юзера в отдельный файл

    #edfile.write(calcIO(dir + file, int(input('Сколько раз запускать прорамму ?  '))))



for file in os.listdir(dir):
    
    x = open(dir+file).readlines()
    txt = ''

    txt += ('  Текст задачи \n')

    txt +=(''.join(open(problemTxt).readlines()).split('@$\n')[os.listdir(dir).index(file)] + '\n')

    txt +=('  Код программы \n')
    
    for i in x:
        txt+=(i)
    txt +=('\n')


    txt +=('  Результат работы программы \n')

    #Пока не разобрался как брать инпут юзера в отдельный файл

    txt += (calcIO(dir + file, int(input('Сколько раз запускать прорамму ?  '))))
    
    
    edfile.write(txt)





