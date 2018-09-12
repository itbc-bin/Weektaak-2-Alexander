while 1:

    print("""
Welkom hier kan je het CG% uit laten rekenen.""")
    seq = input("Voer je DNA/RNA/Protein sequentie nu in:")
    CGPerc = seq.count("C") + seq.count("G")
    Alles = seq.count("T") + seq.count("C") + seq.count("A") + seq.count("G")
    MiniCGPerc = CGPerc / Alles
    Perc = MiniCGPerc * 100
    Resultaat = """
Het CG Percentage is """+str(Perc)
    print(Resultaat)
    print("Het aantal nucleotiden zijn "+str(Alles))
    print("-----------------------")
