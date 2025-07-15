# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define a = Character('[povname]', color="#000000")
define b = Character('Bamoussa', color="#000000")
define b2 = Character('Binta', color="#000000")
define i = Character("???", color="#000000")
define m = Character("Maman", color="#000000")
define l = Character("Lunamystique", color="#000000")
#characters-sprites
#Bamoussa
image bamoussa_default = "bamoussa_default.png"
image bamoussa_anxious = "bamoussa_anxious.png"


# Binta
image Binta_afraid = "Binta_afraid.png"
image Binta_angry = "Binta_angry.png"
image Binta_annoyed = "Binta_annoyed.png"
image Binta_anxious = "Binta_anxious.png"
image Binta_default_happy = "Binta_default_happy.png"
image Binta_explaining = "Binta_explaining.png"
image Binta_grossed_out = "Binta_grossed_out.png"
image Binta_sad = "Binta_sad.png"
image Binta_sad_notspeaking = "Binta_sad_notspeaking.png"
image Binta_thinking = "Binta_thinking.png"
image Binta_very_happy = "Binta_very_happy.png"

#backgrounds
#school
image bg_classroom_day = "classroom_day.jpg"
image bg_classroom_evening = "classroom_evening.jpg"
image bg_classroom_night_lightOff = "classroom_night_lightOff.jpg"
image bg_classroom_night_lightOn = "classroom_night_lightOn.jpg"
image bg_frontGate_day = "frontGate_day.jpg"
image bg_frontGate_evening = "frontGate_evening.jpg"
image bg_frontGate_night = "frontGate_night.jpg"
image bg_courtyard_day = "courtyard_day.jpg"

#roadToSchool
image bg_roadToSchool_day = "roadToSchool_day.jpg"
image bg_roadToSchool_evening = "roadToSchool_evening.jpg"
image bg_roadToSchool_night = "roadToSchool_night.jpg"

#backstreets
image bg_backstreets_day = "backstreets_day.jpg"
image bg_backstreets_evening = "backstreets_evening.jpg"
image bg_backstreets_night = "backstreets_night.jpg"

#bedroom
image bg_bedroom_day = "bedroom_day.jpg"
image bg_bedroom_night_lightOff = "bedroom_night_lightOff.jpg"
image bg_bedroom_night_lightOn = "bedroom_night_lightOn.jpg"
image bg_bedroom_afterSchool = "bedroom_afterSchool.jpg"


#living room
image bg_livingRoom_day = "livingRoom_day.jpg"
image bg_livingRoom_evening = "livingRoom_evening.jpg"
image bg_livingRoom_night_lightOff = "livingRoom_night_lightOff.jpg"
image bg_livingRoom_night_lightOn = "livingRoom_night_lightOn.jpg"

#ruins
image bg_ruins_start = "ruins_start.jpg"
image bg_ruins_corridor = "ruins_corridor.jpg"
image bg_ruins_end = "ruins_end.jpg"
image bg_ruins_outside = "ruins_outside.jpg"


#park
image bg_park_day = "park_day.jpg"
image bg_park_evening = "park_evening.jpg"
image bg_park_night = "park_night.jpg"
#ending
image bg_black_screen = "black.jpg"

#screenshots
image bg_email_1 = "email.png"

# effects
#screenshake
transform shake_bg:
    linear 0.05 xoffset -10  # Déplace légèrement à gauche
    linear 0.05 xoffset 10   # Déplace légèrement à droite
    linear 0.05 xoffset -5   # Retourne légèrement à gauche
    linear 0.05 xoffset 5    # Retourne légèrement à droite
    linear 0.05 xoffset 0    # Revient à la position initiale




#resize character
transform size_normal:
    ysize 600
    fit "contain"


#character positions 
transform left: 
    xalign 0.0
    yalign 0.3
    zoom (0.5)

transform right: 
    xalign 1.0
    yalign 0.3
    zoom (0.5)

transform center: 
    zoom (0.5)
    yalign 0.3
    xalign 0.5


#variables
default hasCheckedNotification = False
default hasTalkedToBullies = False
default bad_choices = 0
default good_choices = 0



# Le jeu commence ici
label start:
    stop music
    "Cette oeuvre est un travail de fiction. Toute ressemblance à des personnes ou des événements est totalement fortuite."
    "Si vous êtes témoin de toute forme d'harcèlement ou de cyberharcèlement, ne laissez pas faire ces actions et contactez les autorités compétentes."
    $ povname = renpy.input("Quel est ton nom ?", length=32)
    $ jeu = renpy.input("Quel est ton jeu du moment ?", length=32)
    centered "{size=+75}{cps=8}{color=#ffffff}Chapitre 1{/color}{/cps}{/size}{p=5.0}{nw}"
    scene bg_bedroom_day with fade
    "Hmmm... Sacrée nuit..."
    "Je pense pas que j'aurais dû jouer aussi tard mais bon... C'est bientôt les vacances et j'ai de bonnes notes, ça devrait le faire non ?"
    "On commence la journée simplement, afin de se réveiller. Brossage de dents, on s'habille, on déjeune et on y va !"
    "Ma mère est déjà absente à cette heure-ci, donc il est temps de mettre un peu de musique..."
    play music "music/Morning.mp3" fadeout 1.0 loop
    scene bg_livingRoom_day with dissolve

    "Au matin je mange simplement : ça sera banane et une compote."
    "Je préfère commencer la journée légèrement, il ne faudrait pas avoir l'estomac trop rempli et m'endormir en plein cours..."
    "Pendant que je déguste tranquillement mon petit déjeuner, une notification sur mon téléphone vient interrompre le calme matinal."
    a "Ah ouais dès le matin ?"
    "Le problème avec les téléphones c'est qu'on est tout le temps connecté, j'ai besoin de souffler de temps en temps aussi non ?"
    "Mais bon, c'est vrai que j'aurais pu me mettre en mode avion..."

    menu: 

            a "Hmm... Alors c'est quoi cette notification ?"
             
            "Regarder la notification.":
                $ hasCheckedNotification = True
                jump notification

            
            "Eteindre mon téléphone.":
                $ hasCheckedNotification = False
                jump eteindre

label notification : 
    "Et puis bon pourquoi ne pas regarder ? J'ai encore un peu de temps non ?"
    "Je prends mon téléphone et clique sur la notification."
    "\"Yo c'était trop cool hier la game, t'es chaud de rejoindre le groupe Echord que j'ai créé ?\""
    "C'était Bamoussa, un ami avec qui j'ai joué hier."
    a "Hello mon gars... Avec plaisir... Envoie le lien. Hop et envoyé !"
    "C'est vrai que pour jouer à des jeux vidéo à plusieurs, Echord est bien meilleur que de passer par le chat vocal du jeu."
    "J'ai attendu quelques instants mais c'est bon, j'ai bien reçu le lien d'invitation, je clique dessus et c'est bon je suis dedans !"
    "Par contre j'ai pas fait gaffe à l'heure, si je pars pas maintenant je risque d'être bien en retard !"
    "Je prends mon sac, mes écouteurs et je n'oublie certainement pas un autre fruit pour le goûter, et c'est parti !"

    jump roadToSchool

label eteindre : 
    "Oh non pas dès le matin tout de même... Il faut commencer la journée petit à petit, je regarderai plus tard !"
    "Vu que j'ai un peu d'avance je prends mon temps, un matin tranquille c'est tout ce que j'aime."
    "Je prends mon sac, mes écouteurs et je n'oublie certainement pas un autre fruit pour le goûter, et c'est parti !"

    jump roadToSchool
    
label roadToSchool : 
    scene bg_roadToSchool_day with fade
    "Sur le chemin je croise des amis avec qui j'aime discuter de nos passions communes."
    "Récemment on joue à un nouveau jeu : [jeu] !"
    "On finit par arriver non loin du collège après une discussion des plus passionnantes..."

    scene bg_frontGate_day with dissolve
    "Arrivé devant le collège, mes camarades s'empressent d'entrer."
    "De mon côté, j'arrive très sereinement au portail, je suis du genre à éviter de me presser pour rien."
    "La vie est vraiment belle quand on a de bonnes notes n'empêche..."
    "Aujourd'hui on commence avec un cours d'anglais, c'est probablement ma matière préférée vu que je suis le meilleur de la classe."
    "Je me rends, le pas léger, en classe."

    scene bg_classroom_day with dissolve
    "Une fois assis sur ma chaise, une voix familière vient m'interpeller."
    i "Yo [povname] !"

    show bamoussa_default at center
    b "Alors t'as pu voir mon message ?"
    "C'était Bamoussa qui m'interpellait. Comme moi, il est du genre à être très serein. C'est vraiment apaisant d'avoir un ami comme lui."

    if hasCheckedNotification == True:
        a "Bien sûr ! J'ai rejoint le groupe, trop hâte de pouvoir jouer en appel ça sera beaucoup plus simple."
        b "Oh ouais carrément, les appels sur Whatsapp c'est pas très évident..."
        a "Y a qui sur le groupe d'ailleurs ?"
        b "Oh tu sais quelques amis à moi et des personnes que j'ai rencontré sur [jeu], ils sont grave sympas donc t'as pas de soucis à te faire !"
    else:
        "Je n'ai même pas regardé cette notification. Oups !"
        a "Euh... J'avoue je n'ai même pas regardé..."
        b "Oh fais un petit effort ! Tu risques de faire pleurer ton meilleur ami là !"
        a "Ahah oui désolé... Alors c'était à propos de quoi ?"
        b "Je t'ai ajouté sur un groupe Echord pour qu'on puisse jouer à [jeu] avec d'autres personnes !  "
        a "Y a qui sur le groupe ?"
        b "Oh tu sais quelques amis à moi et des personnes que j'ai rencontré sur [jeu], ils sont grave sympas donc t'as pas de soucis à te faire !"
    
    "De nouveaux coéquipiers dans l'équipe... Ca pourrait être sympa franchement !"
    a "Bah écoute ce soir je suis partant pour y jouer ! Tu seras là ?"
    b "Bien sûr ! Je me connecterai vers 20h, sois là !"
    i "A vos places s'il vous plait le cours commence !"
    "Le professeur vient interrompt notre conversation."
    "Je fais un signe de confirmation de la tête à Bamoussa tandis qu'il retourne à son siège."
    "Ce soir c'est décidé, ça sera une soirée gaming !"

    scene bg_roadToSchool_evening with fade
    play music "music/Evening.mp3" fadeout 1.0 loop
    "La cloche fait enfin retentir la fin de la journée, il est temps de rentrer à la maison et de faire ses devoirs."

    scene bg_livingRoom_evening with dissolve
    a "Je suis rentré !"
    "Enfin arrivé chez moi, je me déchausse pour enfiler mes pantoufles, c'est le signal qu'une belle soirée peut commencer."
    m "La journée s'est bien passé ?"
    "Ma mère, depuis la cuisine, prépare un copieux repas qui charme déjà mes sens."
    "Je reste un peu avec elle pour raconter nos journées, et ensuite c'est devoirs puis douche !"

    scene bg_bedroom_afterSchool with dissolve
    play music "music/Study And Relax.mp3" fadeout 1.0 loop
    "Une fois enfin posé, j'allume enfin mon ordinateur."
    "Avant de commencer à jouer, je regarde mes mails. On ne sait jamais, on peut toujours recevoir des mails intéressants !"
    "D'ailleurs, je pouvais en voir un très intéressant..."
    a "Un mail de Echord..."
    "Je commence à lire le mail."
    scene bg_email_1 with dissolve:
        zoom 1.4
    "De : support-Echord@securehelp.com"
    "Objet : ⚠️ Action requise : Vérification de votre compte Echord"
    "Nous avons détectéé une activité inhabituel sur votre kompte Echord et nous soupçonnons une connection non autorisér depuis Sihanoukville, Cambodge."
    "📌 Détails de la connexion suspecte :"
    "Adresse IP : 192.168.XXX.XXX, Localisation : Sihanoukville, Cambodge, Heure : 19h45."
    "Par mesure de sécurité, votre compte a été temporairement restreint. Veuillez confirmer votre identité dans les 24 heures pour évité une suspension définitif."
    "👉 Cliquez ici pour sécuriser votre compte : Echord-secure.verification.com/login"
    "Si vous ne vérifiez pas votre compte dans le délai imparti, nous serons contraints de désactiver définitivement votre compte."
    "Merci pour votre coop. L’équipe Echord"

    

    menu: 
        a "Assez étrange comme email...Je pense que je devrais..."

        "Cliquer sur le lien et entrer le mot de passe.":
            $ bad_choices += 1
            jump badChoice_passwordStolen

        "Ne pas cliquer sur le lien et bloquer le compte.":
            $ good_choices += 1
            jump goodChoice_passwordSafe

label badChoice_passwordStolen:

    "Ca me parait être un vrai mail de Echord, mieux vaut leur envoyer mon mot de passe pour être sûr."
    "Ca sonnait assez urgent en tout cas... J'espère qu'ils ont pu rapidement intervenir."
    "Mais enfin bref ! Aujourd'hui, l'objectif c'est me connecter à [jeu] et de jouer toute la nuit."
    "Je dis ça mais je sais très bien que je suis somnolent dès 22h..."

    scene bg_bedroom_day with fade
    play music "music/Morning.mp3" fadeout 1.0 loop

    "Mmhh..."
    "Le réveil fut si doux avec le soleil qui frappe mon visage, aujourd'hui va encore être une belle journée."
    "Je prends mon téléphone pour regarder l'heure : 7h45. Oh non."
    "Je suis super en retard, je prends les premiers vêtements que je vois et je fonce vers la sortie."

    scene bg_frontGate_day with dissolve
    a "Enfin arrivé..."
    "Ce fut la COURSE dès le matin, ce qui me déplaît énormément je vais pas mentir. Le but de la vie c'est de profiter tranquillement, pas de vivre sous pression."
    i "Reste pas planté là [povname] enfin, rentre tu vas être en retard !"
    "Le surveillant au portail m'a ramené à la réalité, je m'empresse de rentrer."

    scene bg_classroom_day with dissolve
    "C'est rare que je fasse parti des derniers à arriver en classe mais parfois ça arrive même aux meilleurs. Sans plus attendre je m'installe, tandis que le cours commence."
    "En passant à côté de Bamoussa, je lui fais signe de la tête, mais il ne me regarde pas. C'est pas grave, on discutera pendant la pause."

    scene bg_courtyard_day with dissolve
    "Durant la pause, la première chose que je fais est d'interpeller Bamoussa."
    a "Hey mec ça va ? C'était trop bien hier, on y rejoue ce soir ?"
    "Bamoussa avait l'air... Perplexe ?"

    show bamoussa_anxious at center
    b "Ah salut..."
    a "Bah alors t'as pas l'air en forme, qu'est-ce qu'il se passe ?"
    b "En fait je me suis fait hacker mon compte Echord..."
    play music "music/Echoes_of_Time.mp3" fadeout 1.0 loop
    a "Mais nan comment s'est arrivé ?"
    b "Eh bien c'est ça le problème, j'ai été hacké à cause de toi, tu m'as envoyé un lien étrange sur Echord et j'ai cliqué dessus."
    "... A cause de moi ?"
    a "Mais attends je t'ai pas du tout envoyé de lien moi, comment tu peux m'accuser ?"
    hide bamoussa_anxious
    "Sans plus attendre, Bamoussa cherche au fond de sa poche son téléphone, l'allume et me montre notre conversation Echord."
    b "Regarde, est-ce que je mens ?"
    "Effectivement, je lui ai envoyé un message, enfin pas MOI, mais mon compte."
    "Cela voulait forcément dire que quelqu'un a pu avoir accès à MON compte. Et donc, à mes données personnelles."
    "Maintenant que j'y repense, c'était probablement au moment où j'ai tapé mon mot de passe sur l'étrange mail que j'ai dû perdre le contrôle..."
    "Je décide d'expliquer la situation à Bamoussa."
    show bamoussa_anxious at center
    b "C'était pas ta meilleure décision, tu m'as habitué à mieux [povname]."
    "Oups c'est pas faux..."
    b "Surtout que maintenant, y a pleins de personnes qui se moquent de moi sur notre groupe Echord, y a des messages privés qui ont été diffusés !"
    b "On dirait presque que c'est fait exprès !"
    a "C'est pas tes amis sur le groupe Echord ?"
    b "Non j'ai invité plein de personnes que je connais pas ou peu... Je m'étais dit que plus on était fous, plus on rit, mais pas rire de moi !"
    a "Bon alors qu'est-ce qu'on peut faire si on a tous les deux perdus le contrôle de nos comptes ?"
    b "J'ai ma petite idée, on va demander à quelqu'un que je connais, c'est une experte dans ce domaine."
    "Pourvu qu'il ne soit pas trop tard pour récupérer nos comptes..."
    "La fin de la récréation approche, on décide de se donner rendez-vous après les cours pour discuter avec la fameuse experte que Bamoussa connait."

    scene bg_roadToSchool_evening with fade
    play music "music/Covert_Affair.mp3" fadeout 1.0 loop
    "Les cours étant terminés, je suis Bamoussa à travers la ville pour aller voir la personne qui nous aiderait."

    scene bg_park_evening with dissolve
    b "On y est."
    "Le rendez-vous avait lieu dans un parc calme non loin de chez moi."
    i "Vous m'avez fait attendre !"
    "Notre experte était déjà là."

    show bamoussa_default at left
    b "[povname], voici Binta. Elle a déjà vécu une situation de cyberharcèlement, elle pourra nous aider."

    show Binta_default_happy at right
    b2 "Salut [povname], ravie de te rencontrer !"
    "Je lui serre la main."
    hide Binta_default_happy
    show Binta_explaining at right

    b2 "Alors, vos comptes Echord ont été hackés, c’est bien ça ?"
    a "Oui."
    "On sort nos téléphones. Moi, j’ai encore accès. Pas Bamoussa."
    b2 "[povname], change ton mot de passe tout de suite. Pour Bamoussa, c’est plus compliqué."

    hide bamoussa_default
    show bamoussa_anxious at left
    b "Je fais quoi alors ?"
    b2 "Tente 'mot de passe oublié' et regarde tes mails pour annuler un éventuel changement d’adresse."
    b2 "Contacte aussi le support avec des preuves, et change tes mots de passe ailleurs s’ils sont identiques."
    b "Et si ça ne marche pas ?"
    b2 "Alors il faudra prévenir tes proches, et créer un nouveau compte."

    "J’interviens."
    a "J’ai changé mon mot de passe. Et maintenant ?"
    b2 "Active l’authentification à deux facteurs, et déconnecte les appareils inconnus. Préviens tes proches au cas où."

    a "Merci encore !"
    b "Mais qui a pu faire ça ?"

    menu:
        a "Personnellement je pense..."

        "Que c'est un manque de bol.":
            $ bad_choices += 1
            jump culpritNotFound

        "Que ça a un rapport avec le groupe Echord.":
            $ good_choices += 1
            jump culpritFound

label culpritNotFound:
    a "Je pense qu'on a juste pas eu de chance."
    b2 "Peut-être, mais l'arrivée massive d’inconnus dans Echord est suspecte."
    a "C’est vrai… On aurait dû faire un groupe privé."
    b "Oui… Merci pour ton aide Binta."

label culpritFound:
    a "Ça a commencé après avoir rejoint le groupe Echord, non ?"
    b "Tu crois que ça vient de là ?"
    a "Très probable. Quelqu’un du groupe a dû s’en prendre à nous."
    b2 "C'était un groupe ouvert, sans modération. C’est dangereux."
    b "Je vais revoir les paramètres et mieux surveiller les membres."
    "Bamoussa ne dit rien, même s’il a ajouté beaucoup d’inconnus…"

    b2 "Besoin d’autre chose ?"
    b "Non, merci Binta, t’assures."
    b2 "Avec plaisir. N’hésitez pas à me recontacter."
    "Chacun rentre chez soi. Sacrée journée."

    jump endofChap1

label goodChoice_passwordSafe:
    "Je vais quand même pas mettre mon mot de passe n'importe où non ?"
    "Plusieurs points me dérange :"
    "Tout d'abord l'adresse email est suspecte : au lieu de @echord.com, on @securehelp.com."
    "J'ai déjà reçu des mails de Echord et c'est pas comme ça que les mails terminent. Pour savoir si ce sont de vrais mails, autant vérifier les anciens."
    "En plus, le message met la pression avec une menace de suspension, assez étrange tout de même de la part d'Echord."
    "J'avais lu sur internet que c'était une tactique souvent utilisé par les arnaqueurs."
    "Et surtout il y a beaucoup de fautes d'orthographe ! Il n'y en aurait eu aucune s'il s'agissait d'un vrai mail de Echord."
    "Enfin bref, heureusement que j'ai réfléchi avant de faire quoi que ce soit, sinon ça aurait pu être grave."
    "Mais enfin bref ! Aujourd'hui, l'objectif c'est me connecter à [jeu] et de jouer toute la nuit."
    "Je dis ça mais je sais très bien que je suis somnolent dès 22h..."

    scene bg_bedroom_day with fade
    play music "music/Morning.mp3" fadeout 1.0 loop

    "Mmhh..."
    "Le réveil fut si doux avec le soleil qui frappe mon visage, aujourd'hui va encore être une belle journée."
    "Je prends mon téléphone pour regarder l'heure : 7h45. Oh non."
    "Je suis super en retard, je prends les premiers vêtements que je vois et je fonce vers la sortie."

    scene bg_frontGate_day with dissolve
    a "Enfin arrivé..."
    "Ce fut la COURSE dès le matin, ce qui me déplaît énormément je vais pas mentir. Le but de la vie c'est de profiter tranquillement, pas de vivre sous pression."
    i "Reste pas planté là [povname] enfin, rentre tu vas être en retard !"
    "Le surveillant au portail m'a ramené à la réalité, je m'empresse de rentrer."

    scene bg_classroom_day with dissolve
    "C'est rare que je fasse parti des derniers à arriver en classe mais parfois ça arrive même aux meilleurs. Sans plus attendre je m'installe, tandis que le cours commence."
    "En passant à côté de Bamoussa, je lui fais signe de la tête, mais il ne me regarde pas. C'est pas grave, on discutera pendant la pause."

    scene bg_courtyard_day with dissolve
    "Durant la pause, la première chose que je fais est d'interpeller Bamoussa."
    a "Hey mec ça va ? C'était trop bien hier, on y rejoue ce soir ?"
    "Bamoussa avait l'air... Perplexe ?"

    show bamoussa_anxious at center
    b "Ah salut..."
    a "Bah alors t'as pas l'air en forme, qu'est-ce qu'il se passe ?"
    b "En fait je me suis fait hacker mon compte Echord..."
    play music "music/Echoes_of_Time.mp3" fadeout 1.0 loop
    a "Mais nan comment s'est arrivé ?"
    b "J'ai reçu un mail étrange de Echord qui me demandait de vérifier mon compte car il y a eu une connexion suspecte... Et au final, regarde où j'en suis."
    b "Surtout que maintenant, y a pleins de personnes qui se moquent de moi sur notre groupe Echord, y a des messages privés qui ont été diffusés !"
    b "On dirait presque que c'est fait exprès !"
    a "C'est pas tes amis sur le groupe Echord ?"
    b "Non j'ai invité plein de personnes que je connais pas ou peu... Je m'étais dit que plus on était fous, plus on rit, mais pas rire de moi !"
    a "C'est pas ta meilleure décision... Mais enfin bref tu sais ce que tu pourrais faire ?"
    b "J'ai ma petite idée, on va demander à quelqu'un que je connais, c'est une experte dans ce domaine."
    "La fin de la récréation approche, on décide de se donner rendez-vous après les cours pour discuter avec la fameuse experte que Bamoussa connait."


    scene bg_roadToSchool_evening with fade
    play music "music/Covert_Affair.mp3" fadeout 1.0 loop
    "Les cours terminés, je suis Bamoussa à travers la ville. Il m’emmène voir quelqu’un qui pourrait nous aider."

    scene bg_park_evening with dissolve
    b "On est arrivés."
    "Le rendez-vous avait lieu dans un petit parc calme. Une femme nous attendait déjà."
    i "Vous m'avez bien fait attendre !"
    "Voici notre experte."

    show bamoussa_default at left
    b "Je te présente Binta. Elle a déjà vécu une situation de cyberharcèlement. Elle va pouvoir nous aider."

    show Binta_default_happy at right
    b2 "Salut [povname], ravie de te rencontrer !"
    "Je la salue."

    hide Binta_default_happy
    show Binta_explaining at right
    b2 "Alors, vos comptes Echord ont été hackés ?"
    a "Non, juste celui de Bamoussa."
    b2 "Regarde si tu peux encore y accéder."
    "Bamoussa tente de se connecter. Impossible."

    b2 "Mot de passe changé. Essaie de le réinitialiser avec 'mot de passe oublié'."
    b2 "Et vérifie tes mails, parfois on peut annuler un changement suspect."
    hide bamoussa_default
    show bamoussa_anxious at left
    b "Ok, je vais tester. Et si ça marche pas ?"
    b2 "Contacte le support, envoie des preuves. Et change tes mots de passe ailleurs si tu les as réutilisés."

    b "Merci beaucoup… et si je récupère pas le compte ?"
    b2 "Crée-en un nouveau, et préviens tes proches."

    a "Et s’il avait encore accès à son compte ?"
    b2 "Il aurait dû changer le mot de passe, activer l’authentification à deux facteurs et déconnecter tous les appareils."

    a "Et prévenir ses proches s’il y a eu des messages suspects, j’imagine ?"
    b2 "Exactement."

    a "Tu nous sauves vraiment la mise, merci !"
    b "Mais… qui a pu hacker mon compte ?"

    menu:
        a "Personnellement je pense…"

        "Que c'est un manque de bol.":
            $ bad_choices += 1
            jump culpritNotFound

        "Que ça a un rapport avec le groupe Echord.":
            $ good_choices += 1
            jump culpritFound2

label culpritFound2:
    a "C’est bizarre que ça ait commencé juste après la création du groupe, non ?"
    b "Tu crois que ça vient de là ?"
    a "C’est très probable. N’importe qui pouvait rejoindre avec un lien."
    b2 "Oui, c’était ouvert, donc sans modération, n’importe qui a pu s’infiltrer."
    b "Je vais revoir les paramètres, limiter les invitations. Faut que je sache qui entre dans le groupe."

    "Bamoussa ne dit rien, mais il sait qu’il a lui-même ajouté pas mal d’inconnus… oups."

    b2 "Besoin d’autre chose ?"
    b "Non, merci Binta. T’es au top."
    b2 "Avec plaisir. Et si besoin, appelez-moi !"

    "Après quelques mots, chacun rentre chez soi. Fin de journée mouvementée."


label endofChap1: 
    scene bg_bedroom_night_lightOff
    play music "music/Late Night Radio.mp3"

    "La sécurité est tellement importante sur Internet et je ne me rends pas vraiment compte. Comme Bamoussa je pourrais me faire harceler du jour au lendemain si je fais pas attention à qui je parle."
    "Je me mets au lit et j'éteins les lumières. Avant de m'endormir je regarde un peu mon téléphone."
    "J'ai reçu une nouvelle notification: une demande d'amie sur Echord. Qui ça peut bien être ?"
    "Pour l'instant ce n'est pas très important, je décide d'être mon téléphone et de m'endormir."

    centered "{size=+75}{cps=8}{color=#ffffff}Chapitre 1{/color}{/cps}{/size}{p=5.0}{nw}" 
    centered "{size=+75}{cps=8}{color=#ffffff}terminé{/color}{/cps}{/size}{p=5.0}{nw}"


label chapter2: 
    scene bg_bedroom_day with fade
    play music "music/Morning.mp3"

    "Les doux rayons du soleil viennent me révéiller quelques minutes avant la sonnerie de mon réveil. Ca c'est une belle matinée."
    centered "{size=+75}{cps=8}{color=#ffffff}Chapitre 2{/color}{/cps}{/size}{p=5.0}{nw}"

    scene bg_livingRoom_day with dissolve
    "Je prends mon petit déjeuner et me prépare à sortir."
    "Après les événements du groupe Echord, Bamoussa a supprimé et créé un nouveau compte où seul ses amis peuvent le contacter."
    "C'est important de rester aux aguets quand on est sur Internet, mais parfois on ne fait pas attention."
    "Les harceleurs du groupe Echord n'ont pas essayé de me viser, mais il faut être prudent dans ce genre de situations."
    "Je prends mon sac juste à côté de la porte, et je pars pour une journée de cours."

    scene bg_livingRoom_evening with dissolve
    play music "music/Evening.mp3"
    "Après ma longue journée, je n'ai qu'une hâte : c'est de me connecter sur mon pc. J'ai hâte de pouvoir jouer et enfin décompresser."
    "Ma mère et moi discutons d'abord de notre journée, c'est notre tradition après tout."
    "Après notre petite discussion, je monte à ma chambre pour jouer."

    scene bg_bedroom_afterSchool with dissolve
    "J'allume mon ordinateur pour voir la notification de la veille."
    "Un certain, ou certaine \"Lunamystique <3\" cherche à m'ajouter."
    menu: 
        "Avec tout ce qui s'est passé récemment je devrais..."

        "Accepter l'invitation.":
            $ bad_choices += 1 
            jump invitationAccepte
        
        "Refuser l'invitation.":
            $ good_choices += 1
            jump invitationRefuse

label invitationAccepte:
    "Je reçois un message quasiment immédiatement."
    l "Salut! J'ai vu tes messages sur le groupe Echord de [jeu] et tu as l'air super cool. Ça te dirait de discuter un peu?"
    menu:
        "Accepter de discuter":
            $ bad_choices += 1 
            jump acceptChat
        "Ignorer le message":
            $ good_choices += 1
            jump ignoreChat
label ignoreChat:
    "Je pense qu'il est préférable de ne pas répondre. Après tout, je ne connais même pas la personne."
    "Vu les événements récents je pense qu'il faut se méfier de toute personne que je ne connais pas."
    "Je supprime le message."
    "A présent il est temps de jouer !"
    jump afterRefusing

label acceptChat:
    "Je décide de répondre."
    a "Salut! Oui pourquoi pas, tu es nouveau ici?"
    l "Nouvelle oui, je découvre un peu le serveur Echord que Bamoussa a créé autour de [jeu]. Tu joues à quoi en ce moment?"
    a "Surtout à [jeu], et toi?"
    play music "music/Symmetry.mp3"
    l "Ah, je connais! D'ailleurs, j'ai un serveur privé avec des potes, tu veux nous rejoindre?"
    "Son ton est amical, mais quelque chose semble étrange."

    menu:
        "Accepter de rejoindre":
            jump askServerInfo
            $ bad_choices += 1
            $ hasTalkedToBullies = True

        "Refuser poliment":
            $ good_choices += 1
            jump refuseChat

label askServerInfo:
    a "Super intéressant je suis partant ! C'est quoi l'adresse du serveur ?"
    l "Oh, je peux te l'envoyer, mais j'aurais besoin de ton email et une photo de toi pour te donner l'accès."
    "C'est bizarre. Pourquoi demander mon email ? Et surtout une photo ?"
    "Je lui pose la question."
    l "Ahah ne t'en fais pas, c'est juste pour bien vérifier que c'est toi !"
    a "Ok..."
    "Super étrange. J'ai vu dans des vidéos que c'était possible de faire des montages super détaillés avec les deepfake."
    "Après elle a bien dit que c'était pour l'identification... Je lui envoie une photo de moi."
    l "Parfait. Je t'envoie le lien."
    "Après deux minutes d'attente, elle décide enfin de m'envoyer une invitation !"
    "Je décide de rejoindre."
    "Une fois arrivée, elle m'envoie de nouveau un message."
    l "Viens sur la discussion vocale, qu'on puisse parler, je te présenterai à mes amis !"
    "Et pourquoi pas ? Ils jouent probablement tous à [jeu] maintenant."
    "Une fois le groupe rejoint, une multitude de voix explose mes tympans."
    i "T'as vu ta tête ? Sérieux, t'aurais dû réfléchir avant d'envoyer ça."
    i "Quelqu'un l'a screenshotté ? Faut qu'on garde ça !"
    i "C'est quoi cette créature ?"
    "Un flot incessant d'insultes et de moqueries m'assaille."
    l "C'est bon les gars arrêtez..."
    l "Pardonne leur ils sont un peu bêtes."
    i "Ouais j'espère que tu nous en voudras pas !"
    a "Euh ouais tranquille c'est pas grave..."
    "Ils font une très mauvaise première impression..."
    "Je décide de rester avec eux pour jouer un temps à [jeu], c'est pour ça que je suis dessus d'ailleurs."
    "Les moqueries continuent mais sont moins agressives, je ressens tout de même une certaine tension."
    "A la fin de nos parties, les moqueries reprennent de plus belles."
    i "Pourquoi il est encore là ? Personne l'aime."
    i "Allez, pleure un coup, ça ira mieux."
    "Comment c'est possible d'être aussi mauvais ? En regardant plus précisément leur serveur Echord, je me rends compte que ces derniers harcèlent bien des gens."
    "Ils ajoutent des individus qu'ils rencontrent un peu partout, pour ensuite se moquer d'eux."
    "Il y a plusieurs canaux de discussion avec des images de d'autres personnes. Certaines images représentent les individus dénudés."
    "Dans ces canaux, on y voit donc leurs insultes, mais aussi les chantages que ces derniers font à leurs victimes."
    "Ils utilisent donc leur serveur Echord comme un moyen d'organiser leur cyberharcèlement... Ce sont des monstres !"
    "Ayant été sincèrement blessé par leur propos et par ce que j'ai vu, je décide de quitter et bloquer le groupe Echord."
    "Et si c'était eux à l'origine de l'harcèlement de Bamoussa ?"

    jump afterRefusing
        

label refuseChat:
    "C'est hors de question de rejoindre un serveur rempli d'inconnus."
    "j'ai vu des vidéos. Des vidéos horribles."
    "Des personnes se font ajouter sur des serveurs, où du contenu illégal est diffusé."
    "On harcèle moralement les victimes qui se font ajouter sur ces serveurs: au début on me demandera pas grand chose, et petit à petit les choses empireront."
    "Des photos de moi puis plus l'harcèlement continue et plus les demandes deviennent cruelles."
    "Mais on ne me l'a fait pas à moi."
    a "C'est gentil mais non merci."
    "Je supprime la personne de mes amis Echord."
    jump afterRefusing

label invitationRefuse:
    "Je pense qu'il est préférable de ne pas accepter l'invitation. Après tout, je ne connais même pas la personne."
    "Vu les événements récents je pense qu'il faut se méfier de toute personne que je ne connais pas."
    "Je supprime l'invitation."
    "A présent il est temps de jouer !"
label afterRefusing:
    scene bg_bedroom_night_lightOn with dissolve
    play music "music/Late Night Radio.mp3"

    "Après ma petite session de jeu, il est enfin temps d'aller dormir."
    "J'éteins mon ordinateur, et m'apprête à éteindre la lumière."
    "Cependant, une nouvelle notification sur mon téléphone vient interrompre mon rituel nocturne."
    "Une nouvelle fois, l'individu essaie de m'inviter."
    "Je vais le bloquer, ça sera bien plus simple."
    "Après autant de stress il est temps pour moi d'aller me coucher."
    "La journée fut épuisante, et cette soirée encore plus. Je n'ai pas pu jouer tranquillement sans stresser..."

    centered "{size=+75}{cps=8}{color=#ffffff}Chapitre 2{/color}{/cps}{/size}{p=5.0}{nw}" 
    centered "{size=+75}{cps=8}{color=#ffffff}terminé{/color}{/cps}{/size}{p=5.0}{nw}"

label chapter3:
    scene bg_bedroom_day with fade
    play music "music/Morning.mp3"

    "Comme à mon habitude, je me lève tranquillement afin de commencer la journée sans stress."
    "J'ai passé une nuit assez agitée avec ce qui s'est passé hier... Je me prépare et pars de chez moi, espérant que la journée me changera les idées."

    scene bg_roadToSchool_day with dissolve
    "Sur le trajet vers l'école, je reçois une nouvelle notification. Il s'agit d'un mail d'un certain Stéphane Kouadi"
    "Je décide de la lire."
    "Objet : Félicitations [povname], vous avez été sélectionné !"
    "Je me permets de vous contacter car vous avez été tiré au sort dans le cadre de notre grand jeu concours \"Jeunes Connectés 2025\", organisé en partenariat avec Samsung."
    "🎉 Félicitations ! Vous avez remporté un Samsung Galaxy Ultra S25 (valeur 1299€)."
    "Afin de recevoir votre lot, il vous suffit simplement de régler les frais de livraison internationaux, d’un montant unique de 45€, par transfert Petpat à notre comptable agréé."
    "Sinon, il vous sera demandé une photo de vous, torse nu avec une pancarte \"Merci pour le Samsung Galaxy Ultra S25\" comme paiement."
    "Veuillez effectuer le paiement dès aujourd’hui pour garantir l’envoi de votre téléphone sous 72h ouvrables."
    "Merci de votre réactivité, et encore bravo pour votre participation !"

    "Euh... Je ne sais pas trop quoi penser. Surtout de la photo qui m'est demandé."
    menu: 
        "Je pense que c'est un fake. Mieux vaut ignorer":
            $ good_choices += 1
            jump fake
        
        "C'est probablement un vrai jeu concours.":
            $ bad_choices += 1
            jump participeConcours

label fake:
    "C'est une évidence que le mail est faux. Ca en est presque risible."
    "Tout est faux : le jeu concours, le lot à gagner, les frais de port... Ne parlons pas de la photo qui est demandé."
    "Je pourrais très bien faire une recherche sur internet, et voir que les jeunes connectés 2025 n'existe pas. Je n'y ai même pas participé c'est pour dire !"
    "Et je sais déjà de quoi il s'agit : ce sont les mêmes harceleurs du Echord qui essaient de me contacter."
    "Ce qui est inquiétant c'est qu'ils ont pu trouver mon adresse email... Quoi d'autre pourront-ils trouver sur moi ensuite ?"
    "L'anxiété monte en moi. J'ai l'impression que tous les regards se posent sur moi."
    "J'arrive bientôt devant l'école. Une fois là-bas je sais que je me sentirais déjà plus en sécurité..."
    "Je vais expliquer la situation à Bamoussa, il doit savoir et ne pas faire confiance à n'importe qui."

    scene bg_classroom_day with dissolve
    "Une fois arrivé en classe, j'explique la situation à Bamoussa."
    show bamoussa_anxious at center
    b "J'en suis sûr qu'il s'agit des mêmes personnes du groupe Echord, il essaie de nous manipuler pour ensuite nous harceler."
    "J'ai regardé leur mode opératoire sur Vtube, et ils essaient d'obtenir des informations sur nous pour nous harceler en ligne comme dans la vraie vie."
    a "J'ai eu raison de me méfier alors..."
    "Mes soupçons se confirment. D'où la demande d'une photo. Je pense qu'il s'agit d'un moyen pour eux d'avoir une emprise psychologique sur nous."
    "Je ne compte pas me laisser faire en interagissant avec eux."
    b "Bloque ce mail, et on verra un adulte après les cours. Il faudrait en parler à nos parents aussi."
    if hasTalkedToBullies == True:
        "J'explique d'ailleurs à Bamoussa la discussion que j'ai eu sur le serveur."
        b "je reconnais leur nom... C'était des gens qui m'ont aussi contacté une fois. Ces personnes sont horribles."
        b "On doit clairement éviter de parler à n'importe qui sur internet."
        a "Pas faux..."
        "La cloche sonne, signalant le début de la récréation. Bamoussa et moi continuons notre discussion sur le phishing et comment s'en prémunir."

    else:
        "La cloche sonne, signalant le début de la récréation. Bamoussa et moi continuons notre discussion sur le phishing et comment s'en prémunir."


    jump afterEmail


label participeConcours:
    "Oh trop bien un jeu concours ! Vu le nombre de fois où je participe sans gagner, ça fait du bien d'enfin réussir."
    "Un peu étrange tout de même de pouvoir payer avec une image, mais je n'ai pas d'argent, donc ça m'arrange !"
    "Je vais en parler à Bamoussa quand j'arrive au collège, il sera trop jaloux !"
    scene bg_classroom_day with dissolve
    "Une fois arrivé en classe, j'explique la situation à Bamoussa."
    show bamoussa_anxious at center
    b "J'en suis sûr qu'il s'agit des mêmes personnes du groupe Echord, il essaie de nous manipuler pour ensuite nous harceler."
    a "Il ne ferait quand même pas ça... Si ?"
    b "Réfléchis un peu; tu trouves pas étrange qu'on te contacte depuis que tu as rejoint le serveur Echord. On est la cible d'une ou plusieurs personne."
    "Il a pas tort... Comment ne l'ai-je pas vu avant ?"
    b "Bloque ce mail, et on verra un adulte après les cours. Il faudrait en parler à nos parents aussi."

label afterEmail:
    scene bg_livingRoom_evening with fade
    play music "music/Evening.mp3"

    "Une fois arrivée chez moi, je décide de tout expliquer à ma mère."
    "Elle était tout d'abord choquée quand j'ai commencé mon histoire, puis son choc est passé à l'énervement."
    "Ce n'est pas contre moi qu'elle était énervée. C'est contre ces individus qui nous ciblent qu'elle l'est."
    "Dans la hâte, elle m'emmène au commiseriat afin de porter plainte contre mes harceleurs."

    scene bg_bedroom_night_lightOff with dissolve
    play music "music/night_time.mp3"

    "Ces derniers jours m'ont beaucoup fait réfléchir à la sécurité sur Internet."
    "Je pensais que ça n’arrivait qu’aux autres. Qu’on repérait facilement les arnaques, les faux profils, les pièges. Mais la vérité, c’est qu’ils savent exactement comment s’y prendre."
    "Il y a des individus mal intentionnés dans notre monde, qui chercheront par tous les moyens possibles de te détruire par pur plaisir."
    "Derrière un écran, tout le monde peut mentir. En sachant cela, on a tous intérêt à apprendre comment vivre ensemble, ou sinon à apprendre à se protéger."

    if bad_choices < 3:
        "Je réfléchis à tout ça avant de m'endormir paisiblement."

    else:
        "J'ai énormément de mal à dormir ces derniers jours. Les pensées se bousculent, et j'ai l'impression de m'engouffrer peu à peu dans un sombre abysse."
        "C'est fou de se dire que certaines personnes veulent juste faire souffrir une autre. Qu'ont-ils à y gagner ? Ce genre de plaisir sadique devrait être puni."

    centered "{size=+75}{cps=8}{color=#ffffff}Chapitre 3{/color}{/cps}{/size}{p=5.0}{nw}" 
    centered "{size=+75}{cps=8}{color=#ffffff}terminé{/color}{/cps}{/size}{p=5.0}{nw}"

   

    scene bg_black_screen with fade:
        xalign 0.5
        yalign 0.2
        zoom 2.0

    centered "Nombre de bons choix : [good_choices]"
    centered "Nombre de mauvais choix : [bad_choices]"
    centered "{size=+75}{cps=8}{color=#ffffff}CRÉDITS{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}Scénario: Étudiants de Louise Michel{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}programmation: Vegacy{/color}{/cps}{/size}{p=5.0}{nw}"


    return
