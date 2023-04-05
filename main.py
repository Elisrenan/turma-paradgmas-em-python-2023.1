match status:
  case 400:
    print("Bad request")
  case 404:
    print("Not found")
  case 418:
    print("I'm a teapot")
  case _:
    print("Something's wrong with the internet")