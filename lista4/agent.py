import networkx as nx
import matplotlib.pyplot as plt
import random, time, os, glob
from PIL import Image

def walk(loop_time, how_many, out_path):
    """
    Function
    Funkcja zapisująca do folderu pliki w formacie jpg, będące klatkami do GIF'a, przedstawiającego spacer agenta po grafie Barabasi-Alberta.

    Input
    loop_time(int) - odcinki czasu, w których pliki będą zrzucane do folderu
    how_many(int) - liczba klatek, z których ma być zrobiony gif (inaczej liczba przejść agenta po grafie)
    out_path(str) - ścieżka do folderu, gdzie zrzucane będą klatki

    """
    G = nx.barabasi_albert_graph(10,1)
    colors = ["green" for i in range(len(G))]
    position = nx.spring_layout(G)
    nx.draw(G, pos=position, node_color=colors, with_labels=True)
    n0 = 0
    total_time = 0
    while total_time < how_many:
        for i in range(how_many):
            neighbours = []
            for edge in G.edges:
                if n0 in edge:
                    if edge.index(n0) == 1:
                        neighbours.append(edge[0])
                    else:
                        neighbours.append(edge[1])
            colors[n0] = "red"
            nx.draw(G, pos=position, node_color=colors, with_labels=True)
            clock = time.time()
            pic_name = "walk" + str(clock) + ".jpg"
            pic_path = os.path.join(out_path, pic_name)
            plt.savefig(pic_path)
            colors[n0] = "green"
            pick = random.choice(neighbours)
            n0 = pick
            time.sleep(loop_time)
            total_time += 1

walk(3, 5, r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 4\node_walk")

def gif(pics_path, time=500, loops=1):
    """
    Function
    Funkcja tworząca GIF z klatek zapisanych w folderze

    Input
    pics_path(str) - ścieżka do folderu zawierającego klatki do GIF'a
    time(int) - opóźnienie klatki w milisekundach (domyślnie 500)
    loops(int) - liczba przejść GIF'a zanim się zatrzyma

    """
    pics = []
    for root, dirs, files in os.walk(pics_path):
        for file in files:
            file_path = os.path.join(root, file)
            pics.append(Image.open(file_path))
    first_pic = pics[0]
    first_pic.save("agent.gif", format="GIF", append_images=pics, save_all=True, duration=time, loop=loops)

gif(r"C:\Users\Rafal\OneDrive\Pulpit\programowanie 2 sem\lista 4\node_walk")
