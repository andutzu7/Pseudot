from functools import reduce
import re

input_text = "Yugoslavia (/ˌjuːɡoʊˈslɑːviə/; Serbo-Croatian: Jugoslavija / Југославија [juɡǒslaːʋija]; Slovene: Jugoslavija [juɡɔˈslàːʋija]; Macedonian: Југославија [juɡɔˈsɫavija];[A] lit. 'South Slavic Land') was a country in Southeast Europe and Central Europe for most of the 20th century. It came into existence after World War I in 1918[B] under the name of the Kingdom of Serbs, Croats and Slovenes by the merger of the provisional State of Slovenes, Croats and Serbs (which was formed from territories of the former Austro-Hungarian Empire) with the Kingdom of Serbia, and constituted the first union of the South Slavic people as a sovereign state, following centuries in which the region had been part of the Ottoman Empire and Austria-Hungary. Peter I of Serbia was its first sovereign. The kingdom gained international recognition on 13 July 1922 at the Conference of Ambassadors in Paris.[2] The official name of the state was changed to Kingdom of Yugoslavia on 3 October 1929.Yugoslavia was invaded by the Axis powers on 6 April 1941. In 1943, a Democratic Federal Yugoslavia was proclaimed by the Partisan resistance. In 1944 King Peter II, then living in exile, recognised it as the legitimate government. The monarchy was subsequently abolished in November 1945. Yugoslavia was renamed the Federal People's Republic of Yugoslavia in 1946, when a communist government was established. It acquired the territories of Istria, Rijeka, and Zadar from Italy. Partisan leader Josip Broz Tito ruled the country as president until his death in 1980. In 1963, the country was renamed again, as the Socialist Federal Republic of Yugoslavia (SFRY).The six constituent republics that made up the SFRY were the SR Bosnia and Herzegovina, SR Croatia, SR Macedonia, SR Montenegro, SR Serbia, and SR Slovenia. Serbia contained two Socialist Autonomous Provinces, Vojvodina and Kosovo, which after 1974 were largely equal to the other members of the federation.[3][4] After an economic and political crisis in the 1980s and the rise of nationalism, Yugoslavia broke up along its republics' borders, at first into five countries, leading to the Yugoslav Wars. From 1993 to 2017, the International Criminal Tribunal for the former Yugoslavia tried political and military leaders from the former Yugoslavia for war crimes, genocide, and other crimes committed during those wars.After the breakup, the republics of Montenegro and Serbia formed a reduced federative state, the Federal Republic of Yugoslavia (FRY), known from 2003 to 2006 as Serbia and Montenegro. This state aspired to the status of sole legal successor to the SFRY, but those claims were opposed by the other former republics. Eventually, it accepted the opinion of the Badinter Arbitration Committee about shared succession[5] and in 2003 its official name was changed to Serbia and Montenegro. This state dissolved when Montenegro and Serbia each became independent states in 2006, while Kosovo proclaimed its independence from Serbia in 2008. "


reducedDataList=[]

def my_map(key):
    return (key,1)


def SortTuple(tup):

    # Getting the length of list
    # of tuples
    n = len(tup)

    for i in range(n):
        for j in range(n-i-1):

            if tup[j][0] > tup[j + 1][0]:
                tup[j], tup[j + 1] = tup[j + 1], tup[j]
    return tup

def my_reduce(element0,element1):
    if element0[0] == element1[0]:
        return (element0[0],element0[1]+1)
    else:
        reducedDataList.append(element0)
        return (element1[0],1)

if __name__=="__main__":
    mappedData=re.split('[:,\s\n]{1}', input_text)
    mappedData=map(my_map,mappedData)
    mappedData = list(mappedData)
    sortedData=SortTuple(mappedData)
    reducedData=reduce(my_reduce,sortedData)
    reducedDataList.append(reducedData)
    print(reducedDataList)
