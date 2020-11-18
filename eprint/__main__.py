from .eprint import eprint


if __name__ == "__main__":
    eprint("Looks cool?")
    eprint.ok("Success")
    eprint.error("Failed")
    eprint.ok("Use color for {} that need {} ", "values", "attention")
