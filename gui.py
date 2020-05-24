from tkinter import messagebox as mb


class Prediction:
    def start(self):
        mb.showinfo('Rules', 'Привіт, загадай число від 1 до 1000')
        answer = mb.askyesno('Rules', 'Загадав?')
        if answer == True:
            Prediction.guesser(self)
        else:
            Prediction.start(self)

    def guesser(self):
        a = 1
        b = 1000
        counter = 0
        while True:
            num = (a + b) // 2
            answer = mb.askyesno('Guess', f'Твоє число {num}? ')
            counter += 1
            if a - b == 1 or b - a == 1:
                mb.showinfo('Lie!', f'Твоє число: {num}!')
                break
            elif answer == True:
                return mb.showinfo('Congratulations!', f'Ура я відгадав! \n За {counter} спроб!')
            else:
                answer = mb.askyesno('Guess', f'Твоє число більше {num}? ')
                if answer == False:
                    b = num - 1
                elif answer == True:
                    a = num + 1
                else:
                    print('Ни нажав щось не то!')


a = Prediction()
if __name__ == "__main__":
    a.start()
