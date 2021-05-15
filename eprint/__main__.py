from eprint import eprint
from eprint.str import ok

if __name__ == "__main__":
    eprint("Looks cool?")
    eprint.ok("Success")
    eprint.error("Failed")
    eprint.info("Use color for {} that need {} ", "values", "attention")
    print(ok("OK"))
