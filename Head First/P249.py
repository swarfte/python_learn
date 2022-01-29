def log_request(req: 'flask_request', res: str, ) -> None:
    ###最大行數:4行
    with open("vsearch.log", "a") as log:
        print(req, res, file=log, end="")

    ###
