from .base import BaseParser

FAKE_DATA = {
    'config': {
        'involved_facts': [
            'Ticket', 'Money'
        ]
    },
    'rules': [
        {
            'name': 'have_ticket',
            'left_hand_side': "Ticket(ticket='yes')",
            'right_hand_side': {
                'executor': '',
                'args': []
            }
        },
        {
            'name': 'have_ticket_and_money',
            'left_hand_side': "AND(Money(money='yes'), Ticket(ticket='yes'))",
            'right_hand_side': {
                'executor': '',
                'args': []
            }
        },
        {
            'name': 'buy_ticket',
            'left_hand_side': "AND(Money(money='yes'), Ticket(ticket='no'))",
            'right_hand_side': {
                'executor': '',
                'args': []
            },

        },
        {
            'name': 'no_money_nor_ticket',
            'left_hand_side': "AND(Money(money='no'), Ticket(ticket='no'))",
            'right_hand_side': {
                'executor': '',
                'args': []
            },

        }
    ]
}


class StaticDataParser(BaseParser):
    def init(self, **kwargs):
        pass

    def parse(self, **kwargs):
        return FAKE_DATA
