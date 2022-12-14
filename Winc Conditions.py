#!/usr/bin/env python
# coding: utf-8

# In[5]:


def eligible_to_vote(age, nationality):
    return True


# In[7]:


eligible_to_vote


# In[39]:


def eligible_to_vote(age, nationality):
    if age >= 18:
        return True
    else:
        return False


# In[ ]:





# In[14]:


def eligible_to_vote(age, nationality):
    if age >= 18:
        if nationality == 'Italian':
            return True
        else:
            return False
    else:
        return False


# In[18]:


def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    else:
        return False


# In[19]:


def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    return False


# In[20]:


def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    elif age >= 25 and nationality == 'Portuguese':
        return True
    else:
        return False


# In[21]:


def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        print('Bene!')
        return True
    elif age >= 25 and nationality == 'Portuguese':
        print('Sim!')
        return True
    elif age >= 31 and nationality == 'Dutch':
        print('Top!')
        return True
    elif age >= 19 and nationality == 'Malawian':
        print('Iya!')
        return True
    else:
        return False


# In[ ]:





# In[62]:


# Here are several examples of this type of if statement:

x = 0
y = 5

if x < y:                            # Truthy
    print('yes')


# In[63]:


# Note that the colon (:) following <expr> is required. Some programming languages require <expr> to be enclosed in parentheses, but Python does not.

# Here are several examples of this type of if statement:

if x:                                # Falsy
    print('yes')
if y:                                # Truthy
    print('yes')


if x or y:                           # Truthy
     print('yes')


if x and y:                          # Falsy
    print('yes')


if 'aul' in 'grault':                # Truthy
     print('yes')


if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
     print('yes')


# In[64]:


if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')


# In[65]:


# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x


# In[66]:


# Soms wilt u een voorwaarde evalueren en één pad nemen als het waar is, maar een alternatief pad specificeren 
# als dat niet het geval is. Dit wordt bereikt met een elseclausule:

if <expr>:
    <statement(s)>
else:
    <statement(s)>


# In[67]:


# In dit voorbeeld x is kleiner dan 50, dus de eerste suite (regel 4 tot 5) wordt uitgevoerd 
# en de tweede suite (regel 7 tot 8) wordt overgeslagen:

x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


# In[28]:


# Hier is daarentegen x groter dan 50, dus de eerste suite wordt overgeslagen en de tweede suite uitgevoerd:

x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')


# In[ ]:


# Er is ook een syntaxis voor het uitvoeren van vertakkingen op basis van verschillende alternatieven. 
# Gebruik hiervoor een of meer elif(afkorting van else if ) clausules. 
# Python evalueert elk <expr>op zijn beurt en voert de suite uit die overeenkomt met de eerste die waar is. 
# Als geen van de expressies waar is en een elseclausule is opgegeven, wordt de bijbehorende suite uitgevoerd:

if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>


# In[68]:


# Er kan een willekeurig aantal elifclausules worden opgegeven. De elseclausule is optioneel. 
# Als het aanwezig is, kan er maar één zijn en moet het als laatste worden opgegeven:

name = 'Joe'

if name == 'Fred':
     print('Hello Fred')
elif name == 'Xander':
     print('Hello Xander')
elif name == 'Joe':
     print('Hello Joe')
elif name == 'Arnold':
     print('Hello Arnold')
else:
     print("I don't know who you are!")


# In[69]:


# Opmerking: het gebruik van een lange if// elif- elsereeks kan een beetje onelegant zijn, 
# vooral wanneer de acties eenvoudige uitspraken zijn zoals print(). 
# In veel gevallen kan er een meer Pythonische manier zijn om hetzelfde te bereiken.

# Hier is een mogelijk alternatief voor het bovenstaande voorbeeld met behulp van de dict.get()methode:

names = {
     'Fred': 'Hello Fred',
     'Xander': 'Hello Xander',
     'Joe': 'Hello Joe',
     'Arnold': 'Hello Arnold'
 }

print(names.get('Joe', "I don't know who you are!"))
print(names.get('Rick', "I don't know who you are!"))

# Bedenk uit de zelfstudie over Python-woordenboeken dat de dict.get()methode een woordenboek 
# doorzoekt naar de opgegeven sleutel en de bijbehorende waarde retourneert als deze wordt gevonden, 
# of de opgegeven standaardwaarde als dat niet het geval is.


# In[ ]:


# Het is gebruikelijk om if <expr>op één regel te schrijven en <statement>op de volgende regel 
# als volgt in te springen:

if <expr>:
    <statement>
    
# Maar het is toegestaan om een hele if verklaring op één regel te schrijven. Het volgende is 
# functioneel equivalent aan het bovenstaande voorbeeld:

if <expr>: <statement>
    
# Er kunnen er zelfs meerdere <statement>op dezelfde regel staan, gescheiden door puntkomma's:

if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
    
# Maar wat betekent dit? Er zijn twee mogelijke interpretaties:

# Als <expr>het waar is, voer dan uit <statement_1>.

# Voer vervolgens <statement_2> ... <statement_n> onvoorwaardelijk uit, ongeacht of <expr> het waar is of niet.

# Als <expr> waar is, voer dan alle <statement_1> ... <statement_n>. Voer ze anders niet uit.

# Python neemt de laatste interpretatie. De puntkomma die de scheiding scheidt <statements>, 
# heeft een hogere prioriteit dan de dubbele punt die volgt <expr>- in computerjargon wordt gezegd dat de puntkomma 
# steviger bindt dan de dubbele punt. Ze worden dus <statements> behandeld als een suite, en ze worden ofwel 
# allemaal uitgevoerd, of geen ervan is:


# In[2]:


if 'f' in 'foo': print('1'); print('2'); print('3')


# In[33]:


if 'z' in 'foo': print('1'); print('2'); print('3')


# In[34]:


# Niks wordt geprint want 'z' zit niet in 'foo'!


# In[71]:


# Meerdere instructies kunnen ook op dezelfde regel worden opgegeven als een elif of else clausule:

x = 2
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')


# In[72]:


x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')


# In[73]:


# Hoewel dit allemaal werkt, en de tolk het toestaat, wordt het over het algemeen afgeraden omdat het 
# tot een slechte leesbaarheid leidt, met name voor complexe if uitspraken. PEP 8 raadt het specifiek af.

# Zoals gewoonlijk is het een beetje een kwestie van smaak. De meeste mensen zouden het volgende visueel 
# aantrekkelijker en op het eerste gezicht gemakkelijker te begrijpen vinden dan het bovenstaande voorbeeld:

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')


# In[74]:


# Als een if verklaring echter eenvoudig genoeg is, kan het redelijk zijn om alles op één regel te plaatsen. 
# Zoiets zou waarschijnlijk niemands nekharen te veel verhogen:

debugging = True  # Set to True to turn debugging on.


if debugging: print('About to call function foo()')


# In[ ]:


# Voorwaardelijke expressies (de ternaire operator van Python)

# Python ondersteunt een extra besluitvormingsentiteit die een voorwaardelijke expressie wordt genoemd. 
# (Het wordt ook wel een voorwaardelijke operator of ternaire operator genoemd op verschillende plaatsen 
# in de Python-documentatie.) Voorwaardelijke uitdrukkingen werden voorgesteld voor toevoeging aan de taal 
# in PEP 308 en groen licht gegeven door Guido in 2005.

# In zijn eenvoudigste vorm is de syntaxis van de voorwaardelijke expressie als volgt:

<expr1> if <conditional_expr> else <expr2>


# In[75]:


# Dit verschilt van de if hierboven vermelde instructieformulieren, omdat het geen besturingsstructuur is die 
# de stroom van programma-uitvoering stuurt. Het werkt meer als een operator die een uitdrukking definieert. 
# In het bovenstaande voorbeeld <conditional_expr> wordt eerst geëvalueerd. Als het waar is, evalueert de 
# expressie naar <expr1>. Als het onwaar is, evalueert de expressie naar <expr2>.

# Let op de niet voor de hand liggende volgorde: de middelste uitdrukking wordt eerst geëvalueerd en op basis 
# van dat resultaat wordt een van de uitdrukkingen aan de uiteinden geretourneerd. Hier zijn enkele voorbeelden 
# die hopelijk zullen helpen verduidelijken:

raining = False
print("Let's go to the", 'beach' if not raining else 'library')


# In[76]:


raining = True
print("Let's go to the", 'beach' if not raining else 'library')


# In[77]:


age = 12
s = 'minor' if age < 21 else 'adult'
s


# In[78]:


'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'


# In[ ]:


# Opmerking: de voorwaardelijke expressie van Python is vergelijkbaar met de 
# <conditional_expr> ? <expr1> : <expr2>syntaxis die door veel andere talen wordt gebruikt - C, Perl en Java 
# om er maar een paar te noemen. In feite wordt de ?:operator in die talen gewoonlijk de ternaire operator genoemd, 
# wat waarschijnlijk de reden is dat de voorwaardelijke expressie van Python soms de ternaire operator van Python 
# wordt genoemd.

# Je kunt in PEP 308 zien dat de <conditional_expr> ? <expr1> : <expr2> syntaxis werd overwogen voor Python, 
# maar uiteindelijk werd afgewezen ten gunste van de hierboven getoonde syntaxis.


# In[ ]:


# Een veelgebruikt gebruik van de voorwaardelijke uitdrukking is het selecteren van variabele toewijzing. 
# Stel dat u bijvoorbeeld het grootste van twee getallen wilt vinden. Natuurlijk is er een ingebouwde functie 
# max()die precies dit (en meer) doet die u zou kunnen gebruiken. Maar stel dat u uw eigen code helemaal opnieuw 
# wilt schrijven.

# U kunt een standaardverklaring gebruiken if met een else clausule:

if a > b:
    m = a
else:
    m = b
    
# Maar een voorwaardelijke uitdrukking is korter en waarschijnlijk ook leesbaarder:

m = a if a > b else b

# Onthoud dat de voorwaardelijke expressie zich syntactisch als een expressie gedraagt. Het kan worden gebruikt 
# als onderdeel van een langere uitdrukking. De voorwaardelijke expressie heeft een lagere prioriteit dan vrijwel 
# alle andere operatoren, dus haakjes zijn nodig om deze op zichzelf te groeperen.


# In[79]:


# In het volgende voorbeeld + bindt de operator strakker dan de voorwaardelijke expressie, dus 1 + x en y + 2 wordt 
# eerst geëvalueerd, gevolgd door de voorwaardelijke expressie. De haakjes in het tweede geval zijn niet nodig en 
# veranderen het resultaat niet:

x = y = 40

z = 1 + x if x > y else y + 2
z


# In[80]:


z = (1 + x) if x > y else (y + 2)
z


# In[81]:


# Als u wilt dat de voorwaardelijke expressie eerst wordt geëvalueerd, moet u deze omgeven met haakjes voor 
# groeperen. In het volgende voorbeeld (x if x > y else y)wordt eerst geëvalueerd. Het resultaat is y, dat is 40, 
# dus z is toegewezen 1 + 40 + 2= 43:

x = y = 40

z = 1 + (x if x > y else y) + 2
z


# In[57]:


# Als u een voorwaardelijke uitdrukking gebruikt als onderdeel van een grotere uitdrukking, is het waarschijnlijk 
# een goed idee om haakjes voor groeperen te gebruiken ter verduidelijking, zelfs als ze niet nodig zijn.


# In[58]:


# Voorwaardelijke uitdrukkingen gebruiken ook kortsluitevaluatie zoals samengestelde logische uitdrukkingen. 
# Delen van een voorwaardelijke expressie worden niet geëvalueerd als dat niet nodig is.

# In de uitdrukking <expr1> if <conditional_expr> else <expr2>:

# Als <conditional_expr> waar is, <expr1> wordt geretourneerd en <expr2> niet geëvalueerd.
# Als <conditional_expr> onwaar is, <expr2> wordt geretourneerd en <expr1> niet geëvalueerd.


# In[82]:


# Net als voorheen kunt u dit verifiëren door termen te gebruiken die een fout zouden veroorzaken:

'foo' if True else 1/0


# In[83]:


1/0 if False else 'bar'


# In[84]:


# In beide gevallen worden de 1/0 termen niet geëvalueerd, dus er wordt geen uitzondering gemaakt.


# In[86]:


# Voorwaardelijke expressies kunnen ook aan elkaar worden geketend, als een soort 
# alternatieve if/ elif/ elsestructuur, zoals hier getoond:
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux'
)
s


# In[ ]:


# Het is niet duidelijk of dit een significant voordeel heeft ten opzichte van het bijbehorende 
# if/ elif/ elsestatement, maar het is syntactisch correcte Python.


# In[ ]:


# Af en toe merk je misschien dat je een codestub wilt schrijven: een tijdelijke aanduiding voor waar je 
# uiteindelijk een codeblok gaat plaatsen dat je nog niet hebt geïmplementeerd.

# In talen waar token-scheidingstekens worden gebruikt om blokken te definiëren, zoals de accolades in Perl en C, 
# kunnen lege scheidingstekens worden gebruikt om een codestrook te definiëren. Het volgende is bijvoorbeeld 
# legitieme Perl- of C-code:

# This is not Python
if (x)
{
}

# Hier definiëren de lege accolades een leeg blok. Perl of C zullen de uitdrukking evalueren x, en dan, 
# zelfs als het waar is, stilletjes niets doen.


# In[ ]:


# Omdat Python inspringing gebruikt in plaats van scheidingstekens, is het niet mogelijk om een leeg blok op 
# te geven. Als u een if instructie invoert met if <expr>:, moet er iets achter komen, op dezelfde regel of 
# ingesprongen op de volgende regel.


# In[56]:


Beschouw dit script foo.py:

if True:

print('foo')

# Als je probeert uit te voeren foo.py, krijg je dit:


# In[57]:


# De Python- passinstructie lost dit probleem op. Het verandert helemaal niets aan het programmagedrag. 
# Het wordt gebruikt als een tijdelijke aanduiding om de tolk tevreden te houden in elke situatie waarin een 
# verklaring syntactisch vereist is, maar u eigenlijk niets wilt doen:

if True:
    pass

print('foo')


# In[1]:


# Conclusie

# Met de voltooiing van deze tutorial begin je Python-code te schrijven die verder gaat dan eenvoudige sequentiële 
# uitvoering:

# Je hebt kennis gemaakt met het concept van controlestructuren . Dit zijn samengestelde instructies die de 
# programmabesturingsstroom veranderen - de volgorde van uitvoering van programma-instructies .
# Je hebt geleerd hoe je individuele uitspraken kunt groeperen in een blok of suite .
# U bent uw eerste besturingsstructuur tegengekomen, de if instructie, die het mogelijk maakt om een instructie 
# of blok voorwaardelijk uit te voeren op basis van evaluatie van programmagegevens.
# Al deze concepten zijn cruciaal voor het ontwikkelen van complexere Python-code


# In[2]:


if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')


# In[4]:


if 10 > 20:                           #  x
        print('Inner condition 1')
        
print('Between inner conditions')


# In[5]:


if 10 < 20:                           #  x
        print('Inner condition 2') 


# In[40]:


print('End of outer condition')       #  x
print('After outer condition')  


# In[91]:


names = {
     'Fred': 'Hello Fred',
     'Xander': 'Hello Xander',
     'Joe': 'Hello Joe',
     'Arnold': 'Hello Arnold'
 }

print(names.get('Joe', "I don't know who you are!"))
print(names.get('Rick', "I don't know who you are!"))


# In[44]:


weather = {
        'rainy': 'take cows to cowshed',
        'sunny': 'take cows to cowshed\nmow grass',
        'windy': 'wait',
        'neutral': 'fertilize pasture'
    }

print(weather.get('rainy', "the cows are standing in the rain"))
print(weather.get('sunny', "The weather is sunny"))
print(weather.get('windy', "No other action"))
print(weather.get('neutral', "The weather is not sunny or windy"))


# In[46]:


time_of_day = {
            'day': 'wait',
            'night': 'take cows to cowshed',
}

print(time_of_day.get('night', "The cows are on the pasture at night"))
print(time_of_day.get('day', "No other action"))


# In[14]:




cow_milking_status = 'Need milking' if True else 'Don\'t need milking'
slurry_tank = 'Full' if True else 'Not full'
grass_status = 'Long' if True else 'Short'
    


# In[15]:


location_of_the_cows = {
                     'pasture': 'take cows to cowshed',
                     'cowshed': 'milk cows',
}

print(location_of_the_cows.get('pasture', "the cows are on the pasture at night"))
print(location_of_the_cows.get('cowshed', "the cows are in the cowshed"))


# In[16]:


season = {
        'winter': 'wait',
        'spring': 'mow grass',
        'summer': 'wait',
        'fall': 'wait',
}

print(season.get('winter', "No other action"))
print(season.get('spring', "The grass is long"))
print(season.get('summer', "No other action"))
print(season.get('fall', "No other action"))


# In[9]:


weather = {
        'rainy': 'take cows to cowshed',
        'sunny': 'take cows to cowshed\nmow grass',
        'windy': 'wait',
        'neutral': 'fertilize pasture'
    }


time_of_day = {
            'day': 'wait',
            'night': 'take cows to cowshed',
}


location_of_the_cows = {
                     'pasture': 'take cows to cowshed',
                     'cowshed': 'milk cows',
}

cow_milking_status = 'Need milking' if True else 'Don\'t need milking'

season = {
        'winter': 'wait',
        'spring': 'mow grass',
        'summer': 'wait',
        'fall': 'wait',
}

slurry_tank = 'Full' if True else 'Not full'
grass_status = 'Long' if True else 'Short'





def farm_action(weather, time_of_day, cow_milking_status, location_of_the_cows, season, slurry_tank, grass_status):
    if weather == "rainy" and time_of_day == "night" and location_of_the_cows == "pasture":
        print("take cows to cowshed")
    elif time_of_day == "day" and cow_milking_status == "Need milking" or location_of_the_cows == "pasture":
        print("take cows to cowshed\nmilk cows\ntake cows back to pasture")
    elif weather == "neutral" or location_of_the_cows == 'cowshed' and slurry_tank == "Full":
        print("fertilize pasture")
    elif weather == "sunny" or location_of_the_cows == 'cowshed' or season == "spring" and grass_status == 'long': 
        print("take cows to cowshed\nmow grass\n take cows back to pasture")
    else:
        print("wait")        
        
        
farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)


# In[ ]:




