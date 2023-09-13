import os
print("Current Java Version")
os.system("java -version")

javaversions = ["1)\tJava 8 | 1.8.0_242 | AdoptOpenJDK (JRE)",
                "2)\tJava 8 | 1.8.0_292 | AdoptOpenJDK",
                "3)\tJava 8 | 1.8.0_351 | Oracle",
                "4)\tJava 8 | 1.8.0_352 | OpenLogic-OpenJDK",
                "5)\tJava 8 | 1.8.0_362 | Eclipse Temurin",
                "7)\tJava 8 | 1.8.0_382 | Eclipse Temurin",
                "8)\tJava 8 | 1.8.361.09 | Oracle",
                "9)\tJava 11 | 11.0.16.1 | Microsoft Build of OpendJDK",
                "10)\tJava 15 | 15.0.9 | Azul Zulu",
                "11)\tJava 16 | 16.0.2 | Eclipse Temurin",
                "12)\tJava 17 | 17.0.6 | Amazon Corretto"
                ]
print("Available Java Versions")
for i in range(11):
    print(javaversions[i])
inputresult = str(input("Select Java Version (1-12)"))
if inputresult == "1":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_242`")
elif inputresult == "2":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")
elif inputresult == "3":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")     
elif inputresult == "4":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")
elif inputresult == "5":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")      
elif inputresult == "6":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")
elif inputresult == "7":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")   
elif inputresult == "8":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")   
elif inputresult == "9":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")
elif inputresult == "10":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")
elif inputresult == "11":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")
elif inputresult == "12":
    os.system("export JAVA_HOME=`/usr/libexec/java_home -v 1.8.0_292`")
else:
    print("False Input")