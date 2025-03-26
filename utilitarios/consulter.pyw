import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import messagebox, Tk, Toplevel, Frame, Label, Button, StringVar, Entry, Canvas
from tkinter.ttk import Combobox

from plyer import notification
from datetime import datetime, timedelta
from threading import Thread
from time import sleep

MOEDAS = {
    "Afghani do Afeganistão": "AFN",
    "Ariary Madagascarense": "MGA",
    "Baht Tailandês": "THB",
    "Balboa Panamenho": "PAB",
    "Birr Etíope": "ETB",
    "Bitcoin": "BTC",
    "Bolívar Venezuelano": "VEF",
    "Boliviano": "BOB",
    "Brent Spot": "XBR",
    "Cedi Ganês": "GHS",
    "Colón Costarriquenho": "CRC",
    "Colon de El Salvador": "SVC",
    "Córdoba Nicaraguense": "NIO",
    "Coroa Checa": "CZK",
    "Coroa Dinamarquesa": "DKK",
    "Coroa Islandesa": "ISK",
    "Coroa Norueguesa": "NOK",
    "Coroa Sueca": "SEK",
    "Dalasi da Gâmbia": "GMD",
    "Denar Macedônio": "MKD",
    "Dinar Argelino": "DZD",
    "Dinar do Bahrein": "BHD",
    "Dinar Iraquiano": "IQD",
    "Dinar Jordaniano": "JOD",
    "Dinar Kuwaitiano": "KWD",
    "Dinar Líbio": "LYD",
    "Dinar Sérvio": "RSD",
    "Dinar Tunisiano": "TND",
    "Dirham dos Emirados": "AED",
    "Dirham Marroquino": "MAD",
    "Dobra São Tomé/Príncipe": "STD",
    "Dogecoin": "DOGE",
    "Dólar Americano": "USD",
    "Dólar Australiano": "AUD",
    "Dólar Canadense": "CAD",
    "Dólar das Bahamas": "BSD",
    "Dólar das Ilhas Cayman": "KYD",
    "Dólar de Barbados": "BBD",
    "Dólar de Belize": "BZD",
    "Dólar de Brunei": "BND",
    "Dólar de Cingapura": "SGD",
    "Dólar de Fiji": "FJD",
    "Dólar de Hong Kong": "HKD",
    "Dólar de Trinidad": "TTD",
    "Dólar do Caribe Oriental": "XCD",
    "Dólar Jamaicano": "JMD",
    "Dólar Namíbio": "NAD",
    "Dólar Neozelandês": "NZD",
    "Dólar Taiuanês": "TWD",
    "Dólar Zimbabuense": "ZWL",
    "Dong Vietnamita": "VND",
    "Dram Armênio": "AMD",
    "DSE": "SDR",
    "Escudo cabo-verdiano": "CVE",
    "Ethereum": "ETH",
    "Euro": "EUR",
    "Florim Húngaro": "HUF",
    "Franco Burundinense": "BIF",
    "Franco CFA Central": "XAF",
    "Franco CFA Ocidental": "XOF",
    "Franco CFP": "XPF",
    "Franco Comorense": "KMF",
    "Franco de Guiné": "GNF",
    "Franco do Djubouti": "DJF",
    "Franco Ruandês": "RWF",
    "Franco Suíço": "CHF",
    "Franco Suíço": "CHFRTS",
    "Gourde Haitiano": "HTG",
    "Guarani Paraguaio": "PYG",
    "Guilder das Antilhas": "ANG",
    "Hryvinia Ucraniana": "UAH",
    "Iene Japonês": "JPY",
    "Kina Papua-Nova Guiné": "PGK",
    "Kip Laosiano": "LAK",
    "Kuna Croata": "HRK",
    "Kwacha Malauiana": "MWK",
    "Kwacha Zambiana": "ZMK",
    "Kwanza Angolano": "AOA",
    "Kyat de Mianmar": "MMK",
    "Lari Georgiano": "GEL",
    "Lek Albanês": "ALL",
    "Lempira Hondurenha": "HNL",
    "Leu Moldavo": "MDL",
    "Leu Romeno": "RON",
    "Lev Búlgaro": "BGN",
    "Libra Egípcia": "EGP",
    "Libra Esterlina": "GBP",
    "Libra Libanesa": "LBP",
    "Libra Síria": "SYP",
    "Libra Sudanesa": "SDG",
    "Lilangeni Suazilandês": "SZL",
    "Litecoin": "LTC",
    "Loti do Lesoto": "LSL",
    "Manat Azeri": "AZN",
    "Marco Conversível": "BAM",
    "Metical de Moçambique": "MZN",
    "Mongolian Tugrik": "MNT",
    "Naira Nigeriana": "NGN",
    "Naira Nigeriana": "NGNI",
    "Naira Nigeriana": "NGNPARALLEL",
    "Nova Lira Turca": "TRY",
    "Novo Shekel Israelense": "ILS",
    "Ouguiya Mauritana": "MRO",
    "Ouro": "XAU",
    "Pataca de Macau": "MOP",
    "Peso Argentino": "ARS",
    "Peso Chileno": "CLP",
    "Peso Colombiano": "COP",
    "Peso Cubano": "CUP",
    "Peso Dominicano": "DOP",
    "Peso Filipino": "PHP",
    "Peso Mexicano": "MXN",
    "Peso Uruguaio": "UYU",
    "Prata": "XAGG",
    "Pula de Botswana": "BWP",
    "Quetzal Guatemalteco": "GTQ",
    "Rand Sul-Africano": "ZAR",
    "Real Brasileiro Turismo": "BRLT",
    "Real Brasileiro": "BRL",
    "Rial Catarense": "QAR",
    "Rial Iraniano": "IRR",
    "Rial Omanense": "OMR",
    "Riel Cambojano": "KHR",
    "Ringgit Malaio": "MYR",
    "Riyal Iemenita": "YER",
    "Riyal Saudita": "SAR",
    "Rublo Bielorrusso": "BYN",
    "Rublo Russo": "RUB",
    "Rublo Russo": "RUBTOD",
    "Rublo Russo": "RUBTOM",
    "Rufiyaa Maldiva": "MVR",
    "Rúpia de Sri Lanka": "LKR",
    "Rúpia Indiana": "INR",
    "Rupia Indonésia": "IDR",
    "Rúpia Mauriciana": "MUR",
    "Rúpia Nepalesa": "NPR",
    "Rúpia Paquistanesa": "PKR",
    "Rúpias de Seicheles": "SCR",
    "Shilling Queniano": "KES",
    "Shilling Somaliano": "SOS",
    "Shilling Tanzaniano": "TZS",
    "Shilling Ugandês": "UGX",
    "Sol do Peru": "PEN",
    "Som Quirguistanês": "KGS",
    "Som Uzbequistanês": "UZS",
    "Somoni do Tajiquistão": "TJS",
    "Taka de Bangladesh": "BDT",
    "Tengue Cazaquistanês": "KZT",
    "TMT": "TMT",
    "Vatu de Vanuatu": "VUV",
    "Won Sul-Coreano": "KRW",
    "XRP": "XRP",
    "Yuan chinês offshore": "CNH",
    "Yuan Chinês": "CNY",
    "Zlóti Polonês": "PLN"
}

API = 'https://economia.awesomeapi.com.br'

class App:
    def __init__(self) -> None:
        self.raiz = Tk()
        self.raiz.title('Consultor de Cotação')
        self.raiz.resizable(width=False, height=False)

        self.quadro = Frame(self.raiz)
        self.quadro.grid(row=1, column=1, padx=10, pady=10)

        self._ = Label(self.quadro, text='De:', font='arial 12', relief='groove', width=10)
        self._.grid(row=1, column=1, padx=2, pady=2)

        self._ = Label(self.quadro, text='Para:', font='arial 12', relief='groove', width=10)
        self._.grid(row=2, column=1, padx=2, pady=2)

        self.caixa1 = Combobox(self.quadro, values=[moeda for moeda in MOEDAS], width=25, state='readonly')
        self.caixa1.grid(row=1, column=2, padx=2, pady=2)

        self.caixa2 = Combobox(self.quadro, values=[moeda for moeda in MOEDAS], width=25, state='readonly')
        self.caixa2.grid(row=2, column=2, padx=2, pady=2)

        self._ = Button(self.quadro, font='arial 12', text='Consultar', command=self.consultar, width=10)
        self._.grid(row=3, column=1, columnspan=2, padx=2, pady=2)

        self.dados = {
            'Compra': StringVar(self.raiz),
            'Alta': StringVar(self.raiz),
            'Baixa': StringVar(self.raiz),
            'Variação': StringVar(self.raiz),
            'Data': StringVar(self.raiz)
        }

        for (linha, dado) in enumerate(self.dados, 4):
            self._ = Label(self.quadro, text=f'{dado}:', font='arial 12', relief='groove', width=10)
            self._.grid(row=linha, column=1, padx=2, pady=2)
            self._ = Label(self.quadro, textvariable=self.dados[dado], font='arial 12', relief='groove', width=19)
            self._.grid(row=linha, column=2, padx=2, pady=2)

        self.botao_monitorar = Button(self.quadro, font='arial 12', text='Monitorar', command=self.monitorar, width=10)
        self.botao_monitorar.grid(row=9, column=1, padx=2, pady=2)
        self.botao_monitorar.config(state='disabled')

        self.botao_historico = Button(self.quadro, font='arial 12', text='Gerar Histórico', command=self.gerar_historico, width=18)
        self.botao_historico.grid(row=9, column=2, padx=2, pady=2)
        self.botao_historico.config(state='disabled')

        self.pausado = True
        self.monitor = Thread(target=self.notificar)
        self.monitor.daemon = True
        self.monitor.start()

        self.fig_canvas = None
        self.toolbar = None

        self.raiz.mainloop()

    def consultar(self,) -> None:
        try:
            self.pausado = True
            self.moeda1 = MOEDAS[self.caixa1.get()]
            self.moeda2 = MOEDAS[self.caixa2.get()]
        except:
            messagebox.showerror('Erro!', 'Selecione as moedas.')
        else:
            self.atualizar()

    def atualizar(self) -> None:
        try:
            self.url = f'{API}/last/{self.moeda1}-{self.moeda2}'
            self.cotacao = requests.get(self.url).json()[f'{self.moeda1}{self.moeda2}']
        except:
            self.botao_monitorar.config(state='disabled')
            self.botao_historico.config(state='disabled')
            for dado in self.dados:
                self.dados[dado].set('')
            messagebox.showerror('Erro!', 'Cotação ainda não disponível na API.')
        else:
            self.dados['Compra'].set(self.cotacao['bid'])
            self.dados['Alta'].set(self.cotacao['high'])
            self.dados['Baixa'].set(self.cotacao['low'])
            self.dados['Variação'].set(self.cotacao['varBid'])
            self.dados['Data'].set(self.cotacao['create_date'])
            self.botao_monitorar.config(state='normal')
            self.botao_historico.config(state='normal')

    def monitorar(self) -> None:
        self.janela = Toplevel(self.raiz)
        self.janela.title('Monitor de Cotações')
        self.janela.resizable(width=False, height=False)
        self._ = Label(self.janela, text='Limiar:', font='arial 12', relief='groove', width=10)
        self._.grid(row=1, column=1, padx=2, pady=2)
        self.entrada = Entry(self.janela, font='arial 12', width=15)
        self.entrada.grid(row=1, column=2, padx=2, pady=2)
        self._ = Button(self.janela, text='Definir', font='arial 12', command=self.definir, width=15)
        self._.grid(row=2, column=1, columnspan=2, padx=2, pady=2)

    def definir(self) -> None:
        try:
            self.limiar = float(self.entrada.get())
            if self.limiar <= 0:
                raise ValueError()
        except:
            messagebox.showerror('Erro', 'Valor Inválido.')
            self.janela.destroy()
        else:
            self.pausado = False
            self.janela.destroy()

    def notificar(self) -> None:
        while True:
            sleep(1)
            if not self.pausado:
                sleep(60)
                self.atualizar()
                try:
                    valor = float(self.cotacao['bid'])
                    if self.limiar > 0 and valor > self.limiar:
                        notification.notify(
                            message='A cotação cruzou o limiar definido.',
                            title='Monitor de Cotação',
                            timeout=3
                        )
                except:
                    pass

    def gerar_historico(self) -> None:
        self.janela_historico = Toplevel(self.raiz)
        self.janela_historico.title('Gerador de Histórico')
        self.janela_historico.resizable(width=False, height=False)

        self.frame_opcoes = Frame(self.janela_historico)
        self.frame_opcoes.grid(row=1, column=1, padx=10, pady=10)

        self._ = Button(self.frame_opcoes, text='15 Dias', font='arial 12', command=lambda: self.gerar_grafico(15), width=15)
        self._.grid(row=1, column=1, padx=2, pady=2)
        self._ = Button(self.frame_opcoes, text='1 Mês', font='arial 12', command=lambda: self.gerar_grafico(30), width=15)
        self._.grid(row=1, column=2, padx=2, pady=2)
        self._ = Button(self.frame_opcoes, text='3 Meses', font='arial 12', command=lambda: self.gerar_grafico(90), width=15)
        self._.grid(row=1, column=3, padx=2, pady=2)
        self._ = Button(self.frame_opcoes, text='6 Meses', font='arial 12', command=lambda: self.gerar_grafico(180), width=15)
        self._.grid(row=1, column=4, padx=2, pady=2)
        self._ = Button(self.frame_opcoes, text='12 Meses', font='arial 12', command=lambda: self.gerar_grafico(365), width=15)
        self._.grid(row=1, column=5, padx=2, pady=2)

        self.canvas_grafico = Canvas(self.janela_historico, width=800, height=400)
        self.canvas_grafico.grid(row=2, column=1, padx=10, pady=10)

    def gerar_grafico(self, dias: int) -> None:
        data_final = datetime.today()
        data_inicial = data_final - timedelta(days=dias)

        url_historico = f'{API}/json/daily/{self.moeda1}-{self.moeda2}/360'
        response = requests.get(url_historico)

        if response.status_code != 200:
            messagebox.showerror('Erro', 'Não foi possível obter os dados históricos.')
            return

        historico = response.json()
        valores = []
        datas = []

        for dia in historico:
            data = datetime.fromtimestamp(int(dia['timestamp']))
            if data_inicial <= data <= data_final:
                datas.append(data)
                valores.append(float(dia['bid']))

        if not datas:
            messagebox.showinfo('Informação', 'Nenhum dado encontrado para o período especificado.')
            return

        if self.fig_canvas:
            self.fig_canvas.get_tk_widget().destroy()
        if self.toolbar:
            self.toolbar.destroy()

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(datas, valores, marker='o')
        ax.set_xlabel('Data')
        ax.set_ylabel('Valor da Cotação')
        ax.set_title(f'Histórico de Cotações de {self.moeda1} para {self.moeda2}')
        ax.grid(True)

        self.fig_canvas = FigureCanvasTkAgg(fig, master=self.canvas_grafico)
        self.fig_canvas.draw()
        self.fig_canvas.get_tk_widget().pack()

        self.toolbar = NavigationToolbar2Tk(self.fig_canvas, self.canvas_grafico)
        self.toolbar.update()
        self.fig_canvas.get_tk_widget().pack()

if __name__ == '__main__': App()
