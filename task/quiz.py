name=input("Enter Your name:")
print("---------------------------------------------")
print("Hello",name)
print("---------------------------------------------")
print("Welcome to the Marvel quiz")
score=0
q1="""1.What is name of Ironman?
A.Tony Stark
B.Steve Rogers
C.Sam Wilson
D.James Rhodes"""
q2="""2.What is Captain America’s shield made of?
A.Adamantium
B.Vibranium
C.Promethium
D.Carbonadium"""
q3="""3.Before becoming Vision, what is the name of Iron Man’s A.I. butler?
A.H.O.M.E.R.
B.J.A.R.V.I.S.
C.A.L.F.R.E.D.
D.M.A.R.V.I.N"""
q4="""4.What is the real name of the Black Panther?
A.T’Challa
B.M’Baku
C.N’Jadaka
D.N’Jobu"""
q5="""5.Who was the last holder of the Space Stone before Thanos claims it for his Infinity Gauntlet?
A.Thor
B.Loki
C.The Collector
D.Tony Stark"""
q6="""6.Who is killed by Loki in the Avengers?
A.Maria Hill
B.Nick Fury
C.Agent Coulson
D.Doctor Erik Selvig"""
q7="""7.Where does Spider-Man shoot his webs from?
A.His wrists
B.His head
C.His feet
D.His eyes"""
q8="""8.Which newspaper did Peter Parker work? 
A.Daily Planet
B.Daily Bugle
C.Sunday Post
D.The New York Daily"""
q9="""9.In which order are the Infinity Stones revealed in the Marvel Cinematic Universe?
A. Time Stone, Space Stone, Power Stone, Soul Stone, Reality Stone and Mind Stone
B. Power Stone, Reality Stone, Time Stone, Space Stone, Mind Stone and Soul Stone
C. Reality Stone, Time Stone, Mind Stone, Soul Stone, Power Stone and Space Stone
D. Space Stone, Mind Stone, Reality Stone, Power Stone, Time Stone and Soul Stone"""
q10="""10.Erik Kilmonger is the villain in which movie?
A. Captain America: The First Avenger
B. Thor
C. Black Panther
D. Iron Man 3"""
answer={q1:"a",q2:"b",q3:"b",q4:"a",q5:"b",q6:"c",q7:"a",q8:"b",q9:"d",q10:"c"}

for i in answer:
    print("-----------------------------------------------------")
    print(i)
    ans=input("enter the answer: ")
    if ans==answer[i]:
        print("your answer is correct,you got 1 point")
        score= score+1
        print("current score",score)
    else:
        print("your answer is incorrect,you lost 1 point")
        score= score-1
        print("current score",score)
print("final score is",score)
        
