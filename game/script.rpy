# chrs define:
define A = Character('Арсений', color="#518b59")
define O = Character('Объявление', color= "#ffffff")
define S = Character('Света', color= "#f77b5c")
define M = Character('Максим', color= "#da9f42")
define L = Character('Лена', color= "#b6037a")
define Art = Character('Артём', color= "#f1e38f")
define W = Character('???', color= "#ffffff")

# спрайты персонажей
image senya = "Senya1.png"
image Lena = "Lena1.png"
image Sveta = "Sveta1.png"
image Max = "Max1.png"
image Art = "Artem1.png"

#фоны
image GUK = "GUK.png"
image auditory = "CLASS.png"
image Club = "PC.png"
image univer = "univer.png"
image GT = "GoodTime.png"
image ST = "Sometime.png"
image ND = "NextDay.png"

#различные баллы:


#звуки

label start:

    show text "samurai team presents"
    with dissolve
    $ renpy.pause(2)
    hide text
    show text "The Choice"
    with dissolve
    $ renpy.pause(2)
    hide text
    with dissolve
        
    $ TestScore = 0
    $ LenaFriendship = 0
    $ SvetaFriendship = 0
    $ MaxFriendship = 0
    $ ArtFriendship = 0 
    
    play music "music/soundStr.mp3" fadein(0.5)
    
    scene univer
    with dissolve

    A "Как я долго ждал этого!"
    A "Столько времени и сил были потрачены не зря!"
    A "Школа, ЕГЭ - всё позади. Теперь я студент"

    O "Внимание! Студенты, поступившие на направление программирования, просим пройти в главный корпус на церемонию!"

    A "Нужно идти в главный корпус"

    stop music fadeout(0.5)

    scene black
    with dissolve

    scene ND
    with dissolve
    $ renpy.pause(2)
    

    #экран с надписью "прошла пышная церемония поступления"

    #экран с надписью ДЕНЬ 1

label Day1:

    #сцена в лекционной аудитории Лена появляется по центру
    play music "music/soundUni.mp3" fadein(0.5)
    scene auditory
    with dissolve

    show Lena
    with dissolve
    W "Привет, я тебя еще на церемонии видела, ты ведь с очень высокими баллами поступил, верно?"
    A "Приветствую! Да, ты права, баллы у меня довольно хорошие, ради них пришлось много трудиться."
    A "Как тебя зовут?"
    W "Точно! Забыла представиться!"
    L "Меня Леной звать, а тебя?"
    A "Арсений"

    hide Lena
    show Max
    with dissolve
    W "Я тут услышал нотки знакомства, ятоже хочу!"

    A "О, я тебя помню, ты же подающий надежды легкоатлет, Максим, кажется, тебя зовут"

    M "Я вообще-то хотел сам представиться, но верно, я Макс, приятно познакомиться"
    M "Простите, но разговор  я ваш услышал, так что и имена ваши я запомнил"

    hide Max
    show Lena
    with dissolve
    L "Ничего страного, так даже интереснее!"
    L "Как вам первый день?"

    A "Я думал, что будет немного проще, но мне нравится"

    hide Lena
    show Max
    with dissolve
    M "Скучно было, я планирую вместо следующей пары пойти в ПК-клуб"
    M "Кто со мной?"

    # выбор пойти в игровуху(ранняя встреча с Артемом) или на следующую пару(+ 0.5 баллов для экзамена)
    menu:
        "Пойти в игровой клуб":
            A "Я Максом пойду, пока Лена!"
            hide Max
            show Lena
            with dissolve
            L "Ну ладно, тогда пока"
            hide Lena
            with dissolve
            $ MaxFriendship += 1
            scene black
            with dissolve
            stop music fadeout(0.5)
            $ renpy.pause(1)
            jump PCclub
        "Остаться на пару":
            A "Я останусь"

            M "Ну твое дело"

            $ LenaFriendship += 1
            $ TestScore += 1
    
    # оставшая часть главы даст 1 балл дружбы с Леной(а поможет это или нет, я хз)))
    hide Max
    show Lena
    with dissolve
    L "Я считаю, что ты поступил правильно, ведь следующая пара важна"

    A "Наверное..."
    A "Пошли пока в аудиторию, займем места получше"

    L "Да, пойдем, как раз самое время"

    hide Lena
    with dissolve

    stop music fadeout(0.5)
    scene black
    with dissolve
    $ renpy.pause(1)
    

    jump Day2

label PCclub:

    #сцена в игровухе
    play music "music/soundUni.mp3" fadein(2)

    scene Club
    with dissolve

    show Max
    with dissolve

    M "Мне кажется, ты поступил правильно, ведь следующая пара нереально скучная"
    A "Наверное..."
    A "Вон там есть свободные места, пошли к ним"
    M "Погнали!"

    #экран НЕКОТОРОЕ ВРЕМЯ СПУСТЯ, к ним подошел Артем
    hide Max
    show Art
    with dissolve
    W "Эмм... Можно к вам присоединиться?"
    menu:
        "Да, конечно!":
            W "Спасибо" 
            A "Как тебя звать?"
            Art "Артем"
            A "Отлично, Артем, подключайся к нам, раунд скоро начнется"
            $ ArtFriendship += 1
        "Не думаю..":
            W "Ну ладно тогда..."
    stop music fadeout(1)
    scene black
    with dissolve
    scene GT
    with dissolve
    $ renpy.pause(1)
    scene black
    with dissolve
    
    #экран МЫ ОТЛИЧНО ПРОВЕЛИ ВРЕМЯ
    
label Day2:
    show text "На следующий день"
    with dissolve
    $ renpy.pause(1)
    hide text
    with dissolve

    play music "music/soundUni.mp3"
    scene auditory
    with dissolve

    show Art
    with dissolve

    if ArtFriendship == 1:
        Art "Могу я сесть рядом на этой паре?"
        A "Да, конечно"
    else:
        W "Могу я сесть рядом на этой паре?"
        A "Да, конечно"
        A "Как мне к тебе обращаться?"
        Art "Просто Артем"
    Art "Тебе не трудно?"
    Art "Я слышал, что на этом направлении тяжело тем, кто не занимался самостоятельно"
    A "Ты прав, у меня действительно проблемы с программированием"
    Art "Я могу помочь тебе. Хочешь?"
    menu:
        "Согласиться":
            Art "Отлично, после этой пары пошли в коворкинг"
            A "Погнали!"
            hide Art
            with dissolve
            $ TestScore += 1
            $ ArtFriendship += 1
            stop music fadeout(0.5)
            scene black
            with dissolve
            show text "После совместных занятий с Артемом я наткнулся на девушку с необычно большим рюкзаком"
            with dissolve
            $ renpy.pause(2)
            hide text
            with dissolve
            $ renpy.pause(0.5)
            

        
        "Отказаться":
            A "Не, я сам хочу разобраться"
            Art "Ну как знаешь.."
            hide Art
            with dissolve
            stop music fadeout(0.5)
            scene black
            with dissolve
            show text "После моего отказа я вышел из аудитории и наткнулся на девушку с необычно большим рюкзаком"
            with dissolve
            $ renpy.pause(2)
            hide text
            with dissolve
            $ renpy.pause(0.5)
    
    #после работы в коворке/пары мы встечаем свету, которая готовила украшения к мероприятию

    play music "music/soundUni.mp3"
    scene GUK 
    with dissolve

    A "Привет! тебе помочь?"
    show Sveta
    with dissolve

    W "Здравствуй, да, спасибо, помощь не помешала бы"
    W "Как тебя зовут?"
    A "Арсений, можно просто сеня. А тебя?" 
    S "Меня света зовут, я староста группы по программированию"
    A "Значит мы с одного направления!"
    A "Это хорошо"
    S "Слушай, мне нужно некоторые декорации перенести в аудиторию, поможешь?"

    S "спасибо большое!"
    A "мне не трудно"
    hide Sveta
    with dissolve
    $ SvetaFriendship += 1
    stop music fadeout(0.5)
    scene black
    with dissolve
    show text "Я помог ей отнести декор в аудиторию, в которой они должны быть"
    with dissolve
    $ renpy.pause(2)
    hide text
    show text "После этого я пошел домой"
    with dissolve
    $ renpy.pause(2)
    hide text
    with dissolve            
    $ renpy.pause(0.5)
            
    
label Day5:

    show text "Прошло некоторое количество дней"
    with dissolve
    $ renpy.pause(2)
    hide text
    with dissolve    

    play music "music/soundUni.mp3"
    scene GUK
    with dissolve

    show Max
    with dissolve
    M "ребят, сегодня концерт известной группы будет"

    hide Max
    show Art
    with dissolve
    Art "а что за группа?"

    hide Art
    show Max
    with dissolve
    M "сегодня мировой тур группы 'TFK' дошел до нашего города"

    hide Max
    show Art
    with dissolve
    Art "не думаю, что пойду, мне надо домашку сделать по матанализу"

    hide Art
    show Sveta
    with dissolve
    S "на носу день рождения университета, я буду там как один из ведущих"
    S "так что прости, не выйдет"
    
    hide Sveta
    show Lena
    with dissolve
    L "я сегодня хотела сесть за подготовку к приближающимся экзаменам"

    hide Lena
    show Max
    with dissolve
    M "а ты как, Сеня?"

    menu:
        "пойти на концерт":
            A "ладно, пошли на концерт"

            hide Max
            show Sveta
            with dissolve
            S "как же так, я видела твой табель"
            S "твои баллы прямо кричат, что тебе следует заняться подготовкой"

            hide Sveta
            show Max
            with dissolve
            M "ой, да ладно вам, будто что-то сильно из-за одного концерта поменяется"

            A "я тоже так думаю"

            hide Max
            show Lena
            with dissolve
            L "ну смотрите, потом будет тяжето наверстать"

            $ MaxFriendship +=1
            
            hide Lena
            with dissolve
            stop music fadeout(0.5)
            scene black
            with dissolve
        "присоединиться к подготовке":
            A "я присоединюсь к Лене"
            A "мне надо бы начинать готовиться, а то баллы в табеле не самые хорошие"

            M "ой да ладно тебе!"
            M "ну пропустишь одну подготовку, много ли потеряешь?"

            hide Max
            show Lena
            with dissolve
            L "Арсений прав, надо начинать заранее"
            
            $ LenaFriendship += 1

            hide Lena
            with dissolve
            stop music fadeout(0.5)
            scene black
            with dissolve
    
    if ArtFriendship >= 0 and LenaFriendship >= 0 and SvetaFriendship >= 0 and MaxFriendship >= 0:
        jump AllTogether
    else:
        jump duo

label duo:

    show text "Прошло еще некоторое количество дней"
    with dissolve
    $ renpy.pause(2)
    hide text
    with dissolve  

    #общался не со всеми персами
    play music "music/soundUni.mp3" fadein(0.5)
    scene GUK
    with dissolve

    show Lena
    with dissolve

    L "ребят, до сессии осталось всего ничего"
    L "предлагаю начать готовиться"

    hide Lena
    show Sveta
    with dissolve
    S "полностью поддерживаю"

    hide Sveta
    show Art
    with dissolve
    Art "я могу с программированием и математикой помочь"

    hide Art
    show Max
    with dissolve
    M "а мне и самому нужна помощь, я с Сеней пойду"

    hide Max
    show Sveta
    with dissolve
    S "ну что, с кем пойдешь готовиться?"

    menu:
        "готовиться со Светой":
            A "думаю можно с тобой, света"
            
            S "спасибо большое, идем в коворгинг"
            
            hide Sveta 
            show Art
            with dissolve
            Art "пока ребят!"

            hide Art
            show Lena
            with dissolve
            L "увидимся на экзамене!"

            hide Lena
            show Max
            with dissolve
            M "удачи вам, мы пошли на подготовку"
            hide Max
            with dissolve
            $ TestScore += 1

        "готовиться с Леной":
            A "Лена много чего знает и хорошо объясняет"
            A "можем с ней пойти"

            hide Sveta
            show Max
            with dissolve
            M "хорошо, пошли с нами, Лена"

            hide Max
            show Lena
            with dissolve
            L "да, конечно"
            
            hide Lena
            show Sveta
            with dissolve
            S "до встречи на экзамене!"

            hide Sveta
            show Art
            with dissolve
            Art "хорошо подготовиться вам!"

            A "спасибо большое!"
            hide Art
            with dissolve

            $ TestScore += 1

        "готовиться с Артемом":
            A "Артем хорошо разбирается в программировании и математике"
            A "это ключевые предметы на экзамене"
            
            hide Sveta
            show Max
            with dissolve
            M "ну тогда пошли с нами, Арт!"

            hide Max
            show Lena
            with dissolve
            L "математика и программирование действительно ключевые предметы"

            hide Lena
            show Sveta
            with dissolve
            S "хорошо подготовиться к экзаменам!"

            hide Sveta
            show Art
            with dissolve
            Art "спасибо большое, вон там есть свободный коворкинг"

            hide Art
            with dissolve
            $ TestScore += 1
    if TestScore >= 2:
        jump GoodEnd
    else:
        jump BadEnd

label AllTogether:
    
    show text "Прошло некоторое количество дней"
    with dissolve
    $ renpy.pause(2)
    hide text
    with dissolve  
    
    #провел время со всеми и можно подготовиться вместе(больше очков)
    scene GUK
    with dissolve

    show Lena
    with dissolve
    L "ребят, до сессии осталось всего ничего"
    L "предлагаю начать готовиться"

    hide Lena
    show Sveta
    with dissolve
    S "полностью поддерживаю"

    hide Sveta
    show Art
    with dissolve
    Art "я могу с программированием и математикой помочь"

    A "может все вместе и пойдем готовиться?"

    hide Art
    show Max
    with dissolve
    M "отличная идея, как раз я видел небольшую свободную аудиторию"

    hide Max
    show Lena
    with dissolve
    L "идем тогда скорее!"
    hide Lena
    with dissolve

    $ TestScore += 2
    
    if TestScore >= 2:
        jump GoodEnd
    else:
        jump BadEnd

label BadEnd:
    
    scene black
    with dissolve
    $ renpy.pause(1)
    show text "Закончился последний экзамен, после которого мы все встретились"
    with dissolve
    $ renpy.pause(2)
    hide text
    with dissolve
    
    play music "music/soundStr.mp3" fadein(1)

    scene univer
    with dissolve

    show Lena
    with dissolve
    L "фух, вот и последний экзамен позади"

    hide Lena
    show Sveta
    with dissolve
    S "матанализ мне показался легким"

    hide Sveta
    show Max
    with dissolve
    M "я по программированию еле-еле порог прошел, но сдал"
    M "Артем вообще самый первый из аудитории вышел"

    hide Max
    show Art
    with dissolve
    Art "там ведь делов на 20 минут"

    hide Art
    show Sveta
    with dissolve
    S "а ты как, Сеня? Сдал?"

    A "к сожалению..."
    A "я потратил все попытки пересдать, но так и не получилось"

    hide Sveta
    show Max
    with dissolve
    M "как же так случилось, тебя ведь отчислят быстро"

    hide Max
    show Lena
    with dissolve
    L "ничего страшного, восстановишься в следующем году"

    O "Внимание! Студенты, не сдавшие экзамены, пожалуйста пройдите в главный учебный корпус!"

    A "ну вот мне и пора, всем пока"

    hide Lena
    show Art
    with dissolve
    Art "Удачи тебе!"

    hide Art
    show Max
    with dissolve
    M "не падай духом, в следующий раз все получится!"

    hide Max
    show Lena
    with dissolve
    L "до встречи!"

    hide Lena
    show Sveta
    with dissolve
    S "если восстановишься в следующем году, будет замечательно"

    A "Спасибо вам всем, я пошел"

    hide Sveta
    with dissolve

    stop music fadeout(0.5)

    scene black
    with dissolve

    show text "Арсений не смог сдать последние экзамены, из-за чего был исключен из института"
    with dissolve
    $ renpy.pause(2)     
    hide text
    show text "Наступила весна, а значит настало время весеннего призыва..."
    with dissolve
    $ renpy.pause(2)
    hide text with dissolve
    show text "BAD ENDING"
    with dissolve
    $ renpy.pause(2)
return

label GoodEnd:
    scene black
    with dissolve
    $ renpy.pause(1)
    
    show text "Закончился последний экзамен, после которого мы все встретились"
    with dissolve
    $ renpy.pause(2)
    hide text
    with dissolve

    play music "music/soundStr.mp3"
    show Lena
    with dissolve
    L "фух, вот и последний экзамен позади"

    hide Lena
    show Sveta
    with dissolve
    S "матанализ мне показался легким"

    hide Sveta
    show Max
    with dissolve
    M "я по программированию еле-еле порог прошел, но сдал"
    M "Артем вообще самый первый из аудитории вышел"

    hide Max
    show Art
    with dissolve
    Art "там ведь делов на 20 минут"

    hide Art
    show Sveta
    with dissolve
    S "а ты как, Сеня? Сдал?"

    A "к счастью, да, сдал, и даже с запасом"

    hide Sveta
    show Lena
    with dissolve
    L "вот видишь, не зря готовился"

    hide Lena
    show Art
    with dissolve
    Art "а ведь раньше и простейшие задачи тебе с трудом давались"

    hide Art
    show Sveta
    with dissolve
    S "а сейчас даже Макса обогнал"

    hide Sveta
    show Max
    with dissolve
    M "мне просто вариант невезучий попался!"

    O "Внимание! Студенты, не сдавшие экзамены, пожалуйста пройдите в главный учебный корпус!"

    A "как хорошо, что никого из нас не касается!"

    hide Max
    with dissolve

    stop music fadeout(0.5)

    scene black
    with dissolve
    
    if ArtFriendship >= 0 and LenaFriendship >= 0 and SvetaFriendship >= 0 and MaxFriendship >= 0:
        show text "После сдачи экзаменов, Арсений получил возможно стать бэк-энд разработчиком в крупной IT компании"
        with dissolve
        $ renpy.pause(2)     
        hide text
        show text "Помимо этого он обрел хороших друзей на всю жизнь"
        with dissolve
        $ renpy.pause(2)
        hide text with dissolve        
        with dissolve
        show text "GOOD ENDING"
        with dissolve
        $ renpy.pause(2)
        hide text
        with dissolve
    else:
        show text "После сдачи экзаменов, Арсений получил возможно стать бэк-энд разработчиком в крупной IT компании"
        with dissolve
        $ renpy.pause(2)     
        hide text
        show text "Но он не смог обрести хороших друзей на всю оставшуюся жизнь"
        with dissolve
        $ renpy.pause(2)
        hide text with dissolve
        show text "NEUTRAL ENDING"
        with dissolve
        $ renpy.pause(2)
        hide text
        with dissolve
    