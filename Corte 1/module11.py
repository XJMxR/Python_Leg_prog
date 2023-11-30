def OtorgarPrestamo(pSalario,
                    pAntiguedad,
                    pSaldoBancario,
                    pGastosMensuales, 
                    pReport, 
                    pValorSolic ):
    if pSalario > 1200000 and pAntiguedad > 2 and pValorSolic <= pSaldoBancario and pReport == False:
        return True
    else:
        return False
