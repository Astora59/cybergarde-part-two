# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define a = Character('Adil', color="#000000")
define b = Character('Bamoussa', color="#000000")
define i = Character("???", color="#000000")
define m = Character("Maman", color="#000000")
#characters-sprites
#Bamoussa
image bamoussa_default = "bamoussa_default.png"




#backgrounds
#school
image bg_classroom_day = "classroom_day.jpg"
image bg_classroom_evening = "classroom_evening.jpg"
image bg_classroom_night_lightOff = "classroom_night_lightOff.jpg"
image bg_classroom_night_lightOn = "classroom_night_lightOn.jpg"
image bg_frontGate_day = "frontGate_day.jpg"
image bg_frontGate_evening = "frontGate_evening.jpg"
image bg_frontGate_night = "frontGate_night.jpg"

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

#ending
image bg_black_screen = "black.jpg"

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


# Le jeu commence ici
label start:
    stop music
    "Cette oeuvre est un travail de fiction. Toute ressemblance à des personnes ou des événements est totalement fortuite."
    "Si vous êtes témoin de toute forme d'harcèlement ou de cyberharcèlement, ne laissez pas faire ces actions et contactez les autorités compétentes."

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
    "\"Yo mec c'était trop cool hier la game, t'es chaud de rejoindre le groupe discord que j'ai créé ?\""
    "C'était Bamoussa, un ami avec qui j'ai joué hier."
    a "Hello mon gars... Avec plaisir... Envoie le lien. Hop et envoyé !"
    "C'est vrai que pour jouer à des jeux vidéo à plusieurs, Discord est bien meilleur que de passer par le chat vocal du jeu."
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
    "Récemment on joue à un nouveau jeu : MonHun : Wilds ! Il faut chasser des monstres de plus en plus massifs pour être le meilleur chasseur !"
    "Je viens d'arriver au rang expert, mes amis sont encore au rang novice... Pff les noobs !"
    "On finit par arriver non loin du collège après une discussion des plus passionnantes..."

    scene bg_frontGate_day with dissolve
    "Arrivé devant le collège, mes collègues chasseurs s'empressent d'entrer."
    "De mon côté, j'arrive très sereinement au portail, je suis du genre à éviter de me presser pour rien."
    "La vie est vraiment belle quand on a de bonnes notes n'empêche..."
    "Aujourd'hui on commence avec un cours d'anglais, c'est probablement ma matière préférée vu que je suis le meilleur de la classe."
    "Je me rends, le pas léger, en classe."

    scene bg_classroom_day with dissolve
    "Une fois assis sur ma chaise, une voix familière vient m'interpeller."
    i "Yo Adil !"

    show bamoussa_default at center
    b "Alors t'as pu voir mon message ?"
    "C'était Bamoussa qui m'interpellait. Comme moi, il est du genre à être très serein. C'est vraiment apaisant d'avoir un ami comme lui."

    if hasCheckedNotification == True:
        a "Bien sûr ! J'ai rejoint le groupe, trop hâte de pouvoir jouer en appel ça sera beaucoup plus simple."
        b "Oh ouais carrément, les appels sur Whatsapp c'est pas très évident..."
        a "Y a qui sur le groupe d'ailleurs ?"
        b "Oh tu sais quelques amis à moi et des personnes que j'ai rencontré sur MonHun, ils sont grave sympas donc t'as pas de soucis à te faire !"
    else:
        "Je n'ai même pas regardé cette notification. Oups !"
        a "Euh... J'avoue je n'ai même pas regardé..."
        b "Oh mec fais un petit effort ! Tu risques de faire pleurer ton meilleur ami là !"
        a "Ahah oui désolé... Alors c'était à propos de quoi ?"
        b "Je t'ai ajouté sur un groupe discord pour qu'on puisse jouer à MonHun avec d'autres personnes !  "
        a "Y a qui sur le groupe ?"
        b "Oh tu sais quelques amis à moi et des personnes que j'ai rencontré sur MonHun, ils sont grave sympas donc t'as pas de soucis à te faire !"
    
    "De nouveaux chasseurs dans l'équipe... Ca pourrait être sympa franchement, il y a beaucoup de monstres durs à chasser donc c'est important d'avoir des alliés."
    a "Bah écoute ce soir je suis partant pour y jouer ! Tu seras là ?"
    b "Bien sûr ! Je me connecterai vers 20h, sois là !"
    i "A vos places s'il vous plait le cours commence !"
    "Le professeur vient interrompt notre conversation."
    "Je fais un signe de confirmation de la tête à Bamoussa tandis qu'il retourne à son siège."
    "Ce soir c'est décidé, ça sera une soirée gaming !"

    scene bg_roadToSchool_evening with fade
    "La cloche fait enfin retentir la fin de la journée, il est temps de rentrer à la maison et de faire ses devoirs."

    scene bg_livingRoom_evening with dissolve
    "Je suis rentré !"
    "Enfin arrivé chez moi, je me déchausse pour enfiler mes pantoufles, c'est le signal qu'une belle soirée peut commencer."
    m "La journée s'est bien passé ?"
    "Ma mère, depuis la cuisine, prépare un copieux repas qui charme déjà mes sens."
    "Je reste un peu avec elle pour raconter nos journées, et ensuite c'est devoirs puis douche !"

    scene bg_bedroom_afterSchool with dissolve
    "Une fois enfin posé, j'allume enfin mon ordinateur."
    "Avant de commencer à jouer, je regarde mes mails. On ne sait jamais, on peut toujours recevoir des mails intéressants !"
    "D'ailleurs, je pouvais en voir un très intéressant"
    a "Un mail de Discord..."
    "Je commence à lire le mail."
    "De : support-discord@securehelp.com"
    "Objet : ⚠️ Action requise : Vérification de votre compte Discord"
    "Nous avons détecté une activité inhabituelle sur votre compte Discord et nous soupçonnons une connexion non autorisée depuis Cluj-Napoca, Roumanie."
    "📌 Détails de la connexion suspecte :"
        




    return
