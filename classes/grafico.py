import matplotlib.pyplot as plt


class Grafico:
    def medias_absolutas(self, dados):
        fig, ax = plt.subplots()
        ax.plot(dados)
        ax.set(
            ylabel = '% Erro',
            xlabel = 'Épocas',
            title  = '% Erro por Épocas' )
        ax.grid()
        plt.show()
