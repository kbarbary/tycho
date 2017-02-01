from argparse import ArgumentParser

def main(argv=None):
    DESCRIPTION = "Determine SN light curve type"
    parser = ArgumentParser(prog="tycho", description=DESCRIPTION)
    args = parser.parse_args(argv)
