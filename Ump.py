import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class UMPFinanceAnalyzer:
    def __init__(self):
        self.parti = "Union pour un Mouvement Populaire (UMP)"
        self.colors = ['#0066CC', '#FF6600', '#009900', '#990099', '#FF3366', 
                      '#33CCCC', '#FFCC00', '#666699', '#CC0066', '#339933']
        
        self.start_year = 2002  # Création de l'UMP
        self.end_year = 2025
        self.creation_year = 2002
        self.renommage_year = 2015  # Devenu Les Républicains
        
        # Configuration spécifique à l'UMP
        self.config = {
            "type": "parti_politique",
            "orientation": "droite",
            "electorat_cible": ["cadres", "entrepreneurs", "retraites", "rural"],
            "budget_base": 25,  # millions d'euros
            "adherents_base": 200000,
            "importance": "majeur",
            "sources_financement": ["cotisations", "dons", "financement_public", "evenements", "formations"]
        }
        
    def generate_financial_data(self):
        """Génère des données financières pour l'UMP"""
        print(f"🏛️ Génération des données financières pour {self.parti}...")
        
        # Créer une base de données annuelle
        dates = pd.date_range(start=f'{self.start_year}-01-01', 
                             end=f'{self.end_year}-12-31', freq='Y')
        
        data = {'Annee': [date.year for date in dates]}
        
        # Données d'adhérents et structure
        data['Adherents'] = self._simulate_adherents(dates)
        data['Federations_Departementales'] = self._simulate_federations(dates)
        data['Elus_Locaux'] = self._simulate_elus_locaux(dates)
        data['Elus_Nationaux'] = self._simulate_elus_nationaux(dates)
        
        # Revenus du parti
        data['Revenus_Total'] = self._simulate_total_revenue(dates)
        data['Cotisations_Adherents'] = self._simulate_membership_fees(dates)
        data['Dons_Prives'] = self._simulate_private_donations(dates)
        data['Financement_Public'] = self._simulate_public_funding(dates)
        data['Revenus_Evenements'] = self._simulate_event_revenue(dates)
        data['Revenus_Formations'] = self._simulate_training_revenue(dates)
        data['Emprunts'] = self._simulate_loans(dates)
        
        # Dépenses du parti
        data['Depenses_Total'] = self._simulate_total_expenses(dates)
        data['Depenses_Personnel'] = self._simulate_staff_expenses(dates)
        data['Depenses_Campagnes'] = self._simulate_campaign_expenses(dates)
        data['Depenses_Communication'] = self._simulate_communication_expenses(dates)
        data['Depenses_Fonctionnement'] = self._simulate_operating_expenses(dates)
        data['Depenses_Formation'] = self._simulate_training_expenses(dates)
        data['Remboursements_Emprunts'] = self._simulate_loan_repayments(dates)
        
        # Indicateurs financiers
        data['Taux_Execution_Budget'] = self._simulate_budget_execution_rate(dates)
        data['Ratio_Cotisations_Revenus'] = self._simulate_membership_ratio(dates)
        data['Dependance_Financement_Public'] = self._simulate_public_funding_dependency(dates)
        data['Solde_Financier'] = self._simulate_financial_balance(dates)
        data['Endettement'] = self._simulate_debt(dates)
        
        # Investissements stratégiques
        data['Investissement_Communication'] = self._simulate_communication_investment(dates)
        data['Investissement_Numérique'] = self._simulate_digital_investment(dates)
        data['Investissement_Formation'] = self._simulate_training_investment(dates)
        data['Investissement_Recherche'] = self._simulate_research_investment(dates)
        data['Investissement_International'] = self._simulate_international_investment(dates)
        
        df = pd.DataFrame(data)
        
        # Ajouter des tendances spécifiques à l'UMP
        self._add_party_trends(df)
        
        return df
    
    def _simulate_adherents(self, dates):
        """Simule le nombre d'adhérents"""
        base_adherents = self.config["adherents_base"]
        
        adherents = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Évolution historique des adhérents selon les périodes politiques
            if 2002 <= year <= 2007:  # Création et présidence Chirac
                growth_rate = 0.15
            elif 2007 <= year <= 2012:  # Présidence Sarkozy
                growth_rate = 0.08
            elif 2012 <= year <= 2014:  # Après défaite 2012
                growth_rate = -0.12
            elif 2014 <= year <= 2016:  # Préparation primaire
                growth_rate = 0.05
            elif 2017 <= year <= 2022:  # Après défaite 2017
                growth_rate = -0.18
            else:  # Reconstruction
                growth_rate = 0.03
                
            growth = 1 + growth_rate * (i/3)
            noise = np.random.normal(1, 0.08)
            adherents.append(base_adherents * growth * noise)
        
        return adherents
    
    def _simulate_federations(self, dates):
        """Simule le nombre de fédérations départementales"""
        base_federations = 100  # Métropole + outre-mer
        
        federations = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2007:
                growth_rate = 0.02
            elif year <= 2012:
                growth_rate = 0.01
            else:
                growth_rate = -0.005
                
            growth = 1 + growth_rate * (i/4)
            federations.append(base_federations * growth)
        
        return federations
    
    def _simulate_elus_locaux(self, dates):
        """Simule le nombre d'élus locaux"""
        base_elus = 50000  # Maires, conseillers municipaux, etc.
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections municipales tous les 6 ans
            if year in [2001, 2008, 2014, 2020]:
                multiplier = 1.15
            else:
                multiplier = 1.0
                
            # Tendance générale
            if year <= 2007:
                growth_rate = 0.03
            elif year <= 2014:
                growth_rate = -0.01
            else:
                growth_rate = -0.02
                
            growth = 1 + growth_rate * (i/5)
            noise = np.random.normal(1, 0.06)
            elus.append(base_elus * growth * multiplier * noise)
        
        return elus
    
    def _simulate_elus_nationaux(self, dates):
        """Simule le nombre d'élus nationaux"""
        base_elus = 300  # Députés, sénateurs, etc.
        
        elus = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Élections législatives tous les 5 ans
            if year in [2002, 2007, 2012, 2017, 2022]:
                if year in [2002, 2007]:  # Majorité UMP
                    multiplier = 1.4
                elif year in [2012]:  # Opposition
                    multiplier = 0.7
                elif year in [2017]:  # LREM majoritaire
                    multiplier = 0.4
                else:  # 2022
                    multiplier = 0.6
            else:
                multiplier = 1.0
                
            growth = 1 - 0.02 * (i/2)  # Tendance décroissante générale
            noise = np.random.normal(1, 0.12)
            elus.append(base_elus * growth * multiplier * noise)
        
        return elus
    
    def _simulate_total_revenue(self, dates):
        """Simule les revenus totaux"""
        base_revenue = self.config["budget_base"]
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Croissance historique des revenus
            if 2002 <= year <= 2007:  # Période faste
                growth_rate = 0.12
            elif 2008 <= year <= 2012:  # Crise financière + fin Sarkozy
                growth_rate = 0.04
            elif 2013 <= year <= 2016:  # Préparation primaire
                growth_rate = 0.08
            elif 2017 <= year <= 2021:  # Après défaite
                growth_rate = -0.10
            else:  # Reconstruction
                growth_rate = 0.05
                
            growth = 1 + growth_rate * (i/3)
            noise = np.random.normal(1, 0.10)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_membership_fees(self, dates):
        """Simule les cotisations des adhérents"""
        base_fees = self.config["budget_base"] * 0.25
        
        fees = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Évolution du nombre d'adhérents et du montant des cotisations
            if year <= 2007:
                growth_rate = 0.10
            elif year <= 2012:
                growth_rate = 0.03
            elif year <= 2016:
                growth_rate = 0.06
            else:
                growth_rate = -0.05
                
            growth = 1 + growth_rate * (i/4)
            noise = np.random.normal(1, 0.08)
            fees.append(base_fees * growth * noise)
        
        return fees
    
    def _simulate_private_donations(self, dates):
        """Simule les dons privés"""
        base_donations = self.config["budget_base"] * 0.35
        
        donations = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Plafonnement des dons et évolution législative
            if year <= 2007:  # Avant plafonnement strict
                multiplier = 1.2
            elif year <= 2012:  # Réglementation renforcée
                multiplier = 0.8
            elif year <= 2017:  # Adaptation
                multiplier = 0.9
            else:  # Nouveaux modes de collecte
                multiplier = 1.1
                
            # Cycles électoraux
            if year in [2002, 2007, 2012, 2017, 2022]:
                electoral_multiplier = 1.8
            else:
                electoral_multiplier = 1.0
                
            growth = 1 + 0.05 * (i/3)
            noise = np.random.normal(1, 0.15)
            donations.append(base_donations * growth * multiplier * electoral_multiplier * noise)
        
        return donations
    
    def _simulate_public_funding(self, dates):
        """Simule le financement public"""
        base_funding = self.config["budget_base"] * 0.30
        
        funding = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Dépend des résultats électoraux
            if year in [2003, 2004, 2005, 2006, 2007, 2008]:  # Majorité présidentielle
                multiplier = 1.4
            elif year in [2012, 2013, 2014, 2015, 2016]:  # Opposition
                multiplier = 0.7
            elif year in [2017, 2018, 2019, 2020, 2021]:  # Faible représentation
                multiplier = 0.4
            else:  # 2022-2025
                multiplier = 0.6
                
            growth = 1 + 0.02 * (i/4)
            noise = np.random.normal(1, 0.08)
            funding.append(base_funding * growth * multiplier * noise)
        
        return funding
    
    def _simulate_event_revenue(self, dates):
        """Simule les revenus des événements"""
        base_revenue = self.config["budget_base"] * 0.05
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Universités d'été, congrès, etc.
            if year in [2002, 2004, 2006, 2010, 2014, 2016, 2021]:
                multiplier = 1.6  # Années de congrès ou universités d'été importantes
            else:
                multiplier = 1.0
                
            growth = 1 + 0.03 * (i/3)
            noise = np.random.normal(1, 0.12)
            revenue.append(base_revenue * growth * multiplier * noise)
        
        return revenue
    
    def _simulate_training_revenue(self, dates):
        """Simule les revenus des formations"""
        base_revenue = self.config["budget_base"] * 0.03
        
        revenue = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2010:  # Développement des formations
                growth = 1 + 0.06 * max(0, (year - 2010)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.10)
            revenue.append(base_revenue * growth * noise)
        
        return revenue
    
    def _simulate_loans(self, dates):
        """Simule les emprunts"""
        base_loans = self.config["budget_base"] * 0.02
        
        loans = []
        for i, date in enumerate(dates):
            year = date.year
            
            # Besoins de financement particuliers
            if year in [2002, 2007, 2012, 2017, 2022]:  # Années électorales
                multiplier = 2.5
            elif year in [2003, 2008, 2013, 2018]:  # Après élections
                multiplier = 1.5
            else:
                multiplier = 1.0
                
            growth = 1 + 0.01 * (i/4)
            noise = np.random.normal(1, 0.20)
            loans.append(base_loans * growth * multiplier * noise)
        
        return loans
    
    def _simulate_total_expenses(self, dates):
        """Simule les dépenses totales"""
        base_expenses = self.config["budget_base"] * 0.95
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [2002, 2007, 2012, 2017, 2022]:  # Années électorales
                multiplier = 1.4
            else:
                multiplier = 1.0
                
            growth = 1 + 0.04 * (i/3)
            noise = np.random.normal(1, 0.08)
            expenses.append(base_expenses * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_staff_expenses(self, dates):
        """Simule les dépenses de personnel"""
        base_staff = self.config["budget_base"] * 0.35
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2012:  # Structure importante
                growth_rate = 0.05
            else:  # Rationalisation
                growth_rate = -0.02
                
            growth = 1 + growth_rate * (i/4)
            noise = np.random.normal(1, 0.06)
            expenses.append(base_staff * growth * noise)
        
        return expenses
    
    def _simulate_campaign_expenses(self, dates):
        """Simule les dépenses de campagne"""
        base_campaign = self.config["budget_base"] * 0.25
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [2002, 2007, 2012, 2017, 2022]:  # Années électorales
                multiplier = 3.0
            elif year in [2001, 2006, 2011, 2016, 2021]:  # Années pré-électorales
                multiplier = 1.8
            else:
                multiplier = 0.5
                
            growth = 1 + 0.03 * (i/3)
            noise = np.random.normal(1, 0.25)
            expenses.append(base_campaign * growth * multiplier * noise)
        
        return expenses
    
    def _simulate_communication_expenses(self, dates):
        """Simule les dépenses de communication"""
        base_communication = self.config["budget_base"] * 0.15
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2010:  # Importance croissante de la communication
                growth = 1 + 0.07 * max(0, (year - 2010)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.12)
            expenses.append(base_communication * growth * noise)
        
        return expenses
    
    def _simulate_operating_expenses(self, dates):
        """Simule les dépenses de fonctionnement"""
        base_operating = self.config["budget_base"] * 0.12
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            growth = 1 + 0.02 * (i/4)
            noise = np.random.normal(1, 0.05)
            expenses.append(base_operating * growth * noise)
        
        return expenses
    
    def _simulate_training_expenses(self, dates):
        """Simule les dépenses de formation"""
        base_training = self.config["budget_base"] * 0.05
        
        expenses = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2008:  # Développement de l'offre de formation
                growth = 1 + 0.05 * max(0, (year - 2008)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.10)
            expenses.append(base_training * growth * noise)
        
        return expenses
    
    def _simulate_loan_repayments(self, dates):
        """Simule les remboursements d'emprunts"""
        base_repayment = self.config["budget_base"] * 0.03
        
        repayments = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2010:  # Accumulation de la dette
                growth = 1 + 0.08 * max(0, (year - 2010)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.15)
            repayments.append(base_repayment * growth * noise)
        
        return repayments
    
    def _simulate_budget_execution_rate(self, dates):
        """Simule le taux d'exécution du budget"""
        rates = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2005:
                base_rate = 0.85
            elif year <= 2012:
                base_rate = 0.88
            elif year <= 2017:
                base_rate = 0.82  # Difficultés financières
            else:
                base_rate = 0.87
                
            noise = np.random.normal(1, 0.04)
            rates.append(base_rate * noise)
        
        return rates
    
    def _simulate_membership_ratio(self, dates):
        """Simule le ratio cotisations/revenus"""
        ratios = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2007:
                base_ratio = 0.28
            elif year <= 2012:
                base_ratio = 0.25
            elif year <= 2017:
                base_ratio = 0.22
            else:
                base_ratio = 0.18  # Baisse de la part des cotisations
                
            noise = np.random.normal(1, 0.05)
            ratios.append(base_ratio * noise)
        
        return ratios
    
    def _simulate_public_funding_dependency(self, dates):
        """Simule la dépendance au financement public"""
        dependencies = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year <= 2007:
                base_dependency = 0.25  # Moins dépendant (dons importants)
            elif year <= 2012:
                base_dependency = 0.32
            elif year <= 2017:
                base_dependency = 0.45  # Plus dépendant
            else:
                base_dependency = 0.38
                
            noise = np.random.normal(1, 0.06)
            dependencies.append(base_dependency * noise)
        
        return dependencies
    
    def _simulate_financial_balance(self, dates):
        """Simule le solde financier"""
        balances = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [2002, 2007, 2012, 2017, 2022]:  # Déficits électoraux
                base_balance = -0.15
            elif year in [2003, 2008, 2013, 2018, 2023]:  # Redressement
                base_balance = 0.08
            else:
                base_balance = 0.02  # Équilibre
                
            noise = np.random.normal(1, 0.10)
            balances.append(base_balance * noise)
        
        return balances
    
    def _simulate_debt(self, dates):
        """Simule l'endettement"""
        base_debt = self.config["budget_base"] * 0.5
        
        debt = []
        current_debt = base_debt
        for i, date in enumerate(dates):
            year = date.year
            
            if year in [2002, 2007, 2012, 2017, 2022]:  # Augmentation dette
                change_rate = 0.25
            elif year in [2004, 2009, 2014, 2019, 2024]:  # Réduction dette
                change_rate = -0.10
            else:
                change_rate = 0.02
                
            current_debt *= (1 + change_rate)
            noise = np.random.normal(1, 0.08)
            debt.append(current_debt * noise)
        
        return debt
    
    def _simulate_communication_investment(self, dates):
        """Simule l'investissement en communication"""
        base_investment = self.config["budget_base"] * 0.08
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2010:
                growth = 1 + 0.09 * max(0, (year - 2010)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.14)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_digital_investment(self, dates):
        """Simule l'investissement numérique"""
        base_investment = self.config["budget_base"] * 0.06
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2012:
                growth = 1 + 0.12 * max(0, (year - 2012)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.18)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_training_investment(self, dates):
        """Simule l'investissement en formation"""
        base_investment = self.config["budget_base"] * 0.04
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2008:
                growth = 1 + 0.06 * max(0, (year - 2008)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.12)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_research_investment(self, dates):
        """Simule l'investissement en recherche"""
        base_investment = self.config["budget_base"] * 0.03
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2015:
                growth = 1 + 0.05 * max(0, (year - 2015)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.15)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _simulate_international_investment(self, dates):
        """Simule l'investissement international"""
        base_investment = self.config["budget_base"] * 0.02
        
        investment = []
        for i, date in enumerate(dates):
            year = date.year
            
            if year >= 2010:
                growth = 1 + 0.04 * max(0, (year - 2010)/10)
            else:
                growth = 1
                
            noise = np.random.normal(1, 0.20)
            investment.append(base_investment * growth * noise)
        
        return investment
    
    def _add_party_trends(self, df):
        """Ajoute des tendances réalistes pour l'UMP"""
        for i, row in df.iterrows():
            year = row['Annee']
            
            # Création de l'UMP (2002)
            if year == 2002:
                df.loc[i, 'Revenus_Total'] *= 1.8
                df.loc[i, 'Adherents'] *= 1.5
            
            # Réélection de Chirac (2002)
            if year == 2002:
                df.loc[i, 'Dons_Prives'] *= 2.2
                df.loc[i, 'Depenses_Campagnes'] *= 2.5
            
            # Élection de Sarkozy (2007)
            if year == 2007:
                df.loc[i, 'Revenus_Total'] *= 1.4
                df.loc[i, 'Depenses_Campagnes'] *= 2.8
            
            # Crise financière (2008-2009)
            if 2008 <= year <= 2009:
                df.loc[i, 'Dons_Prives'] *= 0.75
                df.loc[i, 'Revenus_Total'] *= 0.90
            
            # Défaite présidentielle 2012
            if year == 2012:
                df.loc[i, 'Financement_Public'] *= 0.65
                df.loc[i, 'Adherents'] *= 0.88
            
            # Affaire Bygmalion (2014)
            if year == 2014:
                df.loc[i, 'Dons_Prives'] *= 0.60
                df.loc[i, 'Revenus_Total'] *= 0.85
                df.loc[i, 'Endettement'] *= 1.4
            
            # Changement de nom (2015)
            if year == 2015:
                df.loc[i, 'Investissement_Communication'] *= 1.6
                df.loc[i, 'Depenses_Communication'] *= 1.4
            
            # Primaire 2016
            if year == 2016:
                df.loc[i, 'Revenus_Total'] *= 1.3
                df.loc[i, 'Depenses_Campagnes'] *= 1.8
            
            # Défaite présidentielle 2017
            if year == 2017:
                df.loc[i, 'Financement_Public'] *= 0.45
                df.loc[i, 'Adherents'] *= 0.78
                df.loc[i, 'Elus_Nationaux'] *= 0.35
            
            # COVID-19 (2020)
            if year == 2020:
                df.loc[i, 'Revenus_Evenements'] *= 0.3
                df.loc[i, 'Investissement_Numérique'] *= 1.5
            
            # Élection présidentielle 2022
            if year == 2022:
                df.loc[i, 'Depenses_Campagnes'] *= 2.2
                df.loc[i, 'Dons_Prives'] *= 1.8
    
    def create_financial_analysis(self, df):
        """Crée une analyse complète des finances de l'UMP"""
        plt.style.use('seaborn-v0_8')
        fig = plt.figure(figsize=(20, 24))
        
        # 1. Évolution des revenus et dépenses
        ax1 = plt.subplot(4, 2, 1)
        self._plot_revenue_expenses(df, ax1)
        
        # 2. Structure des revenus
        ax2 = plt.subplot(4, 2, 2)
        self._plot_revenue_structure(df, ax2)
        
        # 3. Structure des dépenses
        ax3 = plt.subplot(4, 2, 3)
        self._plot_expenses_structure(df, ax3)
        
        # 4. Adhérents et structure
        ax4 = plt.subplot(4, 2, 4)
        self._plot_membership_structure(df, ax4)
        
        # 5. Investissements stratégiques
        ax5 = plt.subplot(4, 2, 5)
        self._plot_strategic_investments(df, ax5)
        
        # 6. Indicateurs financiers
        ax6 = plt.subplot(4, 2, 6)
        self._plot_financial_indicators(df, ax6)
        
        # 7. Évolution des élus
        ax7 = plt.subplot(4, 2, 7)
        self._plot_elected_officials(df, ax7)
        
        # 8. Situation financière
        ax8 = plt.subplot(4, 2, 8)
        self._plot_financial_situation(df, ax8)
        
        plt.suptitle(f'Analyse des Finances de l\'{self.parti} ({self.start_year}-{self.end_year})', 
                    fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig(f'UMP_financial_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # Générer les insights
        self._generate_financial_insights(df)
    
    def _plot_revenue_expenses(self, df, ax):
        """Plot de l'évolution des revenus et dépenses"""
        ax.plot(df['Annee'], df['Revenus_Total'], label='Revenus Totaux', 
               linewidth=2, color='#0066CC', alpha=0.8)
        ax.plot(df['Annee'], df['Depenses_Total'], label='Dépenses Totales', 
               linewidth=2, color='#FF6600', alpha=0.8)
        
        ax.set_title('Évolution des Revenus et Dépenses (M€)', 
                    fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Ajouter des annotations pour les événements clés
        key_events = {2002: 'Création UMP', 2007: 'Sarkozy', 2012: 'Défaite', 
                     2015: 'LR', 2017: 'Défaite', 2022: 'Présidentielle'}
        
        for year, event in key_events.items():
            if year in df['Annee'].values:
                y_val = df[df['Annee'] == year]['Revenus_Total'].values[0]
                ax.annotate(event, (year, y_val), xytext=(10, 10), 
                           textcoords='offset points', fontsize=8, 
                           arrowprops=dict(arrowstyle='->', alpha=0.6))
    
    def _plot_revenue_structure(self, df, ax):
        """Plot de la structure des revenus"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Cotisations_Adherents', 'Dons_Prives', 'Financement_Public', 
                     'Revenus_Evenements', 'Revenus_Formations', 'Emprunts']
        colors = ['#0066CC', '#FF6600', '#009900', '#990099', '#FF3366', '#33CCCC']
        labels = ['Cotisations', 'Dons Privés', 'Financement Public', 
                 'Événements', 'Formations', 'Emprunts']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Revenus (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_expenses_structure(self, df, ax):
        """Plot de la structure des dépenses"""
        years = df['Annee']
        width = 0.8
        
        bottom = np.zeros(len(years))
        categories = ['Depenses_Personnel', 'Depenses_Campagnes', 'Depenses_Communication',
                     'Depenses_Fonctionnement', 'Depenses_Formation', 'Remboursements_Emprunts']
        colors = ['#0066CC', '#FF6600', '#009900', '#990099', '#FF3366', '#33CCCC']
        labels = ['Personnel', 'Campagnes', 'Communication', 'Fonctionnement', 'Formation', 'Remboursements']
        
        for i, category in enumerate(categories):
            ax.bar(years, df[category], width, label=labels[i], bottom=bottom, color=colors[i])
            bottom += df[category]
        
        ax.set_title('Structure des Dépenses (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_membership_structure(self, df, ax):
        """Plot des adhérents et structure"""
        # Adhérents
        ax.bar(df['Annee'], df['Adherents']/1000, label='Adhérents (milliers)', 
              color='#0066CC', alpha=0.7)
        
        ax.set_title('Adhérents et Structure Territoriale', fontsize=12, fontweight='bold')
        ax.set_ylabel('Adhérents (milliers)', color='#0066CC')
        ax.tick_params(axis='y', labelcolor='#0066CC')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Fédérations en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Federations_Departementales'], label='Fédérations Départementales', 
                linewidth=2, color='#FF6600')
        ax2.set_ylabel('Fédérations Départementales', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_strategic_investments(self, df, ax):
        """Plot des investissements stratégiques"""
        ax.plot(df['Annee'], df['Investissement_Communication'], label='Communication', 
               linewidth=2, color='#0066CC', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Numérique'], label='Numérique', 
               linewidth=2, color='#FF6600', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Formation'], label='Formation', 
               linewidth=2, color='#009900', alpha=0.8)
        ax.plot(df['Annee'], df['Investissement_Recherche'], label='Recherche', 
               linewidth=2, color='#990099', alpha=0.8)
        
        ax.set_title('Investissements Stratégiques (M€)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Montants (M€)')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_financial_indicators(self, df, ax):
        """Plot des indicateurs financiers"""
        # Taux d'exécution budgétaire
        ax.bar(df['Annee'], df['Taux_Execution_Budget']*100, label='Taux d\'Exécution (%)', 
              color='#0066CC', alpha=0.7)
        
        ax.set_title('Indicateurs Financiers', fontsize=12, fontweight='bold')
        ax.set_ylabel('Taux d\'Exécution (%)', color='#0066CC')
        ax.tick_params(axis='y', labelcolor='#0066CC')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Dépendance financement public en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Dependance_Financement_Public']*100, label='Dépendance Financement Public (%)', 
                linewidth=3, color='#FF6600')
        ax2.set_ylabel('Dépendance Financement Public (%)', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_elected_officials(self, df, ax):
        """Plot de l'évolution des élus"""
        ax.plot(df['Annee'], df['Elus_Locaux']/1000, label='Élus Locaux (milliers)', 
               linewidth=2, color='#0066CC', alpha=0.8)
        
        ax.set_title('Évolution des Élus', fontsize=12, fontweight='bold')
        ax.set_ylabel('Élus Locaux (milliers)', color='#0066CC')
        ax.tick_params(axis='y', labelcolor='#0066CC')
        ax.grid(True, alpha=0.3)
        
        # Élus nationaux en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Elus_Nationaux'], label='Élus Nationaux', 
                linewidth=2, color='#FF6600', alpha=0.8)
        ax2.set_ylabel('Élus Nationaux', color='#FF6600')
        ax2.tick_params(axis='y', labelcolor='#FF6600')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _plot_financial_situation(self, df, ax):
        """Plot de la situation financière"""
        # Solde financier
        ax.bar(df['Annee'], df['Solde_Financier']*100, label='Solde Financier (% du budget)', 
              color=df['Solde_Financier'].apply(lambda x: '#009900' if x > 0 else '#FF6600'), alpha=0.7)
        
        ax.set_title('Situation Financière', fontsize=12, fontweight='bold')
        ax.set_ylabel('Solde Financier (% du budget)', color='#0066CC')
        ax.tick_params(axis='y', labelcolor='#0066CC')
        ax.grid(True, alpha=0.3, axis='y')
        
        # Endettement en second axe
        ax2 = ax.twinx()
        ax2.plot(df['Annee'], df['Endettement'], label='Endettement (M€)', 
                linewidth=3, color='#990099')
        ax2.set_ylabel('Endettement (M€)', color='#990099')
        ax2.tick_params(axis='y', labelcolor='#990099')
        
        # Combiner les légendes
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
    
    def _generate_financial_insights(self, df):
        """Génère des insights analytiques pour l'UMP"""
        print(f"🏛️ INSIGHTS ANALYTIQUES - {self.parti} ({self.start_year}-{self.end_year})")
        print("=" * 70)
        
        # 1. Statistiques de base
        print("\n1. 📈 STATISTIQUES GÉNÉRALES:")
        avg_revenue = df['Revenus_Total'].mean()
        avg_expenses = df['Depenses_Total'].mean()
        avg_adherents = df['Adherents'].mean()
        avg_execution = df['Taux_Execution_Budget'].mean() * 100
        
        print(f"Revenus moyens annuels: {avg_revenue:.2f} M€")
        print(f"Dépenses moyennes annuelles: {avg_expenses:.2f} M€")
        print(f"Adhérents moyens: {avg_adherents:,.0f} personnes")
        print(f"Taux d'exécution budgétaire moyen: {avg_execution:.1f}%")
        
        # 2. Croissance historique
        print("\n2. 📊 ÉVOLUTION HISTORIQUE:")
        revenue_growth = ((df['Revenus_Total'].iloc[-1] / 
                          df['Revenus_Total'].iloc[0]) - 1) * 100
        adherents_growth = ((df['Adherents'].iloc[-1] / 
                           df['Adherents'].iloc[0]) - 1) * 100
        
        print(f"Évolution des revenus ({self.start_year}-{self.end_year}): {revenue_growth:.1f}%")
        print(f"Évolution des adhérents ({self.start_year}-{self.end_year}): {adherents_growth:.1f}%")
        
        # 3. Structure financière
        print("\n3. 📋 STRUCTURE FINANCIÈRE:")
        membership_share = (df['Cotisations_Adherents'].mean() / df['Revenus_Total'].mean()) * 100
        donations_share = (df['Dons_Prives'].mean() / df['Revenus_Total'].mean()) * 100
        public_funding_share = (df['Financement_Public'].mean() / df['Revenus_Total'].mean()) * 100
        
        print(f"Part des cotisations dans les revenus: {membership_share:.1f}%")
        print(f"Part des dons privés: {donations_share:.1f}%")
        print(f"Part du financement public: {public_funding_share:.1f}%")
        
        # 4. Performance et efficacité
        print("\n4. 🎯 PERFORMANCE FINANCIÈRE:")
        avg_balance = df['Solde_Financier'].mean() * 100
        last_debt = df['Endettement'].iloc[-1]
        dependency_public = df['Dependance_Financement_Public'].iloc[-1] * 100
        
        print(f"Solde financier moyen: {avg_balance:.1f}% du budget")
        print(f"Endettement final: {last_debt:.1f} M€")
        print(f"Dépendance au financement public: {dependency_public:.1f}%")
        
        # 5. Spécificités de l'UMP
        print(f"\n5. 🌟 SPÉCIFICITÉS DE L'UMP:")
        print(f"Orientation politique: {self.config['orientation']}")
        print(f"Électorat cible: {', '.join(self.config['electorat_cible'])}")
        print(f"Sources de financement: {', '.join(self.config['sources_financement'])}")
        
        # 6. Événements marquants
        print("\n6. 📅 ÉVÉNEMENTS MARQUANTS:")
        print("• 2002: Création de l'UMP et réélection de Jacques Chirac")
        print("• 2007: Élection de Nicolas Sarkozy")
        print("• 2012: Défaite présidentielle face à François Hollande")
        print("• 2014: Affaire Bygmalion")
        print("• 2015: Changement de nom - Les Républicains")
        print("• 2016: Primaire de la droite et du centre")
        print("• 2017: Défaite présidentielle et effondrement parlementaire")
        print("• 2020: Crise COVID-19 et adaptation numérique")
        print("• 2022: Élection présidentielle et législatives")
        
        # 7. Recommandations stratégiques
        print("\n7. 💡 RECOMMANDATIONS STRATÉGIQUES:")
        print("• Diversifier les sources de financement")
        print("• Renforcer la collecte des cotisations")
        print("• Développer le fundraising numérique")
        print("• Optimiser la structure des dépenses")
        print("• Investir dans la formation des cadres")
        print("• Renforcer la présence territoriale")
        print("• Améliorer la transparence financière")
        print("• Développer les partenariats avec la société civile")

def main():
    """Fonction principale pour l'analyse de l'UMP"""
    print("🏛️ ANALYSE DES FINANCES DE L'UMP/LES RÉPUBLICAINS (2002-2025)")
    print("=" * 60)
    
    # Initialiser l'analyseur
    analyzer = UMPFinanceAnalyzer()
    
    # Générer les données
    financial_data = analyzer.generate_financial_data()
    
    # Sauvegarder les données
    output_file = 'UMP_financial_data_2002_2025.csv'
    financial_data.to_csv(output_file, index=False)
    print(f"💾 Données sauvegardées: {output_file}")
    
    # Aperçu des données
    print("\n👀 Aperçu des données:")
    print(financial_data[['Annee', 'Adherents', 'Revenus_Total', 'Depenses_Total', 'Taux_Execution_Budget']].head())
    
    # Créer l'analyse
    print("\n📈 Création de l'analyse financière...")
    analyzer.create_financial_analysis(financial_data)
    
    print(f"\n✅ Analyse des finances de l'{analyzer.parti} terminée!")
    print(f"📊 Période: {analyzer.start_year}-{analyzer.end_year}")
    print("📦 Données: Revenus, dépenses, adhérents, élus, indicateurs financiers")

if __name__ == "__main__":
    main()