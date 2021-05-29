from Biblioteki import ButtonMenu, readfile, writefile, create_mouse_click_list, generate_points_circle
from Claster import Centroid


class KmeansCore:
    def __init__(self, parent: ButtonMenu):
        self.parent = parent
        self.parent.changeinfo("Kmeans klasyfikator by s21001")

    def create_2d_data(self):
        path, cancel = self.parent.collectdata("Tworzenie danych", "Podaj ścieżkę gdzie zapisać dane")
        if cancel:
            return

        answer = self.parent.askquestion(inputname="Tworzenie zbioru danych", message="Kliknij OK, aby rozpocząć\n"
                                         "Klikaj LPM w dowolnym miejscu aby dodać punkt w miejscu przebywania myszki\n"
                                         "Kliknij PPM aby zakończyć\n")

        if not answer:
            return
        lista = create_mouse_click_list()
        writefile(data=lista, filepath=path, delimiter=",")

        self.parent.drawscatter(lista, nazwa="Punkty")
        self.parent.showdata(f"Gotowe! Zobacz wyniki w pliku {path}")

    @staticmethod
    def _core_group(data: list, k: int, iteracje=20) -> dict:

        ziarno = generate_points_circle(Centroid.prepare_average_point(data), n=k, r=100)
        result = {i: Centroid(ziarno[i]) for i in range(k)}
        stabilne = False

        ilosci_n = dict()
        while not stabilne:
            for centroid in result.keys():
                result.get(centroid).clear()

            for point in data:
                dlugosci = dict()
                for centroid in result.keys():
                    dlugosci[centroid] = result.get(centroid).count_distance(point)
                closest = sorted(dlugosci.items(), key=lambda x: x[1], reverse=False)[0][0]
                result[closest].add_point(point)

            for centroid in result.keys():
                result.get(centroid).count_centroid()

            ilosci_n1 = ilosci_n
            ilosci_n = {klucz: len(result.get(klucz)) for klucz in result.keys()}

            stabilne = True
            for n1, n in zip(ilosci_n1.items(), ilosci_n.items()):
                if n1[1] != n[1]:
                    stabilne = False
                    break

        clean_result = {numer: result.get(numer).get_points() for numer in result.keys()}
        return clean_result

    def group(self):
        dataPath, cancel = self.parent.collectdata("Grupowanie", "Podaj ścieżkę do pliku z danymi")
        if cancel:
            return

        k, cancel = self.parent.collectdata("Grupowanie", "Na ile grup podzielić?")
        if cancel:
            return

        try:
            data = readfile(dataPath, ",")
            result = self._core_group(data=data, k=int(k))
            if len(data[0]) == 2:
                wykres = self.parent.askquestion("Grupowanie", "Grupowane punkty są w przestrzeni 2D czy narysować "
                                                               "wykres?")
                if wykres:
                    self.parent.draw_groups_scatter(result)

            for klucz in result.keys():
                print(f"Do klastra {klucz} zostały przydzielone punkty:")
                for punkt in result.get(klucz):
                    print(f"Punkt: {punkt}")
            self.parent.showdata("Gotowe", important=False)
        except Exception:
            self.parent.showdata("Coś poszło nie tak, upewnij się, że ścieżka do danych jest poprawna"
                                 "i dane nie są zanieczyszczone", important=True)
