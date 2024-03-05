"""
Aufgabe:
Sie haben die historischen Renditen von drei verschiedenen
Investmentportfolios A, B und C sowie die Rendite eines risikofreien
Wertpapiers und eines Marktindex für denselben Zeitraum gegeben.
Ihre Aufgabe ist es, die Sharpe Ratio, Treynor Ratio und Jensen's Alpha
für jedes Portfolio zu berechnen und zu interpretieren.

"""


# Formeln
def calc_all(portfolio, beta, Rp, sigma_p):
    print(f"Portfolio: {portfolio}")
    sharpe_ratio = (Rp - Rf) / sigma_p
    print(f"sharpe_ratio {sharpe_ratio}")

    treynor_ratio = (Rp - Rf) / beta
    print(f"treynor_ratio {treynor_ratio}")

    jensens_alpha = Rp - (Rf + beta * (Rm - Rf))
    print(f"jensens_alpha {jensens_alpha}")
    print("\n --------------------------- \n")


# Variablen
Rf = 0.02
Rm = 0.08

portfolio = "A"
beta = 0.8
Rp = 0.06
sigma_p = 0.1
calc_all(portfolio, beta, Rp, sigma_p)

portfolio = "B"
beta = 1.2
Rp = 0.09
sigma_p = 0.14
calc_all(portfolio, beta, Rp, sigma_p)

portfolio = "C"
beta = 1.0
Rp = 0.07
sigma_p = 0.11
calc_all(portfolio, beta, Rp, sigma_p)

print("""
Sharp Ratio: misst Verhältnis der Rendite einer Anlage zu ihrem Risiko
je höher desto besser
Portfolio B bietet damit den höchsten Wert bei der Sharp Ratio mit 0.5 bzw. 5%
Rangordnung: B > C > A
---------------------------------------------------------------------------\n

Treynor Ratio: misst Verhältnis der Rendite einer Anlage zum Systematischen Risiko (beta).
je höher desto besser 
Portfolio B bietet damit den höchsten Wert bei der Treynor Ratio mit 0.583 bzw. 5.8%
Rangordnung: B > C > A
---------------------------------------------------------------------------\n

Jensen's Alpha: misst die Überrendite einer Anlage im Vergleich zu dem, was aufgrund ihres
systematischen Risikos zu erwarten wäre (beta).
je höher desto besser
positiver Wert = performance ist besser als erwartet
negativer Wert = performance ist schlechter als erwartet 
Portfolio C bietet damit den höchsten Wert bei der Jensen's Alpha mit -0.01 bzw. -1%
Wobei alle Portfolios schlechter abschneiden als aufgrund des Systematischen Fehlers erwartet wird
Rangordnung: C > A > B
""")
