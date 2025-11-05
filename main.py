#Från lektion 1
########################################################################
# Block 1 - Aritmetik
########################################################################
#1
#msg = "Welcome, warrior!"
#print(msg)

#2
#HP = 100
#print(HP)

#3
#goldcoins = 50
#chest = 125
#total = goldcoins + chest
#print(total)

#4
#Spaceship = 500
#Laser = 120
#Energy = Spaceship - Laser
#print(Energy)

#5
#potion = 4
#price = 30
#print(potion * price)

#6
#treasure = 150.0
#print(treasure / 2)

#7
#beans = 25.0
#wizard = 7
#beans_per_wizard = antal_beans // wizard
#print(beans // wizard)

#8
#beans = 25
#wizards = 7
#sum = 25 % 7
#print(sum)

#9


#10
#monster_1_gold = 10
#monster_2_gold = 5
#antal_monster_2 = 2
#print(monster_1_gold + monster_2_gold * antal_monster_2)

#11
#team1 = 10
#team2 = 2
#points_Each = 5
#print(team1 + team2 + points_Each)

#12
#Packing = "fackla---Rep---Svärd"
#gear = Packing.split("---")
#print(gear)

#13
#String1 = ("Analyserar data...")
#String2 = ("Klar!")
#print(String1 + String2)

#14
#mana = 80.5
#print(mana)

#15
#mana = 80.5
#Spell = 15.5
#sum = mana - Spell
#print(sum)

#16
#del1 = "Cyber"
#del2 = "Punk"
#print(del1 + del2)

#17
#varningsljud = "Pip!"
#print(varningsljud * 5)

#18
#marines = 160
#capsules = 7
#Full_Capsules = marines / capsules
#print("Amount of full capsules: " + str(Full_Capsules))
#Amount_Soldiers_Left = marines % capsules
#print("Amount of soldiers who have to sleep outside: " + str(Amount_Soldiers_Left))

#19
#Spaceship_Cost = 5000.0
#Increase = 1.1
#New_Price = 5000.0 * 1.1
#print("New price is: " + str(New_Price))

#20
#Level = 5
#HP = 100
#print("My level is: " + str(Level) +" and I have " + str(HP) + " hp")

########################################################################
# Block 2 - Datatyper och Strängar
########################################################################
#1
#agent_namn = input("What is your Agentname?")
#print(f"Hello agent {agent_namn} !")

#2
#homeplanet = input("What is your homeplanet?")
#print(f"Nice! {homeplanet} is a beautiful place!")

#3
#recept = "Pannkakor"
#print(recept[:1])

#4
#recept = "Pannkakor"
#print(recept[8:9])

#5
#Codeword = "DevOpsIsFun"
#print(Codeword[:6]) #Printar ut första 6 bokstäverna

#6
#Codeword = "DevOpsIsFun"
#print(Codeword[8:])

#7
#Text = "abcRECEPTxyz"
#print(Text[3:-3])

#8
#Codeword = "DevOpsIsFun"
#print(Codeword[::-1]) #"-1" skriver ut strängen baklänges

#9
#password = input("Write a secret password: ")
#number_of_letters = len(password)
#print(f"Password has {number_of_letters} letters in it")

#10
#name = "grogu"
#print(f"{name.upper()}") #Funktionen skriver ut namnet med stora bokstäver

#11
#question = input("ATTACK OR RUN?! ")
#print(f"{question.title()}") #skriver ut svaret i små bokstäver

#12
#Book_title = "sagan om ringen"
#print(f"{Book_title.title()}")

#13
#Username = "*_anna_"
#print(Username.strip("*_"))

#14
#fel = "Jag gillar Jovo"
#new = fel.replace("Jovo", "Java")
#print(new)

#15
#List = "Mjölk,bröd,ägg"
#print(List.split(","))

#16
#Text = "Var i galaxen är Xur?"
#print(Text[17:20])

#17
#Fruit = "banana"
#antal = Fruit.count("a")
#print(antal)

#18
#File = "bild.jpg"#
#print(File.startswith("bild"))#

#19
#File = "bld.jpg"
#print(File.endswith(".jpg"))

#20
#Meaning = "lösenorde är: banan"
#print(Meaning.__contains__("lösenord"))

########################################################################
# Block 3 - Villkorssatser
#if, elif, else och typkonvertering
########################################################################
#1
#bananas_str = input("Hur många bananer har du? ")
#antal = int(bananas_str)
#print(antal)

#2
#Price = input("Vad är priset på en Potion? (t.ex. 19.5): ")
#Potion = float(Price)
#print("En Potion kostar " + Price + " kr")

#3
#age = input("What is your age?: ")
#age = int(age)
#if age > 18:
#    print("Tillträde beviljas")
#elif age < 18:
#    print("Fel svar, gå hem")

#4
#Magic_Word = input("Vad är det magiska ordet? ")
#if Magic_Word == "DevOps":
#    print("Porten öppnas!")

#5
#temp = input("Vad är temperaturen ute idag? ")
#temp = int(temp)
#if temp > 25:
#    print("Det är sommarvarmt!")
#elif temp > 15:
#    print("Det är lagom svenskt väder.")
#elif temp < 15:
#    print("Det är kallt, ta på jackan!")

#6
#Choice = input("Svara ja eller nej: ")
#Choice = str(Choice)
#if Choice == "ja":
#    print("Du valde att fortsätta äventyret!")
#elif Choice == "nej":
#    print("Tråkmåns!")

#7
#Player = input("Vad är din status? 'redo' eller 'upptagen'? ")
#if Player == "redo":
#    print("GLHF")
#else:
#     print("Vänta... Spelaren är inte redo")

#8
#gold = input("Hur många guldmynt har du? ")
#gold = int(gold)
#if gold < 50:
#    print("Du har inte råd med det här svärdet")

#9
#level = input("Vad är din level? ")
#level = int(level)
#if level > 10:
#    print("Du kan lära dig formeln 'Fireball'!")

#10
#age = int(input("Vad är din ålder? "))
#ticket = input("Har du biljett? (ja/nej): ").strip().lower()
#if age > 17 and ticket == "ja":
#    print("Välkommen in på konserten!")
#else:
#    print("Du får inte komma in")

#11
#goldkey = input("Har du en guldnyckel? ")
#dyrk = input("Har du en dyrk? ")
#if goldkey == "ja" or dyrk == "ja":
#    print("Du lyckas öppna kistan!")

#12
#är_förbannad = True
#if not är_förbannad:
#    print("Dina attacker gör normal skada")
#else:
#    print("Dina attacker är svagare!")

#13
#name = input("vad är ditt namn? ")
#print("Hej, " + name + "!")

#14
#name = input("Vad är ditt namn? ")
#if name == "":
#    print("Du måste sange ett namn för att spara spelet!")

#15
#game_over = input("Hur många liv har du? ")
#if game_over == 0:
#    print("Game Over")
#else:
#    print("Keep on truckin'!")

#16
#forbidden = ("kniv bomb").split(" ")
#security = input("Vad har du i väskan? ")
#if any(word in security for word in forbidden):
#    print("Säkerhetskontroll! Du stoppas!")
#else:
#    print("Nemas problemas")

#17
#postal = input("Vad är ditt postnummer? ")
#if postal.isdigit:
#    print("Giltigt format")

#18
#name = input("Vad är ditt namn? ")
#if name.isalpha():
#    print("Giltigt format")
#else:
#    print("Ett namn får inte innehålla siffror eller tecken.")

#19
#password = input("Skriv in ett lösenord: ")
#if len(password) < 8:
#    print("Lösenordet är för kort! Minst 8 tecken krävs!")

#20
#action = input("Vad väljer du? (attack/försvar/magi) ")
#if action == "attack":
#    print("Du svingar ditt svärd!")
#elif action == "försvar":
#    print("Du höjer din sköld!")
#elif action == "magi":
#    print("Du kastar en formel!")
#else:
#    print("Ogiltigt val")

########################################################################
# Block 4
# for, while, range & break
########################################################################

#1
#for i in range(5):
#    print("Abracadabra!")

#2
#for i in range(5):
#    print("Startar nivå",(i+1))

#3
#code = "LÅST"
#for i in code:
#    print(i)

#4
#for i in range(10, 0, -1):
#    print("bränslenivå",(i))

#5
#height =  0
#
#while height < 5:
#    print(f"Höjd: {height}")
#    height += 1

#6
#while True:
#    password = input("Vad är lösenordet? ")
#    if password == "exit":
#        break
#    else:
#        print("Försök igen")

#7
#engine = range(10+1)
#rpm = [x for x in engine if x % 2 == 0]
#print(rpm)

#8
#for i in range(1, 11):
#    if i % 3 == 0:
#        print(i)

#9
#magic = 20
#spell = 5
#while True:
#    magoo = input("Kasta formel? ja/nej: ").strip()
#    if magoo.strip().lower() == "ja":
#        magic -= spell
#        print(f"Du har {magic} kvar.")
#    elif magoo.strip().lower() == "nej":
#        print("Avslutar.")
#        break
#    else:
#        print("Svara ja eller nej.")

#10
#cheer = int(input("Hur många gånger ska jag heja? "))
#for _ in range(cheer):
#    print("Heja!")

#11
#while True:
#    password = input("Skriv ett säkert lösenord: ")
#    if len(password) < 6:
#        print("För kort lösenord, försök igen. ")
#    else:
#        print("Säkert lösenord.")
#        break

#12
#schema = "måndag tisdag onsdag"
#dagar = schema.split(" ")
#for dag in dagar:
#    print(dag)

#13
#for i in range(5, 0, -1):
#    print(i, end = " ")

#14
#while True:
#    game = input("Är du redo att starta spelet? ")
#    if game.__contains__ ("ja"):
#        break

#15
#while True:
#    user_input = input("Skriv ett ord: ")
#    if user_input.__contains__ ("a"):
#        print("Hittade ett 'a'!")
#        break
#    else:
#        print("Prova ett nytt ord")

#16
