# Hugo Solares

import pandas as pd
import matplotlib.pyplot as plt

# Data Keys
agregados_monetarios_creditos_key = 'agg_mon_cred'
balance_fiscal_key = 'bal_fis'
balanza_comercial_key = 'bal_com'
balanza_pagos_key = 'bal_pag'
cuentas_nacionales_key = 'cuen_nac'
deuda_externa_key = 'deu_ext'
deuda_publica_key = 'deu_pub'
indicadores_solidez_financiera_key = 'ind_sol_fin'
mercado_laboral_key = 'merc_lab'
precios_key = 'precios'
reservas_internacionales_key = 'res_int'
servicio_deuda_externa_key = 'serv_deu_ext'
tasas_de_cambio_key = 'tas_camb'
tasas_de_interes_key = 'tas_int'
terminos_intercambio_key = 'term_interc'

# Data file path
agregados_monetarios_creditos_file_path = 'data/agregados_monetarios_credito.csv'
balance_fiscal_file_path = 'data/balance_fiscal.csv'
balanza_comercial_file_path = 'data/balanza_comercial.csv'
balanza_pagos_file_path = 'data/balanza_pagos.csv'
cuentas_nacionales_file_path = 'data/cuentas_nacionales.csv'
deuda_externa_file_path = 'data/deuda_externa.csv'
deuda_publica_file_path = 'data/deuda_publica.csv'
indicadores_solidez_financiera_file_path = 'data/indicadores_solidez_financiera.csv'
mercado_laboral_file_path = 'data/mercado_laboral.csv'
precios_file_path = 'data/precios.csv'
reservas_internacionales_file_path = 'data/reservas_internacionales_netas.csv'
servicio_deuda_externa_file_path = 'data/servicio_deuda_externa.csv'
tasas_de_cambio_file_path = 'data/tasas_de_cambio.csv'
tasas_de_interes_file_path = 'data/tasas_de_interes.csv'
terminos_intercambio_file_path = 'data/terminos_intercambio.csv'

# Column labels
fecha_estructurada = '[Fecha_Estructurada]'
nombre_indicador = '[NombreIndicador]'


class Analyzer:
    def __init__(self, data_selector):
        try:
            # Initialize DF with the data selected
            self.df = self.set_data(data_selector)

            # Initialize the country list
            self.country_list = ['ARGENTINA', 'BOLIVIA', 'BRASIL', 'CHILE', 'COLOMBIA', 'COSTA RICA',
                                 'REPUBLICA DOMINICANA', 'ECUADOR', 'GUATEMALA', 'HONDURAS', 'JAMAICA',
                                 'MEXICO', 'NICARAGUA', 'PANAMA', 'PERU', 'PARAGUAY', 'EL SALVADOR', 'URUGUAY',
                                 'VENEZUELA']

        # Handle exceptions
        except FileNotFoundError:
            print(f"Error: File not found for: '{data_selector}'.")
            self.df = None

        except pd.errors.ParserError:
            print(f"Error: Parsing issue for: '{data_selector}'.")
            self.df = None

    # Use the data selector key to select and return the DF
    def set_data(self, data_selector):
        if data_selector == agregados_monetarios_creditos_key:
            return pd.read_csv(agregados_monetarios_creditos_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == balance_fiscal_key:
            return pd.read_csv(balance_fiscal_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == balanza_comercial_key:
            return pd.read_csv(balanza_comercial_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == balanza_pagos_key:
            return pd.read_csv(balanza_pagos_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == cuentas_nacionales_key:
            return pd.read_csv(cuentas_nacionales_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == deuda_externa_key:
            return pd.read_csv(deuda_externa_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == deuda_publica_key:
            return pd.read_csv(deuda_publica_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == indicadores_solidez_financiera_key:
            return pd.read_csv(indicadores_solidez_financiera_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == mercado_laboral_key:
            return pd.read_csv(mercado_laboral_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == precios_key:
            return pd.read_csv(precios_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == reservas_internacionales_key:
            return pd.read_csv(reservas_internacionales_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == servicio_deuda_externa_key:
            return pd.read_csv(servicio_deuda_externa_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == tasas_de_cambio_key:
            return pd.read_csv(tasas_de_cambio_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == tasas_de_interes_key:
            return pd.read_csv(tasas_de_interes_file_path, delimiter=';', encoding='utf-16')
        elif data_selector == terminos_intercambio_key:
            return pd.read_csv(terminos_intercambio_file_path, delimiter=';', encoding='utf-16')
        elif data_selector is None:
            return None
        else:
            raise ValueError("Invalid data_selector provided.")

    def exercise_1(self):
        my_data = self.date_range(self.df, '2020-01-01', '2024-01-01')

        # my_data = my_data[my_data[nombre_indicador] == 'base monetaria, moneda nacional']
        # my_data = my_data[my_data[nombre_indicador] == 'depositos en moneda nacional, moneda nacional']
        # my_data = my_data[my_data[nombre_indicador] == 'depositos en moneda extranjera, moneda nacional']
        # my_data = my_data[my_data[nombre_indicador] == 'm2, moneda nacional']
        # my_data = my_data[my_data[nombre_indicador] == 'credito en moneda extranjera, moneda nacional']
        my_data = my_data[my_data[nombre_indicador] == 'credito en moneda nacional, moneda nacional']

        country_columns = self.filter_countries('VENEZUELA')

        self.plotter(my_data, country_columns)

    def exercise_2(self):
        my_data = self.date_range(self.df, '2020-01-01', '2024-01-01')

        # my_data = my_data[my_data[nombre_indicador] == 'resultado fiscal total público, moneda nacional']
        my_data = my_data[my_data[nombre_indicador] == 'resultado fiscal primario público, moneda nacional']

        self.plotter(my_data, self.country_list)

    def exercise_3(self):
        my_data = self.date_range(self.df, '2020-01-01', '2024-01-01')

        # my_data = my_data[my_data[nombre_indicador] == 'importaciones de bienes (mensual), dolares']
        my_data = my_data[my_data[nombre_indicador] == 'exportaciones de bienes (mensual), dolares']

        countries = self.filter_countries(['MEXICO', 'BRASIL'])

        self.plotter(my_data, countries)

    def exercise_4(self):
        my_data = self.date_range(self.df, '2020-01-01', '2024-01-01')

        unique_values = my_data[nombre_indicador].unique()
        print(unique_values)

    def date_range(self, data, from_date, to_date):
        data[fecha_estructurada] = pd.to_datetime(data[fecha_estructurada])
        return data[(data[fecha_estructurada] >= from_date) & (data[fecha_estructurada] < to_date)]

    def filter_countries(self, country_to_trim):
        return [country for country in self.country_list if country not in country_to_trim]

    def plotter(self, data, country_columns):
        formatted_country_columns = ['[' + country + ']' for country in country_columns]

        for country in formatted_country_columns:
            plt.plot(data[fecha_estructurada], data[country], label=country)

        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title('Values for Each Country Over Time')
        plt.legend()

        plt.show()


if __name__ == '__main__':
    try:
        # Analyzer(agregados_monetarios_creditos_key).exercise_1()
        # Analyzer(balance_fiscal_key).exercise_2()
        # Analyzer(balanza_comercial_key).exercise_3()
        Analyzer(balanza_pagos_key).exercise_4()

    # Handle the exceptions appropriately
    except ValueError as e:
        print(e)

    except AttributeError as e:
        print(e)
