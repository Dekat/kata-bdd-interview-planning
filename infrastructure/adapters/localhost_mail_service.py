from domain import ports


class LocalhostMailService(ports.EmailService):

    def send_email(self, email_address: str) -> None:
        # TODO: implement it !
        pass
