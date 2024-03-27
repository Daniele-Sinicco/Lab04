import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view


    def handleSpellCheck(self,e):
        """
        print(str(self._view._language.value))
        print(str(self._view._search.value))
        print(str(self._view._input.value))
        """
        self._view._lvOut.controls.clear()
        self._view.update()
        if self._view._language.value == None or self._view._search.value == None or self._view._input.value == "":
            self._view._lvOut.controls.append(ft.Text("All fields should be filled."))
            self._view.update()
        else:
            errate, tempo = self.handleSentence(self._view._input.value, self._view._language.value, self._view._search.value)
            errate_split = errate.split(" - ")
            for err in errate_split:
                self._view._lvOut.controls.append(ft.Text(err))
            tempo_str = "Time elapsed: " + str(tempo)
            self._view._lvOut.controls.append(ft.Text(tempo_str))
            self._view.update()


    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split(" ")
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text