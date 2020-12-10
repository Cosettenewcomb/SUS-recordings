import jiwer
from jiwer import wer


def errorRate(ground_truth, hypothesis):
    error = wer(ground_truth, hypothesis)
    return error

s1 = errorRate("When does the glass thank the wrong hand", 
    "When does the glass Bank the wrong hand")
print(s1)
​
s2 = errorRate("When does the art catch the fair song",
    "When does the art catch the fair song")
print(s2)
​
s3 = errorRate("When does the course convict the free bank",
    "When does the course convict the free Bank")
print(s3)
​
s4 = errorRate("Why does the jazz hit the brown bar",
    "why does the jazz hit the brown bar")
print(s4)
​
s5 = errorRate("the dishonest audiences began the corny Rosemary",
    "the dishonest audiences began the corny Rosemary")
print(s5)
​
s6 = errorRate("where does the press waste the green court",
    " where does the press waste the green court")
print(s6)
​
s7 = errorRate("when does the flow guide the blue front",
    "when does the flow guide the blue front")
print(s7)
​
s8 = errorRate("The clumsy thundershowers undid the honorary referendum",
    "the clumsy thundershowers Undead the honorary referendum")
print(s8)
​
s9 = errorRate("the lucrative cooperatives swam the Triangular connoisseur",
    "the lucrative cooperatives swam the Triangular connoisseur")
print(s9)
​
s10 = errorRate("The unable worlds oversaw the nucleic accelerator",
    "The Honorable world's oversaw the nucleic accelerator")
print(s10)
​
s11 = errorRate("The indoor heights retook the northeastern impediment",
    "indoor Heights retook the northern and pediat")
print(s11)
​
s12 = errorRate("The estimable duties nipped the hazardous diner",
    "The estimable duties nip the Hazardous Diner")
print(s12)
​
s13 = errorRate("The uneven rites swam the feverish hub",
    "The uneven rights swarm the feverish Pub")
print(s13)
​
s14 = errorRate("the salty controversies outdid the geometric monoxide",
    "the salty controversies outdated the geometric monoxide")
print(s14)
​
s15 = errorRate("he petty mangers arose the bearable borzoi",
    "Eddie managers are rose the bearable bourgeois")
print(s15)
​
s16 = errorRate("the portly spinners drew the hidebound organist",
    "Spinners drew the hidebound organist")
print(s16)
​
s17 = errorRate("the sluggish industries overtook the sinister fiat",
    "the sluggish Industries overtook the Sinister black")
print(s17)
​
s18 = errorRate("the catholic musicals ate the accountable newness",
    "Catholic musicals ate the accountable newness")
print(s18)
​
s19 = errorRate("The agrarian grams overran the counterproductive tablespoon",
    "The Agrarian grams over and the counterproductive tablespoon")
print(s19)
​
s20 = errorRate("the renowned traits outran the turbulent kingdom",
    "renowned traits out R and turbulent Kingdom")
print(s20)
​
s21 = errorRate("the exuberant assurances knew the dictatorial pint",
    "exuberant assurances new the dictatorial pint")
print(s21)
​
s22 = errorRate("the interscholastic fragrances strove the industrial plaid",
 "the interscholastic fragrances Stroh the industrial glad")
print(s22)
​
s23 = errorRate("the droll sacraments undertook the spotty Opera",
 "the dolls sacraments undertook the spotty Opera")
print(s23)
​
s24 = errorRate("the unseeded hemophiliacs overcame the pregnant chunk",
 "the unseeded hemophiliacs overcame the pregnant shock")
print(s24)

s25 = errorRate("the repentant tuneup drew the magical tsarina",
    "the repentant tune-up drew the magical Serena")
print(s25)

sum = (s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10 + s11 + s12 + s13 + s14 + s15 + s16 + s17 + s18 + s19 + s20 + s21 + s22 + s23 + s24 + s25)/25
print("sum = ", sum)