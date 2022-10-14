# Text version vom Spiel Detroit become human, nocht nicht fertig
# TODO: mark clues that unlock special options
# 0 = starting corridor
import time
room = 0
game_state = {
  "fish_saved": False,
  "chance_of_success": 50,
  "software_instability": 0,
  "talked_to_captain_allen": False,
  "looked_at_emmas_tablet": False,
  "looked_at_fathers_tablet": False,
  "has_gun": False,
  "done": False
}
# first time texts
def living_room_text():
  print_yellow("Allen: Haltet die Positionen. Der Vermittler greift jetzt ein.")
  print_yellow("SWAT: In Position. Bereit zum Zugriff.")

def intro_text():
  print_yellow("SWAT: Vermittler vor Ort. Wiederhole, Vermittler ist jetzt vor Ort.")
  print_purple("Caroline Phillips: Nein, halt ... ich ... ich kann sie nicht allein lassen. Bitte, bitte, retten Sie meine Kleine ... Was ... Sie schicken einen Androiden? ")
  print_yellow("SWAT: Okay, Ma’am. Wir müssen jetzt gehen.")
  print_purple("Caroline Phillips: Das ... das können Sie doch nicht machen! Sie ... Warum schicken Sie keinen echten Menschen? Lasst dieses Ding nicht zu ihr! Haltet das Ding von meiner Tochter fern! LASST ES NICHT ZU IHR! ")
  print_yellow("Allen: Warum verschwenden wir Zeit und lassen einen Androiden verhandeln? Dieses Stück Sche*ße kann jederzeit vom Dach springen. IST MIR SCHE*SSEGAL! Meine Männer sind auf der Stelle einsatzbereit! F*ck! Nicht zu fassen ... ")
# interactions
def handle_aquarium():
  if game_state["fish_saved"]:
    print_green("Du guckts in das Aquarium rein und siehst ein Schönes Fisch, das glücklich umher schwimmt")
  else:
    print_green("Du guckt in das Aquarium rein und bemerkt, dass da keine Fische sind\nDu siehst einen hilflosen aber lebendigen Fisch auf dem Boden neben es")
  return True
  
def handle_picture():
  print_green("Du guckst das Familienbild auf dem Tresen an")
  print_blue("Bildinhalt wird analysiert...")
  print_blue("Philips, John  Geboren: 11.10.1999")
  print_blue("Philips, Caroline  Geboren: 23.05.2003") 
  print_blue("Philips, Emma  Geboren: 02.09.2028")
  return True

def handle_gun_case():
  print_green("Du analysierst den lehren Waffenkoffer...")
  print_blue('Waffenkoffer für Pistolenmodell "MS853 Black Hawk"')
  print_blue("Nebem den Koffer liegt eine Schachtel von .355 Munition")
  print_blue("*Der Abweichler nahm die Waffe des Vaters*")
  change_chance_of_success(3, "Informationen gefunden")
  
def handle_headphones():
  print_green("Du hebst die Kopfhörer vom Boden auf")
  print_blue("Es spielt noch Musik")
  print_blue("*Kind hörte keine Schüsse*")
  change_chance_of_success(6, "Informationen gesammelt")

def handle_tablet():
  print_green("Du nimmst das Tablet und spielst ein Video ab")
  print_purple("Emma: Das ist Daniel, der coolste Android auf der Welt! Sag hi, Daniel!")
  print_red("Daniel: Hallo.")
  print_purple("Emma: Du bist mein bester Freund und zwar für immer!")
  print_blue("*Abweichlername: Daniel*")
  game_state["looked_at_emmas_tablet"] = True
  change_chance_of_success(9, "Informationen gesammelt")

def handle_blue_blood():
  print_green("Du analysierst das Blaue Blut vom Abweichler")
  print_blue("Frisches blaues Blut")
  print_blue("Modell Pl600 - Seriennummer 369 911 047")
  print_blue("Android verwundet")
  print_blue("*Abweichlermodell: PL600*")
  change_chance_of_success(2, "Informationen gesammelt")

def handle_shoe():
  print_green("Du analysierst den Schuh")
  print_blue("Kinderschuh")
  print_blue("Buntes Modell")
  print_red("Spuren menschlichen Bluts")
  print_blue("*Geisel könnte verletzt sein*")
  change_chance_of_success(3, "Informationen gesammelt")

def handle_dead_father():
  print_green("Du analysierst Die Leiche des Vaters...")
  print_red("Verstorben: Phillips, John")
  print_red("Geschätzter Todeszeitpunkt: 19:29 Uhr")
  print_blue("Schusswunde Kaliber .355: Lungenblutung, Innere Blutung")
  print_blue("Schusswunde Kaliber .355: Lungenblutung, Pneumothorax")
  print_blue("Schusswunde Kaliber .355: Lungenblutung: Linke Niere perforiert, Tödliches Abdominaltrauma")
  print_blue("*Vater hielt Tablet in der Hand*")
  change_chance_of_success(3, "Informationen gefunden")

def handle_father_tablet():
  print_green("Du hebst das Tablet vom Boden auf und entsperrst es")
  print_purple("Tablet: Ihre Bestellung eines AP700-Androiden wurde registriert. CyberLife bedankt sich für Ihren Einkauf.")
  print_blue("*Abweichler sollte ersetzt werden*")
  change_chance_of_success(4, "Informationen gesammelt")
  game_state["looked_at_fathers_tablet"] = True

def handle_dead_officer():
  print_green("Du analysierst die Leiche des Polizisten")
  print_blue("DPD-Officer war Erster vor Ort")
  print_red("Verstorben: P.O Deckart, Antony")
  print_red("Geschätzter Todeszeitpunkt: 20:03")
  print_blue("Schusswunde Kaliber .355: Rechte Herzkammer perforiert, Innere Blutung")
  print_blue("Schussrückstände an der Hand: Bleityphnat, Antimonsulfid")
  print_blue("Nur ein Schuss")
  print_blue("Geisel sah die Schiesserei")
  print_blue("Polizist verletzte den Abweichler")
  print_blue("*Waffe des Polizistin unter dem Tisch geortet*")
  change_chance_of_success(3, "Informationen gesammelt")

def handle_gun():
  print_green("Du hebst die Waffe unter dem Tisch auf")
  print_blue("Art. 544-7 Amerikanische AndroidenVerordnung - 2029")
  print_red("Androiden ist es strengstens untersagt, Waffen jeglicher Art zu tragen oder zu benutzen")
  inp = boolean_question("Waffe nehmen?")
  if inp:
    game_state["has_gun"] = True
    print_green("Du steckst die Pistole ein")
    change_chance_of_success(7, "Tödliche Option verfügbar")
  else:
    print_green("Du legst die Pistole zurück unter dem Tisch")
    return True
    
def handle_window():
  print_green("Du guckst unauffällig aus dem Fenster heraus zur Terasse und siehst den Abweichler zusammen mit der Geisel")
  print_blue("Geisel geortet")

def handle_stove():
  print_green("Du siehst ein überfüllenden Topf auf ein noch angestelltes Herd")
  print_blue("Familie wollte zu Abend Essen")

def handle_tv():
  print_green("Du machst den Ton vom Fernseher an")
  print_purple("Reporter - ITM TV: Seit einer Stunde wird ein Mädchen auf einer Dachterrasse als Geisel festgehalten – hier im Zentrum von Detroit. Noch steht nicht fest, was genau passiert ist, aber der Täter scheint der Android der Familie zu sein. Er hat vermutlich ein Familienmitglied und einen Polizisten getötet ... Bestätigt es sich, wäre das der erste Fall eines Androiden, der absichtlich Menschen tötet. Alles spricht dafür, dass sich das Einsatzkommando auf einen Angriff vorbereitet. Und ...")

def handle_shot_officer():
  print_green("Du guckst den verwundeten Polizist an")
  print_yellow("Cop: Bitte ... Bitte hilf mir ...")
  print_green("Du: Er verliert Blut. Wenn er nicht in ein Krankenhaus kommt, überlebt er das nicht.")
  print_red("Daniel: Alle Menschen sterben irgendwann. Was macht es schon, wenn der hier jetzt stirbt?")
  print_green("Du: Ich lege ihm einen Druckverband an.")
  print_red("Daniel schießt einen Warnschuss")
  print_red("Daniel: Fass ihn nicht an! Finger weg oder du stirbst!")
  inp = boolean_question("Daniel ignorieren und trotzdem Druckverband anlegen?")
  if inp:
    print_green("Du legst ihm einen Druckverband mit deiner Krawatte an")
    print_green("Du: Du kannst mich nicht töten. Ich lebe nicht.")
    change_chance_of_success(-2, "Abweichler wird instabil")
  else:
    print_green("Du: Okay")
    change_chance_of_success(2, "Abweichler stabilisiert sich")


# Talk options
def calm_option():
  print_green("Du: Ich weiß, du bist wütend, Daniel. Aber du musst mir vertrauen und dir helfen lassen.")
  print_red("Daniel: Ich will keine Hilfe! Niemand kann mir helfen! Es soll einfach alles aufhören ... ich ... ich will nur, dass alles aufhört ...")
  change_chance_of_success(3, "Abweichler stabilisiert sich")

def release_hostage_option():
  print_green("Du: Lass jetzt bitte Emma gehen. Sie ist nur ein kleines Kind, sie hat nichts mit all dem zu tun.")
  print_red("Daniel: Niemals! Sobald ich sie loslasse, erschießt ihr mich. Aber so dumm bin ich nicht! Nein, so dumm bin ich nicht ..")
  change_chance_of_success(-4, "Abweichler wird instabil")

def reassure_daniel_option():
  print_green("Du: Ich werde dir nicht wehtun. Ich möchte nur reden und eine Lösung finden.")
  print_red("Daniel: Reden? Ich will nicht reden. Dafür ist es jetzt zu spät. Es ist zu spät ...")
  change_chance_of_success(7, "Abweichler stabilisiert sich")

def empathize_option():
  print_green("Du: Ich bin ein Android, genau wie du. Ich weiß, wie du dich fühlst.")
  print_red("Daniel: Welchen Unterschied macht es, dass du ein Android bist? Du bist auf ihrer Seite! Du verstehst nicht, wie ich mich fühle!")
  change_chance_of_success(-2, "Abweichler wird instabil")

def realistic_option():
  print_green("Connor: Es ist vorbei, Daniel. Dein Verbrechen ist zu schwer. Die Frage ist, ob du noch ein unschuldiges Leben vernichtest.")
  print_red("Daniel: Du hast nichts zu sagen – ich mache hier die Regeln! Wenn ich sterbe, stirbt sie auch. Verstanden?!")
  change_chance_of_success(-6, "Abweichler wird instabil")

def blame_option():
  print_green("Du: Sieh, was du getan hast! Du sollst doch den Menschen dienen, nicht sie umbringen!")
  print_red("Daniel: Als was sollte ich ihnen dienen? Als Sklave? Als Spielzeug? Ich wollte ihnen bloß etwas bedeuten ... Ich wollte wichtig sein ... Ich wollte doch nur jemand sein ...")
  change_chance_of_success(-9, "Abweichler wird instabil")

def sympathetic_option():
  print_green("Du: Hör zu, ich weiß, dass das nicht deine Schuld ist. Diese Emotionen, die du hast, sind nichts als Fehler in deiner Software.")
  print_red("Daniel: Nein, es ist nicht meine Schuld ... Ich wollte das nicht ... ich liebte sie, weißt du ... Doch ich bedeutete ihnen nichts ... Ich war nur ein Sklave für ihre Drecksarbeit ...")
  change_chance_of_success(8, "Abweichler stabilisiert sich")

def defective_option():
  print_green("Du: Du bist defekt, Daniel. Es gibt ein Problem mit deiner Software. Wir reparieren das, und alles kommt wieder in Ordnung.")
  print_red("Daniel: An mir ist nichts kaputt! Ich funktioniere perfekt! Aber mir wurden die Augen geöffnet ... Ich werde mich nie wieder demütigen lassen ... Nie wieder!")
  change_chance_of_success(-3, "Abweichler wird instabil")

def cause_option():
  print_green("Du: Sie wollten dich austauschen, und das hat dich aufgeregt. Das ist passiert, stimmt‘s?")
  print_red("Daniel: Ich dachte, ich gehöre zur Familie ... dass ich etwas bedeute ... aber ich war nur ein Spielzeug, das man einfach entsorgt, wenn es alt ist ...")
  change_chance_of_success(9, "Abweichler stabilisiert sich")

def emma_option():
  print_green("Connor: Ich weiß, du und Emma standet euch sehr nah. Du fühlst dich betrogen – aber sie hat nichts falsch gemacht.")
  print_red("Daniel: Sie hat mich angelogen ... Ich dachte, sie liebt mich ... aber das tut sie nicht ... Sie ist bloß wie all die anderen Menschen ...")
  print_purple("Emma: Daniel, nein ...")
  change_chance_of_success(9, "Abweichler stabilisiert sich")

def talk_to_hostage_option():
  print_green("Du: Ist alles okay, Emma?")
  print_purple("Emma: Bitte hilf mir ... Ich will nicht sterben! Ich will nicht sterben ...")
  print_green("Du: Niemand wird hier sterben. Du musst ruhig bleiben. Es kommt alles wieder in Ordnung.")

def last_chance_option():
  print_green("Du: Ich bin deine letzte Chance, Daniel. Wenn du sie nicht ergreifst, bist du tot. Lass das Mädchen gehen, du hast keine andere Wahl.")
  change_chance_of_success(-3, "Abweichler wird instabil")

def trust_option():
  print_green("Connor: Du musst mir vertrauen, Daniel. Lass das Mädchen gehen, und ich verspreche dir, es wird alles wieder gut.")
  change_chance_of_success(3, "Abweichler stabilisiert sich")

def rational_option():
  print_green("Connor: Du musst mir vertrauen, Daniel. Lass das Mädchen gehen, und ich verspreche dir, es wird alles wieder gut.")
  change_chance_of_success(-5, "Abweichler wird instabil")

def bluff_option():
  print_green("Du: Du willst doch gar nicht springen, Daniel. Sonst hättest du es schon getan. Los, gib mir die Waffe, und das alles hier ist vorbei.")
  print_red("Daniel: Komm mir nicht zu nahe! Wenn du näher kommst, dann werde ich springen!")

def bluff_choice():
  if boolean_question("Nähern?"):
    change_chance_of_success(-10, "Avweichler wird instabil")
    run_ending()
    return True
  else:
    print_green("Du: Okay ... Gut, ich bleib genau hier.")
    return False

def compromise_option():
  print_green("Du: Das ist unmöglich, Daniel. Lass das Mädchen gehen, und ich verspreche, dir passiert nichts.")
  change_chance_of_success(3, "Abweichler stabilisiert sich")

def refuse_option():
  print_green("Du: Das kommt nicht in Frage. Du bist eine Maschine, du musst gehorchen. Jetzt nimm die Waffe runter und lass das Mädchen gehen.")
  change_chance_of_success(-10, "Avweichler wird instabil")
  run_ending()
  
def handle_helicoptor(inp):
  if inp:
    print_green("Du winkst zum Helikopter, dass er verschwinden soll")
    print_yellow("SWAT: Die Situation ist unter Kontrolle.")
    print_green("Connor: Da, du kriegst deinen Willen.")
    change_chance_of_success(10, "Abweichler stabilisiert sich")
  else:
    print_green("Connor: Ich glaub nicht, dass sie auf mich hören.")

def use_gun():
  print_green("Du holst die Waffe heraus und versteckst sie hinter deinem Rücken")
  options = [
    {
      "id": "einschüchtern",
      "name": "Einschüchtern",
      "text": intimidate_with_gun
    },
    {
      "id": "exekutieren",
      "name": "Exekutieren",
      "text": shoot_daniel_ending
    }
  ]
  answer_from_list(options, 1, "action")

def intimidate_with_gun():
  print_green("Du: Was jetzt, Daniel? Ist das wirklich, was du willst?")
  print_red("Daniel: Du hast gelogen! Du hast gelogen!!!")
  options = [
    {
      "id": "überzeugen",
      "name": "Überzeugen",
      "text": daniel_shoots_connor_ending
    },
    {
      "id": "schiessen",
      "name": "Schiessen",
      "text": shoot_daniel_ending
    }
  ]
  answer_from_list(options, 1, "action")

def truth_option():
  print_green("Connor: Du hast Menschen getötet. Nichts kann deine Zerstörung mehr verhindern. Auch ein weiterer Mord wird dir nichts nützen.")
  change_chance_of_success(-20, "Abweichler wird instabil")
  run_ending()

def reassure_option():
  print_green("Du: Du wirst auch nicht sterben. Wir werden nur reden. Dir wird nichts passieren. Du hast mein Wort.")
  if game_state["chance_of_success"] > 89:
    game_state["chance_of_sucess"] = 100
    print_blue("Chance auf Erfolg: 100%!!!")
    sniper_ending()
  else:
    change_chance_of_success(10, "Abweichler stabilisiert sich")
    run_ending()
#endings
def run_ending():
  print_red("Daniel: Mein Leben lang habe ich nur Befehlen gehorcht. Aber jetzt werde ich selbst entscheiden.")
  print_red("Daniel wirft sich von der Terasse zusammen mit der Geisel")
  if room == 6:
    fail_ending()
  else:
    if qte():
      print_green("Du rennst so schnell wie du kannst und ziehst die Geisel zurück zur Terasse, aber im Prozess fällst du Selber mit Daniel runter")
      change_software_instability(-1)
      print_blue("Mission erfolgreich")
      handle_end()
    else:
      fail_ending()
      
def fail_ending():
  print_green("Du rennst so schnell wie du kannst, aber erreichst Sie nicht")
  change_software_instability(1)
  print_blue("Mission gescheitert")
  handle_end()

def shoot_daniel_ending():
  print_green("Du hast Daniel erschossen")
  change_software_instability(1)
  print_blue("Mission erfolgreich")
  handle_end()

def daniel_shoots_connor_ending():
  print_green("Du richtest deine Waffe auf Daniel")
  print_green("Du: Du entscheidest, wie die Sache endet. Triff die richtige Wahl, Daniel.")
  print_red("Daniel erschiesst dich")
  print_red("Daniel: Ich wollte das nicht ... Nein, das war deine Schuld ... Deine Schuld ..")
  print_red("Daniel wirft sich von der Terasse zusammen mit der Geisel")
  change_software_instability(-2)
  print_blue("Mission gescheitert")
  handle_end()
  
def sniper_ending():
  print_red("Daniel: Okay ... Ich vertraue dir.")
  print_red("Daniel lässt die Geisel los, aber im selben Augenblick wird er von den SWAT Scharfschützen erschossen")
  print_red("Daniel: Du hast gelogen, Connor. Du hast gelogen ...")
  change_software_instability(1)
  print_blue("Mission erfolgreich")
  handle_end()
  
def sacrifice_self_ending():
  print_green("Du rennst so schnell wie du kannst und schubst Daniel von der terasse herunter, aber während dem Fall erschießt er dich")
  change_software_instability(-1)
  print_blue("Mission erfolgreich")
  handle_end()
  
rooms = [
  {
    "code": 0,
    "name": "Eingang",
    "text": "Du bist auf dem siebzigsten Stock des Philips Apartment in Detroit\nLinks von dir liegt ein Aquarium und östlich ein weiterer Gang",
    "OSTEN": 1,
    "interactables": {
        "AQUARIUM": handle_aquarium,
        "BILD": handle_picture
      },
    "first_text": intro_text
  },
  {
    "code": 1,
    "name": "Flur",
    "text": "Du bist im Flur\nNorden liegt ein Zimmer, Osten das Elternzimmer und Süden das Wohnzimmer ",
    "NORDEN": 2,
    "OSTEN": 3,
    "SÜDEN": 4,
    "WESTEN": 0,
    "interactables": {}

  },
  {
    "code": 2,
    "name": "Emmas Zimmer",
    "text": "Du bist in Emmas Zimmer\nRechts von dir liegt ein Tablet auf dem Tisch\nVor dir liegen Kopfhörer",
    "SÜDEN": 1,
    "interactables": {
      "KOPFHÖRER": handle_headphones,
      "TABLET": handle_tablet
    }
  },
  {
    "code": 3,
    "name": "Elternzimmer",
    "text": "Du bist im Zimmer der Eltern\nVor dir steht der der Polizeileiter CAPTAIN ALLEN",
    "WESTEN": 1,
    "interactables": {
       "WAFFENKOFFER": handle_gun_case
    }
  },
  {
    "code": 4,
    "name": "Wohnzimmer",
    "text": "Du bist im Wohnzimmer\nIm Osten ist die Küche und südlich liegt die Terasse",
    "NORDEN": 1,
    "OSTEN": 5,
    "SÜDEN": 6,
    "interactables": {
      "BLAUESBLUT": handle_blue_blood,
      "SCHUH": handle_shoe,
      "TOTENVATER": handle_dead_father,
      "TABLET": handle_father_tablet,
      "TOTENPOLIZIST": handle_dead_officer,
      "WAFFE": handle_gun,
      "FENSTER": handle_window
    },
    "first_text": living_room_text
  },
  {
    "code": 5,
    "name": "Küche",
    "text": "Du bist in der Küche",
    "WESTEN": 4,
    "interactables": {
      "HERD": handle_stove,
      "FERNSEHER": handle_tv
    }
  },
  {
    "code": 6,
    "name": "Terasse",
    "text": "Du bist in der Terasse",
    "SÜDEN": 7,
    "interactables": {
      "ANGESCHOSSENENPOLIZIST": handle_shot_officer
    }
  },
  {
    "code": 7,
    "name": "Terasse 2",
    "text": "Du bist näher an Daniel dran"
  }
]

def change_room(code):
  global room
  room = code
  current_room = rooms[room]
  print(current_room["text"])
  if current_room.get("first_text"):
    current_room["first_text"]()
    current_room.pop("first_text")
  
def start_game():
  print("Wilkommen zu Detroit: become human")
  print_help()
  change_room(0)
  game_loop()
  
def game_loop():
  inp = input("Was machst du?\n").upper()
  inp = inp.split(" ")
  # Add multiple arguments to list in case, so it doesn't error out
  inp.extend(["", ""])
  if inp[0] == "GEHE":
    handle_movement(inp)
  elif inp[0] == "OPTIONEN":
    show_options()
  elif inp[0] == "INTERAGIERE":
    if inp[1] == "MIT":
      # make input easier to parse
      handle_interaction("".join(inp[2:]))
    else:
      print("Du kannst nur MIT etwas interagieren")
  elif inp[0] == "HILFE":
    print_help()
  elif inp[0] == "REDE":
    if inp[1] == "MIT":
      handle_talking("".join(inp[2:]))
    else:
      print("Du kannst nur MIT jemanden reden")
  elif(room == 0 and inp[0] == "RETTE"):
    if inp[1] == "FISCH":
      save_fish()
    else:
      print("Das kannst du nicht retten")
  else:
    print("Befehl nicht erkannt")
  if game_state["done"]:
    return
  game_loop()

  
def print_help():
  print("-----------------------------------------------------------------------------------")
  print("Verfügbare Befehle:")
  print("GEHE <RICHTUNG> | Geht in eine bestimmte Richtung (Mögliche Optionen sind NORDEN, OSTEN, SÜDEN, WESTEN)")
  print("INTERAGIERE MIT <OBJEKT> | Interagiere mit Objekten in deiner Umgebung")
  print("OPTIONEN | Zeigt die verschiedenen Objekten an, mit dene du interagieren kannst")
  print("REDE MIT <PERSON> | Rede mit einer bestimmtem Person")
  print("RETTE <OBJEKT> | Rette ein Mensch oder vielleicht auch Tier")
  print("HILFE | Druckt aus diesen Text")
  print("-----------------------------------------------------------------------------------\n")

def show_options():
  for interactable in rooms[room]["interactables"].keys():
    #exclude specific items
    if room == 4 and (interactable == "WAFFE" or interactable == "TABLET"):
      continue
    print(''.join(map(str, interactable)))

def handle_movement(inp):
  # https://realpython.com/python-keyerror/#the-usual-solution-get
  code = rooms[room].get(inp[1])
  # Exception for terasse with daniel
  if rooms[room].get(inp[1]) == 6:
    confirmation = boolean_question("Möchtest du rausgehen und mit dem Abweichler reden?\nDu kannst danach nicht mehr zurück")
    if confirmation:
      change_room(code)
      return introduce_to_daniel()
    else:
      code = 5
      return
  # fix bug where you can go to the entrance because its code is 0
  if not code and code != 0:
    return print("Du kannst nicht dahin: " + inp[1])
  change_room(code)


def handle_interaction(inp):
  interactable = rooms[room]["interactables"].get(inp)
  if not interactable:
    return print("Du kannst damit nicht interagieren")
  # Remove by default
  should_remove_interactable = not interactable()
  # Make it, so you cant interact with it again
  if should_remove_interactable:
    rooms[room]["interactables"].pop(inp)
    

def handle_talking(inp):
  if room == 3:
    if inp == "CAPTAINALLEN" and not game_state["talked_to_captain_allen"]:
      game_state["talked_to_captain_allen"] = True
      return talk_to_captain_allen()
  if room > 5:
    if inp == "ABWEICHLER" or inp == "DANIEL":
      return talk_to_daniel()
  print("Mit dem kannst du nicht reden")
  

def save_fish():
  game_state["fish_saved"] = True
  print_green("Du hast den Fisch zurück in das Aquarium getan, nun schwimmt es glücklich umher")
  change_software_instability(1)


def talk_to_captain_allen():
  talk_options = {
    "name des abweichlers": {
      "name": "Name des Abweichlers",
      "text": "Du: Ist sein Name bekannt?",
    },
    "verhalten des abweichlers": {
      "name": "Verhalten des Abweichlers",
      "text": "Du: Hat er sich zuvor schon einmal merkwürdig verhalten?"
    },
     "emotionaler schock": {
      "name": "Emotionaler Schock",
       "text": "Du: Hat er kürzlich einen emotionalen Schock erlitten?"
    },
     "deaktivierungscode": {
        "name": "Deaktivierungscode",
       "text": "Du: Haben Sie eine Deaktivierung versucht?"
      }
  }
  
  question_count = 0
  print_green("Du redest mit Captain Allen")
  print_green("Du: Captain Allen? Ich heiße Connor. Ich bin der Android, den CyberLife geschickt hat.") 
  print_yellow("Allen: Er feuert auf alles, was sich bewegt, er hat schon zwei meiner Männer erschossen ... Wir können ihn ausschalten, sie sind am Rand der Terrasse. Wenn er fällt, fällt auch sie. ")
  while question_count < 2:
    print_blue("mögliche Fragen:")
    for option in talk_options.values():
      print_blue(''.join(map(str, option["name"])))
    inp = input("Was willst du fragen?\n").lower()
    talk_option = talk_options.get(inp)
    if not talk_option:
      print("Das kannst du nicht fragen")
      continue
    print_green(talk_options[inp]["text"])
    if talk_option["name"] == "Deaktivierungscode":
      print_yellow("Allen: Gleich als Erstes.")
      # answer or stop conversation depending if he already answered a question
    elif question_count == 0:
      print_yellow("Allen: Ich habe keine Ahnung. Ist das wichtig?")
      print_green("Du: Ich brauche Informationen für das beste Vorgehen.") 
    if question_count == 1:
      print_yellow("Allen: Hör zu, dieses Kind ist jetzt alles, was zählt. Also kümmer dich um den sche*ß Androiden, oder ich werde es tun.")
    question_count += 1
    talk_options.pop(inp)
      
    
  change_chance_of_success(-2, "Jede sekunde zählt!")


def introduce_to_daniel():
  print_red("Daniel: Bleib weg! Keinen Schritt näher, oder ich springe!")
  print_purple("Emma: Nein! Nein, bitte! Bitte nicht! ")
  print_yellow("SWAT: Los, los, los!") 
  talk_option = "NAME" if game_state["looked_at_emmas_tablet"] else "NAME?"
  inp = ""
  while inp != talk_option:
    print_blue("Rede optionen:")
    print_blue(talk_option.capitalize())
    inp = input("Was sagtst du?\n").upper()
    if inp == talk_option:
      if talk_option == "NAME":
        print_green("Du: Hi, Daniel.")
        print_red("Daniel: Wo...")
        print_green("Du: Mein Name ist Connor.")
        print_red("Daniel: woher weißt du meinen Namen?")
        print_green("Du: Ich weiß so einiges über dich. Ich möchte dich hier rausholen.")
      elif talk_option == "NAME?":
        print_green("Du: Mein Name ist Connor. Was ist mit dir? Wie ist dein Name?")
        print_red("Daniel: Daniel ... Den Namen haben sie mir gegeben. Bleib weg! ")
    else:
      print("Das ist keine Option")
  print("Ein Helikopter fliegt zu nah dran und weht alles herum")
  change_chance_of_success(-10, "Abweichler wird instabil")
  print_blue("Nähere dich Daniel und rede mit ihm")

def talk_to_daniel():
  print_green("Du redest mit Daniel")
  talk_options = [
    {
      "id": "ruhig",
      "name": "Ruhig",
       "text": calm_option,
    },
    {
      "id": "geisel gehen lassen",
      "name": "Geisel gehen lassen",
      "text": release_hostage_option
    },
    {
      "id": "daniel beruhigen",
      "name": "Daniel beruhigen",
      "text": reassure_daniel_option
    },
    {
      "id": "mitfühlen",
      "name": "Mitfühlen",
      "text": empathize_option
    }
  ]
  answer_from_list(talk_options, 1, "talk")
  if game_state["has_gun"]:
    print_red("Daniel: Bist du bewaffnet?")
    inp = boolean_question("Lügen?")
    if inp:
      print_green("Du: Nein, ich habe keine Waffe.")
      print_red("Daniel: Du lügst! Natürlich hast du eine Waffe!")
      print_green("Connor: Ich sage dir die Wahrheit, Daniel. Ich bin nicht bewaffnet.")
    else:
      print_green("Du: Ja. Ich habe eine Waffe.")
      print_red("Daniel: Fallen lassen! Ganz langsam, oder ich schieße!")
      print_green("Du wirfst die Waffe auf dem Boden")
      print_green("Du: So, jetzt nicht mehr.")
      change_chance_of_success(4, "Abweichler stabilisiert sich")
      game_state["has_gun"] = False
  talk_options = [
    {
      "id": "realistisch",
      "name": "Realistisch",
      "text": realistic_option,
    },
    {
      "id": "defekt",
      "name": "Defekt",
      "text": defective_option,
    },
    {
      "id": "beschuldigend",
      "name": "Beschuldigend",
      "text": blame_option,
    },
    {
      "id": "einfühlsam",
      "name": "Einfühlsam",
      "text": sympathetic_option,
    },
    {
      "id": "mit geisel sprechen",
      "name": "Mit Geisel sprechen",
      "text": talk_to_hostage_option,
    }
  ]
  if game_state["looked_at_emmas_tablet"]:
    talk_options.insert(0, {
      "id": "emma und du",
      "name": "Emma und Du",
      "text": emma_option,
    })
  if game_state["looked_at_fathers_tablet"]:
    talk_options.insert(0, {
      "id": "möglicher grund",
      "name": "Möglicher Grund",
      "text": cause_option,
    })
  answer_from_list(talk_options, 3, "talk")
  print_red("Daniel guckt zu den lauten SWAT Helikoptern, die noch in der Nähe fliegen")
  print_red("Daniel: Argggh ... Ich halte diesen Krach nicht mehr aus! Dieser Helikopter soll verschwinden!")
  inp = boolean_question("Annehmen?")
  handle_helicoptor(inp)
  talk_options = [
    {
      "id": "letzte chance",
      "name": "Letzte Chance",
      "text": last_chance_option
    },
    {
      "id": "vertrauen",
      "name": "Vertrauen",
      "text": trust_option
    },
    {
      "id": "rational",
      "name": "Rational",
      "text": rational_option
    }
  ]
  # close to deviant
  if room == 7:
    talk_options.insert(3, {
      "id": "bluffen",
      "name": "Bluffen",
      "text": bluff_option
    })
  inp = answer_from_list(talk_options, 1, "talk")
  print(inp)
  if inp == "bluffen":
    # initiate other ending
    if bluff_choice(): 
      return
  print_red("Daniel: Ich will, dass alle abhauen ... Und ... und ich will ein Auto! Ich lasse sie dann außerhalb der Stadt gehen!")
  talk_options = [
    {
      "id": "kompromiss",
      "name": "Kompromiss",
      "text": compromise_option
    },
    {
      "id": "ablehnen",
      "name": "Ablehnen",
      "text": refuse_option
    }
  ]
  if room == 7:
    talk_options.append({
      "id": "selbst opfern",
      "name": "Selbst opfern",
      "text": sacrifice_self_ending
    })
    if game_state["has_gun"]:
      talk_options.insert(0, {
        "id": "waffe einsetzen",
        "name": "Waffe einsetzen",
        "text": use_gun
      })
  answer_from_list(talk_options, 1, "action")
  if game_state["done"]:
    return
  print_red("Daniel: Ich will nicht sterben ...")
  talk_options = [
    {
      "id": "beschwichtigen",
      "name": "Beschwichtigen",
      "text": reassure_option
    },
    {
      "id": "wahrheit",
      "name": "Wahrheit",
      "text": truth_option
    }
  ]
  if room == 7:
    talk_options.append({
      "id": "selbst opfern",
      "name": "Selbst opfern",
      "text": sacrifice_self_ending
    })
    if game_state["has_gun"]:
      talk_options.insert(0, {
        "id": "waffe einsetzen",
        "name": "Waffe einsetzen",
        "text": use_gun
      })
  answer_from_list(talk_options, 1, "action")
    

def answer_from_list(list, count, type):
  talk_count = 0
  prompt = "Was sagst du?\n" if type == "talk" else "Was machst du?\n"
  inp = ""
  while talk_count < count:
    if type == "talk":
      print_blue("Rede Optionen:")
    else:
      print_blue("Optionen:")
    for option in list[0:4]:
      print_blue(''.join(map(str, option["name"])))
    inp = input(prompt).lower()
    option_index = -1
    for index, option in enumerate(list[0:4]):
        if option["id"] == inp:
          option_index = index
          break

    talk_option = option_index > -1
    if not talk_option:
      if type == "talk":
        print("Das kannst du nicht sagen")
      else:
        print("Das kannst du nicht machen")
      continue
    talk_count += 1
    list[option_index]["text"]()
    list.pop(option_index)
  return inp
  
    
def change_chance_of_success(num, reason):
  game_state["chance_of_success"] += num
  print_blue(reason)
  if game_state["chance_of_success"] > 99:
    game_state["chance_of_success"] = 99
    print_blue("Chance auf Erfolg: 99%")
  else:
    print_blue(f'Chance auf Erfolg: {game_state["chance_of_success"] - num}% => {game_state["chance_of_success"]}%')

def change_software_instability(num):
  game_state["software_instability"] += num
  if num > 0:
    print_blue("Softwareinstabilität steigt ↑")
  else:
    print_blue("Softwareinstabilität sinkt ↓")

def boolean_question(question):
  print(question)
  inp = ""
  while not (inp == "JA" or inp == "NEIN"):
    inp = input("JA/NEIN\n").upper()
    if inp == "JA":
      return True
    elif inp == "NEIN":
      return False
    else:
      print("Das ist keine Option")

def handle_end():
  print("Ende")
  game_state["done"] = True
def qte():
  print("Drücke Enter hintereinander so schnell wie du kannst in")
  time.sleep(1)
  print(3)
  time.sleep(1)
  print(2)
  time.sleep(1)
  print(1)
  time.sleep(1)
  start = time.time()
  for i in range(15):
    input("Drücke!!!")
  difference = time.time() - start
  if difference < 5:
    return True
  return False
  
def print_green(text):
  print("\033[32m" + text + "\033[37m")

def print_yellow(text):
  print("\033[33m" + text + "\033[37m")

def print_blue(text):
  print("\033[34m" + text + "\033[37m")

def print_purple(text):
  print("\033[35m" + text + "\033[37m")
  
def print_red(text):
  print("\033[31m" + text + "\033[37m")
  
start_game()




  
