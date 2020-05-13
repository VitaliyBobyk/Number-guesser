class Prediction():
    def start(self):
        answer = input('Загадали?:Так/Ні ')
        if answer == 'Так':
            Prediction.guesser(self)
        else:
            Prediction.start(self)
    def rules(self):
        print('Привіт, загадай число від 1 до 1000')
        return Prediction.start(self)
    def guesser(self):
        a = 1
        b = 1000
        counter = 0
        while True:
            num = (a + b) // 2
            answer = input(f'Твоє число {num}? ')
            counter += 1
            if a - b == 1 or b - a == 1:
                print(f'Твоє число: {num}!')
                break
            elif answer == '=':
                print('Ура я відгадав!')
                print(f'За {counter} спроб!')
            elif answer == '<':
                b = num - 1
            elif answer == '>':
                a = num + 1
            else:
                print('Ни нажав щось не то!')




a = Prediction
a.rules('Number')