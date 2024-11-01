define n = Character('Наруто', color="#FFFF00")
define g = Character("[name]")
define s = Character('Сакура', color = "#FF00FF")
define a = Character('Саске', color = "#191970")
define c = Character('Цунаде', color = "#228B22")

image konoha = "images/Konoha.jpg"
image academy_shinobi = "images/academy_shinobi.png"
image home_naruto = "images/Home_naruto.jpg"
image konohastreet = "images/konoha1.png"
image kabinethokage = "images/kabinet_xokage.jpg"
image zdaniehokage = "images/xokage_home.jpg"
image lessmerti = "images/lessmerti.jpg"
image restorant = "images/restorant.png"
image proshanie = "images/vorota.jpg"
image happynaruto = "images/narutohappy.png"
image narutosmile = "images/narutosmile.jpg"

label start:
    python:
        name = renpy.input("Как тебя зовут?")

        name = name.strip() or "Guy"

    scene konoha
    
    play music "naruto.mp3" fadeout 1 

    show naruto 
    with dissolve
    
    n "Добро пожаловать в Коноху!."
    n "Меня зовут Наруто! Я - будущий хокаге нашей деревни!"
    n "А как тебя зовут?"
    g "Меня зовут [name]. Я пришёл чтобы изучить вашу деревню."
    n "Давай прогуляемся по деревне и я познакомлю тебя со своими друзьями!"

    menu:
        "Да, конечно!.":
            jump choice1_yes
        "Нет, не хочу.":
            jump choice1_no

    label choice1_yes:
        $ menu_flag = True
        n "Давай, для начала прогуляемся в академию шиноби"
        jump choice1_done

    label choice1_no:
        $ menu_flag = False

        n "Ладно, давай тогда пойдём ко мне домой, поедим лапши и поговорим, наверное тогда ты наверняка захочешь прогуляться по нашей деревне."

        scene home_naruto
        n "Иди присаживайся, я разогрею лапшу и принесу."
        g "Хорошо"

        scene black
        "Вы поговрили с Наруто и он вас переубедил пойти гулять по деревне."

        scene konohastreet
        show naruto 
        with dissolve
        n "Давай для начала пойдём в академию шиноби."
        g "Хорошо ты меня переубедил. Пошли)"

        jump choice1_done

    label choice1_done:

        scene academy_shinobi
        show naruto:
            xalign 0.0 yalign 1.0
        with dissolve

        n "Вот академия шиноби. Здесь мы обучаемся новым приёмам и тактике ведения борьбы с врагом."
        n "Пора тебя познакомить с моими друзьями!"
        n "Как раз вот они и идут"

        show sakura:
            xalign 0.5 yalign 1.0
        with dissolve

        s "Привет, меня зовут Сакура. Буду рада знакомству!"

        show sasuke:
            xalign 1.0 yalign 1.0
        with dissolve

        a "Привет, меня зовут Саске."
        g "Приятно познакомиться, меня зовут [name]"
        n "Кстати, [name], не хочешь пойти прогуляться до здания хокаге и познакомиться с ней?"

        menu:
            "Да, конечно!.":
                jump choice2_yes

            "Нет, не хочу. Я стесняюсь!":
                jump choice2_no

        label choice2_yes:

            $ menu_flag = True

            n "Тогда не будем терять время. Пошли."
            
            scene kabinethokage
            show tsunade:
                xalign 0.0 yalign 1.0
            with dissolve

            show naruto:
                xalign 1.0 yalign 1.0
            with dissolve

            c "Что случилось, Наруто и кого ты привёл?"
            n "Тётушка Цунаде это [name]"
            n "Он пришёл из далёкой деревни к нам, чтобы изучить нашу деревню."
            g "Приятно познакомиться)"
            c "С какими целями ты сюда добрался?"
            g "Исключительно с хорошими!"
            c "Тогда хорошо тебе провести у нас в деревне."
            g "Спасибо!"
            n "Тогда мы пошли. Нам ещё надо побывать в некоторых местах в нашей деревне."
            c "До свидания"
            
            scene zdaniehokage
            show naruto

            n "В следующее место, в которое мы пойдём это лес смерти." 
            g "Жуткое название."
            n "Я слышу в твоём голосе неуверенность. Ты хочешь пойти туда или нет?"
            jump choice2_done

        label choice2_no:

            $ menu_flag = False

            n "Хорошо. Тогда пошли в лес смерти."
            g "Жуткое название. Как и место наверное."
            n "Я слышу в твоём голосе неуверенность. Ты хочешь пойти туда или нет?"
            jump choice2_done

        label choice2_done:

        menu:
            "Да, пошли!":
                jump choice3_yes

            "Нет, не хочу. Только услышав название, страшно стало!":
                jump choice3_no  

        label choice3_yes:

            $ menu_flag = True

            n "Хорош. Тогда пошли."

            scene lessmerti 

            n "Мы добрались. За забор нельзя."
            g "Там настолько опасно?"
            n "Да. Там обитают ниндзя и существа, которые могут в каждую секунду тебя убить."
            g "Жутко"
            g "Я думаю на пора идти. Я проголодался."
            n "Я тоже, давай сходим в раменную."
            g "Давай!"

            jump choice3_done

        label choice3_no:

            $ menu_flag = False

            n "Хорошо. Тогда пошли в раменную. Ты точно проголодался за всё это время."
            g "Это точно!"

            jump choice3_done
        
        label choice3_done:

            scene restorant

            n "Ну вот мы дошли до раменной. Здесь рамен самый вкусный."
            n "Какую лапшу будешь [name]?"
            g "Такую же какую и ты ешь."

            scene proshanie

            show happynaruto
            n "Приятно было с тобой познакомиться! Счастливого пути!"
            
            scene narutosmile
            "Конец игры. Пожалуйста не судите строго я новичок! Если понравилась игра то ставьте лайк или даже можно 5 (прошу)"


    return
